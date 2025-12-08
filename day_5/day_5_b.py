# -*- coding: utf-8 -*-
"""
Created on Mon Dec  8 04:27:01 2025

@author: Callum
"""

from day_5 import RangeIngestor


class RangeIngestorModified(RangeIngestor):
    
    def sumfreshTuples(self):
        self.totalVal = 0
        for rTuple in self.freshTuples:
            sumTuples = len(range(rTuple[0], rTuple[1] + 1))
            self.totalVal += sumTuples
    

rI = RangeIngestorModified('day_5_input.txt')
rI.processFile()
rI.sortTuples()
rI.mergeRanges()
rI.sumfreshTuples()

print(rI.freshTuples)
print(rI.totalVal)