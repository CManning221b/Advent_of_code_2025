# -*- coding: utf-8 -*-
"""
Created on Tue Dec  2 15:09:36 2025

@author: Callum
"""

from typing import List, Tuple

# Process inputs
# Comma seperated ranges
# get each range
# take the lowest and highest numbers
# shift those numbers (up for lowest, down for highest) till they both have even digits
# split the digits of the lowest in half '2234' becomes '22'
# Generate duplicate numbers till we are outside the range of the highest numbers eg. 2222, 2323, 2424
# Save all the valid numbers
# sum them up

# Single Range Class ID Validator - Treat it like an adder, take the overflow !
class SingleRangeIDValidator():
    def __init__(self, minNum: int, maxNum: int, validIdLst: List = []):
        self.minNum = minNum
        self.maxNum = maxNum
        self.validIdLst = validIdLst
        self.runningTotal = sum(self.validIdLst)
    
    def shiftLowest(self):
        lowLength = len(str(self.minNum))
        if lowLength%2 != 0:
            newMin = 10**(lowLength)
            self.minNum = newMin
            #check new min not bigger than old max
    
    def shiftHighest(self):
        highLength = len(str(self.mzxNum))
        if highLength%2 != 0:
            newMax = (10**highLength) - 1
            self.maxNum = newMax
            #Probably don't need this
            
    def genCanidateLst(self):
        canidateLst = []
        lowLength = len(str(self.minNum))
        if lowLength%2 != 0:
            print("Valid IDs must have even number of digits")
            return []
        currentCanidate = 0
        splt = int(lowLength/2)
        genBase = str(self.minNum)[:(splt)]
        while currentCanidate <= self.maxNum:
            if currentCanidate != 0 and currentCanidate >= self.minNum:
                print(f'Adding canidate {currentCanidate}')
                canidateLst.append(currentCanidate)
            currentCanidate = int(genBase + genBase)
            genBase = str(int(genBase)+1)
        return canidateLst
    
    def runReigon(self):
        print(f'The intial min number is {self.minNum}')
        self.shiftLowest()
        print(f'The shifted min number is {self.minNum}')
        if self.minNum < self.maxNum:
            canidates = self.genCanidateLst()
            self.validIdLst.extend(canidates)
            self.runningTotal = sum(self.validIdLst)
            print(self.runningTotal)
        return self.validIdLst

#Open the file 
#Get a list of comma seperated reigons

class MultiRangeIDvalidator():
    def __init__(self, filePath: str, validIdLst: List = []):
        self.filePath = filePath
        self.validIdLst = validIdLst
        self.runningTotal = sum(self.validIdLst)
        self.reigonLst = []
        
    def processLine(self, line: str):
        minN, maxN = line.split('-')
        return (int(minN), int(maxN))
    
    def processList(self, lst: str):
        for l in lst.split(','):
            self.reigonLst.append(self.processLine(l))
    
    def processFile(self):
        f = open(self.filePath)
        self.processList(f.read())
        
    def runReigon(self, reigonTuple: Tuple[int, int]):
        validator = SingleRangeIDValidator(reigonTuple[0], reigonTuple[1], self.validIdLst)
        self.validIdLst = validator.runReigon()
        self.runningTotal = sum(self.validIdLst)
    
    def runAll(self):
        self.processFile()
        for reigonTuple in self.reigonLst:
            print(f'Running Validator for range {reigonTuple}')
            self.runReigon(reigonTuple)
            print('\n\n\n')
        print(f'Final Valid List is {self.validIdLst}')
        print(f'The running total is {self.runningTotal}')
        return self.runningTotal
        
    
    

# validator = SingleRangeIDValidator(1188511880, 1188511890)     
# validator.runReigon()   

# multiValidator = MultiRangeIDvalidator('./day_2_test.txt')
# multiValidator.runAll()        
            
# multiValidator = MultiRangeIDvalidator('./day_2_input.txt')
# multiValidator.runAll()  
        
