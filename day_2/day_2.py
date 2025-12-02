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
        highLength = len(str(self.maxNum))
        if highLength%2 != 0:
            newMax = (10**highLength) - 1
            self.maxNum = newMax
            #Probably don't need this
            
    def genCanidateLst(self):
        candidateLst = []
        lowLength = len(str(self.minNum))
        if lowLength%2 != 0:
            print("Valid IDs must have even number of digits")
            return []
        currentCanidate = 0
        splt = int(lowLength/2)
        genBase = str(self.minNum)[:(splt)]
        while currentCanidate <= self.maxNum:
            if currentCanidate != 0 and currentCanidate >= self.minNum:
                print(f'Adding candidate {currentCanidate}')
                candidateLst.append(currentCanidate)
            currentCanidate = int(genBase + genBase)
            genBase = str(int(genBase)+1)
        return candidateLst
    
    def runRegion (self):
        print(f'The intial min number is {self.minNum}')
        self.shiftLowest()
        print(f'The shifted min number is {self.minNum}')
        if self.minNum < self.maxNum:
            candidates = self.genCanidateLst()
            self.validIdLst.extend(candidates)
            self.runningTotal = sum(self.validIdLst)
            print(self.runningTotal)
        return self.validIdLst

#Open the file 
#Get a list of comma seperated region s

class MultiRangeIDvalidator():
    def __init__(self, filePath: str, validIdLst: List = []):
        self.filePath = filePath
        self.validIdLst = validIdLst
        self.runningTotal = sum(self.validIdLst)
        self.region Lst = []
        
    def processLine(self, line: str):
        minN, maxN = line.split('-')
        return (int(minN), int(maxN))
    
    def processList(self, lst: str):
        for l in lst.split(','):
            self.region Lst.append(self.processLine(l))
    
    def processFile(self):
        with open(self.filePath) as f:
            self.processList(f.read())
        
    def runRegion (self, region Tuple: Tuple[int, int]):
        validator = SingleRangeIDValidator(region Tuple[0], region Tuple[1], self.validIdLst)
        self.validIdLst = validator.runRegion ()
        self.runningTotal = sum(self.validIdLst)
    
    def runAll(self):
        self.processFile()
        for region Tuple in self.region Lst:
            print(f'Running Validator for range {region Tuple}')
            self.runRegion (region Tuple)
            print('\n\n\n')
        print(f'Final Valid List is {self.validIdLst}')
        print(f'The running total is {self.runningTotal}')
        return self.runningTotal
        
    
    

validator = SingleRangeIDValidator(95, 115)     
validator.runRegion ()   

# multiValidator = MultiRangeIDvalidator('./day_2_test.txt')
# multiValidator.runAll()        
            
# multiValidator = MultiRangeIDvalidator('./day_2_input.txt')
# multiValidator.runAll()  
        
