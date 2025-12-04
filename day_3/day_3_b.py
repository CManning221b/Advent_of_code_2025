# -*- coding: utf-8 -*-
"""
Created on Wed Dec  3 18:12:20 2025

@author: callu
"""
from typing import List, Tuple

from day_3 import bank, fullBank

# Essentially a constraint satisfaction problem
# We want to sort the list so we have the 12 largest digits up front
# but which satisfies the constraint that their index is in size order
# So we can shift small numbers further down, but we can't shift any number up
# Got to find the largest number in the lowest poistion


# Oh Oh New Idea
# So we need to find the biggest no.
# In a fixed range
# The first number can only be in the first four digits
# The second number then can only be between that and 11 digits left
# The third digit then...
# so its between the last digit and the final possible digit


class bankModified(bank):
    def __init__(self, cellLst: List = None, cellNum: int = 12):
        self.cellLst = cellLst if cellLst else []
        self.valueArray = []
        self.indexArray = []
        self.cellNum = cellNum
        self.highValue = 0
            
    def scanForHigh(self):
        l = len(self.cellLst)
        minNo = 0
        self.valueArray = []
        self.indexArray = []
        for i in range(self.cellNum):
            remaining = self.cellNum - i - 1
            maxNo = l - remaining
            window = [(self.cellLst[j], j) for j in range(minNo, maxNo)]
            max_value, max_index = max(window, key=lambda x: x[0])
            self.valueArray.append(max_value)
            self.indexArray.append(max_index)
            minNo = max_index + 1
    
            
    def concatDigits(self):
        chrlst = list(str(d) for d in self.valueArray)
        self.highValue = int(''.join(chrlst))
    
    def runAll(self):
        self.scanForHigh()
        self.concatDigits()
        return self.highValue
        

class fullBankModified(fullBank):
    def processFile(self):
        with open(self.filePath) as f:
            for line in f:
                b = bankModified()
                b.processLine(line.strip())
                hV = b.runAll()
                self.bankValue.append(hV)
        self.valueTotal = sum(self.bankValue)
        print(self.bankValue)
        print(f'The total value is {self.valueTotal}')
        return self.valueTotal
    
fB = fullBankModified('./day_3_input_tst.txt')
fB.processFile() 
    
