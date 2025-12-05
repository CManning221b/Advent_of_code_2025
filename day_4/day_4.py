# -*- coding: utf-8 -*-
"""
Created on Fri Dec  5 12:03:12 2025

@author: Callum
"""
import numpy as np
from typing import List, Tuple
from numpy.typing import NDArray
from scipy.signal import convolve2d
from pprint import pprint

# Its a convolution problem
# Massive binary matrix (1,0)
# New matrix where each cell is the sum of the 8 surrounding cells multiplied by its own value
# Then a filter which goes cell by cell and checks for values less than 4
# Then sum the number of those cells

# Need a matrix processor
# Some sort of costume kernal scipy.ndimage.generic_filter, scipy.signal.convolve2d
# correlate and a boolena mask
class matrixProcessor():
    def __init__(self, binMatrix: NDArray, kernel: NDArray, threshold: int = 4, totalVal: int = 0 ):
        self.totalVal = totalVal
        self.threshold = threshold
        self.binMatrix = binMatrix
        self.kernel = kernel
    
    def convMult(self):
        filteredMatrix = convolve2d(self.binMatrix, self.kernel, mode = "same", boundary = 'fill', fillvalue=0)
        pprint(filteredMatrix)
        print('\n')
        filteredMatrix = (self.binMatrix * filteredMatrix) + self.binMatrix
        pprint(filteredMatrix)
        print('\n')
        parse = np.vectorize(lambda x: int(x > 0 and x < (self.threshold+1)))
        boolMatrix = parse(filteredMatrix)
        pprint(boolMatrix)
        self.totalVal =  np.sum(boolMatrix)
        return boolMatrix

# Need an ingestor, goes line by line and char by char - produces matrix
class matrixIngestor():
    def __init__(self, filePath: str, totalVal: int  = 0, threshold: int  = 4 ):
        self.filePath = filePath
        self.totalVal = totalVal
        self.threshold = threshold
        self.npArray = None
        
    def setUpKernel(self):
        kernel = np.array([[1,1,1],[1,0,1],[1,1,1]])
        return kernel
    
    def convertLine(self, line:str = ''):
        charArr =  np.array(list(line.strip()))
        parse = np.vectorize(lambda x: int(x == '@'))
        binArr = parse(charArr)
        return binArr
    
    def processArr(self):
        kern = self.setUpKernel()
        m = matrixProcessor(self.npArray, kern, self.threshold, self.totalVal)
        m.convMult()
        self.totalVal = m.totalVal
        
    def processFile(self):
        lineList = []
        with open(self.filePath) as f:
            for line in f:
                lineArray = self.convertLine(line)
                lineList.append(lineArray)
        self.npArray = np.array(lineList)
                
                


m = matrixIngestor('day_4_input.txt')
m.processFile()
pprint(m.npArray)
print('\n')
m.processArr()
print(f'\n\nThe total value is {m.totalVal}')
