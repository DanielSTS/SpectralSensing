# encoding: utf-8
import numpy as np
from gnuradio import gr
from scipy.special import erfinv
from math import sqrt
import datetime 


class blk(gr.sync_block): 
  
    energia = 0
    controle = 0 	
    
    def __init__(self, num_amostras = 10, variancia_ruido  = 0, snr = -10): 
       
        gr.sync_block.__init__(
            self,
            name='Detector de Energia', 
            in_sig=[np.complex64],
            out_sig=[np.complex64]
        )
        pfa = 0.1
	self.num_amostras = num_amostras
	self.variancia_ruido = variancia_ruido
	self.snr = snr
	self.limiar = variancia_ruido * ( erfinv(1 - 2*pfa ) * 2 * sqrt(num_amostras) + num_amostras )
	
	
	

    def work(self, input_items, output_items):

	detector = open('/home/daniel/Gnuradio_Workspace/sensoriamento_deteccao_energia/dados.txt','a') 
        vetor_amostras = np.abs(input_items[0])
	limite = self.num_amostras
	
	#print(len(input_items[0]))

	if (self.controle < self.num_amostras): 

		if(len(vetor_amostras) < self.num_amostras): #altera o limite caso o vetor_amostra seja menor que o num_amostras necessárias
			
			limite = len(vetor_amostras)
	
		for i in range (limite): 

			self.energia += vetor_amostras[i] * vetor_amostras[i]
			self.controle += 1
			
			if(self.controle == self.num_amostras):#após calcular a energia é feita a decisão 
		
				if (self.energia < self.limiar):
				
					print("canal livre") 
					dados = ['canal livre',self.energia,self.limiar,self.snr,str(datetime.datetime.now())]
					detector.write('%s' %dados)
					detector.write('\n')
					self.controle = 0
					self.energia = 0
					break

				else:
					print("canal ocupado")
					dados = ['canal ocupado',self.energia,self.limiar,self.snr,str(datetime.datetime.now())]
					detector.write('%s' %dados)
					detector.write('\n')
					self.controle = 0
					self.energia = 0
					break
			
	detector.close()
	return len(output_items[0])









