# -*- coding: utf-8 -*-
"""
Created on Mon Dec  8 04:43:09 2025

@author: Callum
"""
import math

# Ok should be a simple matter of parsing, forming lists and then using sum or prod

class mathSolver():
    def __init__(self, filePath: str, totalVal: int  = 0):
        self.filePath = filePath
        self.totalVal = totalVal
        self.questionLists = []
        
    def processFile(self):
        with open(self.filePath) as f:
            listCheck = False
            for line in f:
                line = line.strip()
                if '*' in line or '+' in line:
                    numLine = [x for x in line.split()]
                else:
                    numLine = [int(x) for x in line.split()]
                for idx, n in enumerate(numLine):
                    if not listCheck:
                        self.questionLists.append([n])
                    else: 
                        self.questionLists[idx].append(n)
                listCheck = True
                        
    def runEquation(self):
        for numList in self.questionLists:
            val = 0
            if numList[-1] == '+':
                val = sum(numList[:-1])
            elif numList[-1] == '*':
                val = math.prod(numList[:-1])
            self.totalVal += val


# mS = mathSolver('./day_6_input.txt')
# mS.processFile()
# mS.runEquation()

# print(mS.questionLists)
# print(mS.totalVal)
            
                
                        
                    
                    
                