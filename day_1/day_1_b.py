# -*- coding: utf-8 -*-
"""
Created on Tue Dec  2 03:12:51 2025

@author: Callum
"""

from day_1 import safeObject

#safe object, pointer, list, counter
class safeObjectModified(safeObject):
        
    def rotateUp(self, n_degrees: int):
        self.currentPos = self.currentPos + n_degrees
        self.checkMax()
        
    def rotateDown(self, n_degrees: int):
        self.currentPos = self.currentPos - n_degrees
        self.checkMin()
    
    def checkMax(self):
        if self.currentPos > self.maxPos:
            self.currentPos =  self.currentPos - (self.maxPos + 1)
            self.zeroCount = self.zeroCount + 1
            self.checkMax()
        
    def checkMin(self):
        if self.currentPos < self.minPos:
            self.currentPos = (self.maxPos + 1) + self.currentPos
            self.zeroCount = self.zeroCount + 1
            self.checkMin()
    
# testString = """L68
# L30
# R48
# L5
# R60
# L55
# L1
# L99
# R14
# L82"""

# elfSafe = safeObjectModified()
# elfSafe.summary()

# i = 0
# for l in testString.splitlines():
#     print(f"Line {i}")
#     print(l)
#     elfSafe.readLine(l)
#     elfSafe.summary()
#     i+=1
    
# elfSafe.get_pass()


# run
# ingest input
print("\n\n\nProper Run !")

with open('./day_one_insructions.txt') as f:
    fullRun = f.read()

elfSafe = safeObjectModified()
elfSafe.summary()

for l in fullRun.splitlines():
    elfSafe.readLine(l)

elfSafe.summary()
elfSafe.get_pass()


