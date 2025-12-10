# -*- coding: utf-8 -*-
"""
Created on Tue Dec  9 23:43:29 2025

@author: Callum
"""

import numpy as np
from typing import List, Tuple
from numpy.typing import NDArray
from scipy.signal import convolve2d
from pprint import pprint

# For each line in the the array
# Each line we need an array of tachyon beams 
# will need to identify position of any splitters in the line
# will need to replace any beam at a splitter with two either side


class manifold():
    def __init__(self, filePath: str, totalVal: int  = 0):
        self.filePath = filePath
        self.manifoldDesign = []
        self.totalVal = totalVal
        self.beamDesign = []
        self.lineLen = 0
    
    def processFile(self):
        with open(self.filePath) as f:
            for line in f:
                line = line.strip()
                self.lineLen = len(line)
                lineArr = np.zeros(self.lineLen)
                indices = [i for i, x in enumerate(line) if x == "^"]
                for i in indices:
                    lineArr[i] = 1
                indices = [i for i, x in enumerate(line) if x == "S"]
                for i in indices:
                        lineArr[i] = -1
                self.manifoldDesign.append(lineArr)
                
    def transverseBeam(self):
        currentLine = np.zeros(self.lineLen)
        indices = [i for i, x in enumerate(self.manifoldDesign[0]) if x == -1]
        self.beamDesign.append(currentLine)
        for i in indices:
            currentLine[i] = 1
        for splitterLine in self.manifoldDesign[1:]:
            newLine = currentLine.copy()
            currentLine = currentLine * (-splitterLine)
            indices = [i for i, x in enumerate(currentLine) if x < 0]
            for i in indices:
                newLine[i] = 0
                newLine[i-1] = 1
                newLine[i+1] = 1
                self.totalVal += 1
            currentLine = newLine
            self.beamDesign.append(currentLine.copy())
    

    def writeToBeam(self, fileWritePath: str = '', beam=True, design=True):
        fileStr = ""
        
        if beam and design:
            specFile = (2 * np.array(self.manifoldDesign)) + np.array(self.beamDesign)
        elif design:
            specFile = 2 * np.array(self.manifoldDesign)
        else:
            specFile = np.array(self.beamDesign)
        
        for idx, line in enumerate(specFile):
            fileLine = ""
            for char in line:
                if char == 0:
                    fileLine += '.'
                elif char == 1:
                    fileLine += '|'
                elif char == 2:
                    fileLine += '^'
                else:
                    fileLine += 'S'
            fileLine += '\n'
            fileStr += fileLine
        
        with open(fileWritePath, 'w+') as f:
            f.write(fileStr)
            
    
            
            

# m = manifold('./day_7_input_tst.txt')

# m.processFile()
# m.transverseBeam()


# m.writeToBeam('./output_beam_only.txt', beam=True, design=False)      # Just beams
# m.writeToBeam('./output_design_only.txt', beam=False, design=True)    # Just manifold
# m.writeToBeam('./output_combined.txt', beam=True, design=True)        # Both overlaid


# pprint(m.manifoldDesign)
# print('\n\n\n')
# pprint(m.beamDesign)
# pprint(m.totalVal)
    