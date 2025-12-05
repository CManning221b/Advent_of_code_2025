# -*- coding: utf-8 -*-
"""
Created on Fri Dec  5 14:23:04 2025

@author: Callum
"""
from pprint import pprint

# Now its all just a matter of recursion

from day_4 import matrixProcessor, matrixIngestor

class modifiedMatrixIngestor(matrixIngestor):
    def processArr(self):
        kern = self.setUpKernel()
        subTotal = - 1
        arr = self.npArray
        while subTotal != 0:
            m = matrixProcessor(arr, kern, self.threshold, 0)
            removable = m.convMult()
            subTotal  = m.totalVal
            self.totalVal += subTotal
            arr = arr - removable
        
m = modifiedMatrixIngestor('day_4_input.txt')
m.processFile()
pprint(m.npArray)
print('\n')
m.processArr()
print(f'\n\nThe total value is {m.totalVal}')