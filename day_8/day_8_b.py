# -*- coding: utf-8 -*-
"""
Created on Thu Dec 18 04:13:21 2025

@author: Callum
"""
import numpy as np
from day_8 import treeSearchSpace

class treeSearchSpaceModified(treeSearchSpace):
    
    def find_all_edges_until_complete(self):
        all_edges = []
        for i in range(len(self.points)):
            for j in range(i + 1, len(self.points)):
                dist = np.linalg.norm(self.points[i] - self.points[j])
                all_edges.append((dist, i, j))
        
        all_edges.sort()
        
        last_edge = None
        for dist, i, j in all_edges:
            if self.union(i, j):
                edge = tuple(sorted((i, j)))
                self.unique_edges.add(edge)
                last_edge = (i, j)
                
                root = self.find(0)
                if all(self.find(k) == root for k in range(len(self.points))):
                    break
        
        if last_edge:
            x_product = self.points[last_edge[0]][0] * self.points[last_edge[1]][0]
            print(f"Final connecting edge: {self.points[last_edge[0]]} and {self.points[last_edge[1]]}")
            print(f"Product of X coordinates: {x_product}")
            return x_product
        
ts = treeSearchSpaceModified('./day_8_input.txt')
ts.processFile()
ts.build_tree()
ts.find_all_edges_until_complete()
ts.group_edges()
ts.plot_coord_space()
ts.product_top_3()
print(f"Unique Nearest Neighbor Edges (Total: {len(ts.unique_edges)})")