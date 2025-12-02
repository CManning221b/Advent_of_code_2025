# -*- coding: utf-8 -*-
"""
Created on Tue Dec  2 16:36:59 2025

@author: Callum
"""

from functools import reduce
from typing import List, Tuple
from day_2 import SingleRangeIDValidator, MultiRangeIDvalidator


# Single Range Class ID Validator - Treat it like an adder, take the overflow !
class SingleRangeIDValidatorModified(SingleRangeIDValidator):
   
    # We need to now take the factors of the length of the number, 
    # not including itself or 1
    # Go from largest to lowest factor
    # For each set of factors, start at lowest numver and repeat
    # Heading up towars max
    
    def getFactors(self, n: int):
        return set(reduce(list.__add__,([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
    
    def getCombinedFactors(self):
        lowFactors = self.getFactors(len(str(self.minNum)))
        highFactors = self.getFactors(len(str(self.maxNum)))
        combinedList = lowFactors | highFactors
        combinedList.remove(1)
        return list(combinedList)
        
    
    def genSubLists(self, number: int, factor: int, candidateList: List = []):
        subCandidateLst = []
        currentCandidate = 0
        splitSize = int(len(str(number))/factor)
        partlist = list(map(''.join, zip(*[iter(str(number))]*splitSize)))#
        if len(partlist)>0:
            genBase = partlist[0]
            while currentCandidate <= self.maxNum:
                if currentCandidate != 0 and currentCandidate >= self.minNum and currentCandidate not in candidateList:
                    print(f'Adding candidate {currentCandidate}')
                    subCandidateLst.append(currentCandidate)
                currentCandidate = int(genBase*factor)
                genBase = str(int(genBase)+1)
        return subCandidateLst
                
        
    def genCandidateLst(self):
        candidateLst = []
        factors = self.getCombinedFactors()
        for factor in factors:
            subList = self.genSubLists(self.minNum, factor, candidateLst)
            candidateLst.extend(subList)
            subList = self.genSubLists(self.maxNum, factor, candidateLst)
            candidateLst.extend(subList)
        return candidateLst
       
    
    def runReigon(self):
        print(f'Checking reigon between {self.minNum} and {self.maxNum}')
        candidates = self.genCandidateLst()
        self.validIdLst.extend(candidates)
        self.runningTotal = sum(self.validIdLst)
        print(f'The validated list is {self.validIdLst}')
        print(f'The running total is {self.runningTotal}')
        return self.validIdLst

class MultiRangeIDvalidatorModified(MultiRangeIDvalidator):
    
    def runReigon(self, reigonTuple: Tuple[int, int]):
        validator = SingleRangeIDValidatorModified(reigonTuple[0], reigonTuple[1], self.validIdLst)
        self.validIdLst = validator.runReigon()
        self.runningTotal = sum(self.validIdLst)
        print(self.validIdLst)
        
    
    

validator = SingleRangeIDValidatorModified(95, 115)     
validator.runReigon()   

# # multiValidator = MultiRangeIDvalidatorModified('./day_2_test.txt')
# # multiValidator.runAll()        
            
# multiValidator = MultiRangeIDvalidatorModified('./day_2_input.txt')
# multiValidator.runAll()  


      