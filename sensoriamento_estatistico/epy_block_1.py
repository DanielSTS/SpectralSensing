
#from __future__ import division, print_function, absolute_import

#import warnings
#import math
#from collections import namedtuple

import numpy as np
#from numpy import array, asarray, ma, zeros

#from scipy._lib.six import callable, string_types
#from scipy._lib._version import NumpyVersion
#import scipy.special as special
#import scipy.linalg as linalg
from scipy.stats import distributions
#import numpy
#from scipy.stats import kurtosis, skew, stats
from gnuradio import gr

class blk(gr.sync_block):  
    

    def __init__(self):  
        
        gr.sync_block.__init__(
            self,
            name='Jarque Bera',  
            in_sig=[np.float32],
            out_sig=[np.float32],
        )
	
        
        

    def work(self, input_items, output_items):

		arquivo_detec=open('/home/daniel/Gnuradio_Workspace/sensoriamento_estatistico/detec.txt','a')
		
		n = float(input_items[0].size)
		mu = input_items[0].mean()
		diffx = input_items[0] - mu
		skewness = (1 / n * np.sum(diffx**3)) / (1 / n * np.sum(diffx**2))**(3 / 2.)
		kurtosis = (1 / n * np.sum(diffx**4)) / (1 / n * np.sum(diffx**2))**2
		JB = n / 6 * (skewness**2 + (kurtosis - 3)**2 / 4)
		p = 1 - distributions.chi2.cdf(JB, 2)
		for i in range(len(input_items[0])):

			a=p * input_items[0][i]
			
			if JB > a:
				
				
				vetor_dados_detec = [p, input_items[0][i], a, JB]
				
				arquivo_detec.write('%s' %vetor_dados_detec)
				
				arquivo_detec.write('\n')
				
		
		arquivo_detec.close()
		
		return len(output_items[0])



