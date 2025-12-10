# -*- coding: utf-8 -*-
"""
Created on Wed Dec 10 03:11:10 2025

@author: Callum
"""

import numpy as np
from typing import List, Tuple
from numpy.typing import NDArray
from scipy.signal import convolve2d
from pprint import pprint
from day_7 import manifold

# have to modify the beam traverser to now count paths 

class manifoldModified(manifold):    
    
    def transverseBeam(self):
        currentLine = np.zeros(self.lineLen)
        pathCounts = np.zeros(self.lineLen)
        
        indices = [i for i, x in enumerate(self.manifoldDesign[0]) if x == -1]
        self.beamDesign.append(currentLine.copy())
        for i in indices:
            currentLine[i] = 1
            pathCounts[i] = 1
        
        for splitterLine in self.manifoldDesign[1:]:
            newLine = currentLine.copy()
            newPathCounts = np.zeros(self.lineLen)
            
            currentLine = currentLine * (-splitterLine)
            indices = [i for i, x in enumerate(currentLine) if x < 0]
            
            for i in indices:
                newLine[i] = 0
                newLine[i-1] = 1
                newLine[i+1] = 1
                newPathCounts[i-1] += pathCounts[i]
                newPathCounts[i+1] += pathCounts[i]
                self.totalVal += 1
            
            for i in range(self.lineLen):
                if currentLine[i] == 0 and newLine[i] == 1:  
                    newPathCounts[i] += pathCounts[i]
            
            currentLine = newLine
            pathCounts = newPathCounts
            self.beamDesign.append(currentLine.copy())
        
        return int(np.sum(pathCounts))
    
    

        
    
m = manifoldModified('./day_7_input_tst.txt')
m.processFile()
print(f'path count is {m.transverseBeam()}')


