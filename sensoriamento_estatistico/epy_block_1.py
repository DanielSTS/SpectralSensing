# encoding: utf-8
import numpy as np
from gnuradio import gr
from scipy.stats import jarque_bera,anderson


class blk(gr.sync_block): 
  
    backup = 0
    
    def __init__(self,teste_aderencia ='jarque_bera', num_amostras = 1024): 
       
        gr.sync_block.__init__(
            self,
            name='Detector Estatístico', 
            in_sig=[np.complex64],
            out_sig=[np.complex64]
        )
	self.teste_aderencia = teste_aderencia
	self.num_amostras = num_amostras
	
	
	

    def work(self, input_items, output_items):

	teste = self.teste_aderencia
	num = self.num_amostras
	
	if not isinstance(self.backup,int):
		 vetor_amostras = np.append(self.backup,np.abs(input_items[0]))
	else:
		 vetor_amostras = np.abs(input_items[0])

	n = len(vetor_amostras)
	print(n)
	

        if n >= self.num_amostras: 

		if teste == 'jarque_bera':
			JB = jarque_bera(vetor_amostras[:num])
			#print(JB)
			if JB[1] > 0.05:
				print("livre")
			else:
				print("Ocupado")

		elif teste == 'anderson':
 			AD = anderson(vetor_amostras[:num])
			#print(AD)
			if AD[0] < AD[1][2]:
				print("Livre")
			else:
				print("Ocupado")
		
	else:
        	self.backup = vetor_amostras
		
		
	return len(output_items[0])










