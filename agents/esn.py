'''
Created on Oct 22, 2013

@author: vinnie
'''

import random
import numpy as np
import matplotlib.pyplot as plt


symbol_map = {'R': -1, 'P': 0, 'S': 1}
value_map = {-1:'R', 0:'P', 1:'S'}
n = 10
def make_symbol(p):
    return value_map[min(symbol_map.values(), key=lambda x:abs(x-p))]
    
if input == '':
    beat = {'R': 'P', 'P': 'S', 'S': 'R'}
    output = random.choice(['R','P','S'])
    esn = ESN(1,100,1)
    esn.gen_weights()
    i = 0
    utrain = []
    ytrain = []
else:
    if i < n:
        output = random.choice(['R','P','S'])
        utrain.append(symbol_map[input])
        ytrain.append(symbol_map[beat[input]])
    elif i == n:
        print utrain
        print ytrain
        esn.train(np.array(utrain), np.array(ytrain))
        output = random.choice(['R','P','S'])
    else:
        p = esn.step(symbol_map[input])
        p_symbol = make_symbol(p)
        output = beat[p_symbol]
    
    i += 1