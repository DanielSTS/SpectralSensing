# encoding: utf-8
import numpy as np
from gnuradio import gr
from scipy.special import erfinv
from math import sqrt


class blk(gr.sync_block): 
  
    energia = 0
    controle = 0
    variancia = 0.0	
    aux_somatorio = 0
    somatorio = 0.0

    def __init__(self, num_amostras = 10): 
       
        gr.sync_block.__init__(
            self,
            name='Variancia do Ruido', 
            in_sig=[np.complex64],
            out_sig=[np.complex64]
        )
        
	self.num_amostras = num_amostras
	
	
	
    def work(self, input_items, output_items):

	
        vetor_amostras = np.abs(input_items[0])
	limite = self.num_amostras
	    
    	if (self.controle < self.num_amostras): 

	    if(len(vetor_amostras) < self.num_amostras): #altera o limite caso o vetor_amostra seja menor que o num_amostras necessárias
		    
	    	limite = len(vetor_amostras)
    
	    for i in range (limite): 

	    	self.energia += vetor_amostras[i] * vetor_amostras[i]
		self.controle += 1
			
	     	if(self.controle == self.num_amostras):
			self.variancia = (1.0/self.num_amostras) * self.energia
			self.somatorio += self.variancia               	   
		        self.controle = 0
		        self.energia = 0
                	self.variancia = 0.0
			self.aux_somatorio += 1
			break
		if(self.aux_somatorio == self.num_amostras):
			print(self.somatorio / self.num_amostras)
			self.aux_somatorio = 0
			self.somatorio = 0	

	return len(output_items[0])









