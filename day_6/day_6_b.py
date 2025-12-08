# -*- coding: utf-8 -*-
"""
Created on Mon Dec  8 05:11:04 2025

@author: Callum
"""

from day_6 import mathSolver

class mathSolverModified(mathSolver):
    
    def processFile(self):
        with open(self.filePath) as f:
            listCheck = False
            group = []
            for line in f:
                line = line.replace('\n', '')
                for idx, c in enumerate(line):
                    if not listCheck:
                        self.questionLists.append([c])
                    else: 
                        self.questionLists[idx].append(c)
                listCheck = True
        self.questionLists = self.questionLists[::-1]
            
    def groupNumbers(self):
        group = []
        newQuestionList = []
        current_number = ""
        for l in self.questionLists:
            for char in l: 
                if char != ' ':
                    if char in ['+', '*']:
                        if current_number:
                            group.append(int(current_number))
                            current_number = ""
                        group.append(char)
                        newQuestionList.append(group)
                        group = []
                    else:
                        current_number += char
                else:
                    if current_number:
                        group.append(int(current_number))
                        current_number = ""
            if current_number:
                group.append(int(current_number))
                current_number = ""
        
        self.questionLists = newQuestionList
            
                    

mS = mathSolverModified('./day_6_input.txt')
mS.processFile()
mS.groupNumbers()
mS.runEquation()

print(mS.questionLists)
print(mS.totalVal)
            