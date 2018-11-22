# encoding: utf-8
import numpy as np
from gnuradio import gr
from scipy.stats import jarque_bera,anderson

class blk(gr.sync_block):
    
    def __init__(self, teste_aderencia ='jarque_bera', num_amostras = 1024): 
        
        gr.sync_block.__init__(
            self,
            name='Detector Estatístico',   
            in_sig=[np.complex64],
            out_sig=[np.complex64]
        )
	self.teste_aderencia = teste_aderencia
	self.num_amostras = num_amostras
	
	


    def work(self, input_items, output_items):
		
		
		arquivo_detec=open('/home/daniel/Gnuradio_Workspace/sensoriamento_estatistico/detec.txt','a')
		num_slots = int(len(input_items[0])/ self.num_amostras)
		vetor = np.array_split(abs(input_items[0]),num_slots)
		teste = self.teste_aderencia
		n = len(vetor)
		
		
		if teste == 'jarque_bera':
			for i in range(n):
				JB = jarque_bera(vetor[i])
				print(JB)
				if JB[1] > 0.05:
					print("livre")
				else:
					print("Ocupado")

		elif teste == 'anderson':
 			for i in range(n): 
				AD = anderson(vetor[i])
				print(AD)
				if AD[0] < AD[1][2]:
					print("Livre")
				else:
					print("Ocupado")
		
			
			
				
		
		arquivo_detec.close()

		return len(output_items[0])

