# -*- coding: utf-8 -*-
"""
Created on Wed Dec  3 17:41:09 2025

@author: callu
"""

from typing import List, Tuple

# Battery Bank 
# Bank is n cells wide
# Search n-1 cells for the highest number
# Find the highest at cell position m
# Search m+1 to n 

class bank():
    def __init__(self, cellLst: List = None):
        self.cellLst = cellLst if cellLst else []
        self.tensValue = 0
        self.tensIndex = 0
        self.unitsValue = 0
        self.unitIndex = 0
        self.highValue = 0
        
    def processLine(self, line):
        self.cellLst = list(int(c) for c in line)
    
    def findTens(self):
        possibilities = self.cellLst[:-1]
        self.tensValue = max(possibilities)
        self.tensIndex = possibilities.index(self.tensValue)
    
    def findUnits(self):
        possibilities = self.cellLst[self.tensIndex+1:]
        self.unitsValue = max(possibilities)
        self.unitIndex = possibilities.index(self.unitsValue)
    
    def runAll(self):
        self.findTens()
        self.findUnits()
        self.highValue = int(str(self.tensValue)+str(self.unitsValue))
        return self.highValue


# test_string = "818181911112111"  

# b = bank()
# b.processLine(test_string)
# b.runAll()
    
class fullBank():
    def __init__(self, filePath: str,):
        self.filePath = filePath
        self.bankValue = []
        self.valueTotal = 0
    
    def processFile(self):
        with open(self.filePath) as f:
            for line in f:
                b = bank()
                b.processLine(line.strip())
                hV = b.runAll()
                self.bankValue.append(hV)
        self.valueTotal = sum(self.bankValue)
        print(self.bankValue)
        print(f'The total value is {self.valueTotal}')
        return self.valueTotal
        
# fB = fullBank('./day_3_input.txt')
# fB.processFile()
                
                
            
            