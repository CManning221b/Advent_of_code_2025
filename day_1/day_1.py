# -*- coding: utf-8 -*-
"""
Created on Tue Dec  2 02:19:59 2025

@author: Callum
"""

#safe object, pointer, list, counter
class safeObject:
    def __init__(self, currentPos: int = 50,  maxPos: int= 99, minPos: int = 0, upDir: str = 'R', downDir: str = 'L',  zeroCount: int = 0):
        self.currentPos = currentPos
        self.maxPos = maxPos
        self.minPos = minPos
        self.upDir = upDir
        self.downDir = downDir
        self.zeroCount = zeroCount
        
    def rotateUp(self, n_degrees: int):
        self.currentPos = self.currentPos + n_degrees
        self.checkMax()
        self.checkZero()
        
    def rotateDown(self, n_degrees: int):
        self.currentPos = self.currentPos - n_degrees
        self.checkMin()
        self.checkZero()
    
    def checkMax(self):
        if self.currentPos > self.maxPos:
            self.currentPos =  self.currentPos - (self.maxPos + 1)
            self.checkMax()
        
    def checkMin(self):
        if self.currentPos < self.minPos:
            self.currentPos = (self.maxPos + 1) + self.currentPos
            self.checkMin()
    
    def checkZero(self):
        if self.currentPos == self.minPos:
            self.zeroCount = self.zeroCount + 1
        
    def readLine(self, line: str):
        if self.upDir in line:
            if self.upDir == line[0]:
                n_degrees = int(line[1:])
                self.rotateUp(n_degrees)
            else: 
                print(f"Formatting error in line - {line}")
        elif self.downDir in line:
            if self.downDir == line[0]:
                n_degrees = int(line[1:])
                self.rotateDown(n_degrees)
            else: 
                print(f"Formatting error in line - {line}")
                
    def get_pass(self):
        print(f'The password is {self.zeroCount}')
    
    def summary(self):
        print(f"""The safe's current status is thus \n"""+ 
              f"""Its currently at {self.currentPos} \n"""+
              f"""The max position of the dial is {self.maxPos} \n"""+
              f"""The min position of the dial is {self.minPos} \n"""+
              f"""The direction to increase the dial is {self.upDir} \n"""+
              f"""The direction to decrease the dial is {self.downDir} \n"""+
              f"""The current zero count is {self.zeroCount} \n"""+
              f"""\n\n\n""")
            
testString = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""

elfSafe = safeObject()
elfSafe.summary()

i = 0
for l in testString.splitlines():
    print(f"Line {i}")
    print(l)
    elfSafe.readLine(l)
    elfSafe.summary()
    i+=1
    
elfSafe.get_pass()


#run
#ingest input
# print("\n\n\nProper Run !")

# with open('./day_one_insructions.txt') as f:
#     fullRun = f.read()

# elfSafe = safeObject()
# elfSafe.summary()

# for l in fullRun.splitlines():
#     elfSafe.readLine(l)

# elfSafe.summary()
# elfSafe.get_pass()


