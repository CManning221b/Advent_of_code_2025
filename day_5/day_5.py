# -*- coding: utf-8 -*-
"""
Created on Sun Dec  7 06:13:30 2025

@author: Callum
"""
# Looks like a fairly simple lookup 
# Some set of ranges, some set of values to check
# if they exist within said ranges. 
# Could probably just use range, a list and then check with 'in'

# Ok tried a loop but I'm basically brute forcing the thing here
# Need a revised version, maybe this is a tree problem !
# Organsiing branches and leaves of a tree. 

# Actually tree is only useful for dynamic input, static input probs just needs sorted ranges

# Class which generates list

# Simple loop which checks in and retrieves

class RangeIngestor():
    def __init__(self, filePath: str, totalVal: int  = 0):
        self.filePath = filePath
        self.totalVal = totalVal
        self.freshTuples = []
        self.availableList = []
        
    def processFile(self):
        availableSection = False
        with open(self.filePath) as f:
            for line in f:
                line = line.strip()
                if '-' in line:
                    rTuple = line.split('-')
                    self.freshTuples.append(tuple((int(rTuple[0]), int(rTuple[1]))))
                elif availableSection:
                    self.availableList.append(int(line))
                else:
                    availableSection = True
    
    def sortTuples(self):
        self.freshTuples = sorted(self.freshTuples, key = lambda x: x[0])
    
    def mergeRanges(self):
        mergedList = []
        currentTuple = self.freshTuples[0]
        for nextTuple in self.freshTuples[1:]:
            if nextTuple[0] <= currentTuple[1]:
                currentTuple = (currentTuple[0], max(currentTuple[1], nextTuple[1]))
            else:  
                mergedList.append(currentTuple)
                currentTuple = nextTuple
                
        mergedList.append(currentTuple)
        self.freshTuples = mergedList
            
    # Needs a ninary search of some sort
    def checkValue(self):
        for val in self.availableList:
            left, right = 0, len(self.freshTuples) - 1
            found = False
    
            while left <= right:
                mid = (left + right) // 2
                interval = self.freshTuples[mid]
                if interval[0] <= val <= interval[1]:
                    found = True
                    break
                elif val < interval[0]:
                    right = mid - 1
                else:  
                    left = mid + 1
            if found:
                self.totalVal += 1

rI = RangeIngestor('day_5_input.txt')
rI.processFile()
rI.sortTuples()
rI.mergeRanges()
rI.checkValue()

print(rI.freshTuples)
print(rI.availableList)
print(rI.totalVal)
  
                
