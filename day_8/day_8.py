# -*- coding: utf-8 -*-
"""
Created on Wed Dec 17 17:38:43 2025

@author: Callum
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KDTree
from collections import Counter
import math
import matplotlib


# So take a bunch of points in 3D space
# Find each of their nearest neighbouts
# Connect them 
# Not a million miles away from k - nearest - neighbours
# I don't want to necessairly have to check every single node
# Not a million miles away from a collision problem
# A subgrid might be an idea - some set of trees. 
# Quick bit of googling says -> KD-Tree is the way to go, Union-Find?
# Squared distance is maybe the way to go
# Build Tree
# Collect Canidate edges
# Build subgraphs


class treeSearchSpace():
    def __init__(self, filePath: str, totalVal: int  = 0):
        self.filePath = filePath
        self.points = []
        self.tree = None
        self.unique_edges = set()
        self.distances = None
        self.indices = None
        self.parent = []
        
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j
            return True
        return False
    
    # 1. Get coords data
    def processFile(self):
        with open(self.filePath) as f:
            self.points = np.array([[int(x) for x in line.strip().split(',')] for line in f])
        self.parent = np.arange(len(self.points))
        
    
    # 2. Build KD-Tree
    def build_tree(self):
        self.tree = KDTree(self.points)
    
    # 3. Find unique edges    
    def find_unique_edges(self, n=None):
        all_edges = []
        for i in range(len(self.points)):
            for j in range(i + 1, len(self.points)):
                dist = np.linalg.norm(self.points[i] - self.points[j])
                all_edges.append((dist, i, j))
    
        all_edges.sort()
        if n is not None:
            all_edges = all_edges[:n]
        for dist, i, j in all_edges:
            edge = tuple(sorted((i, j)))
            self.unique_edges.add(edge)
        
    
    # 4. Group Edges 
    def group_edges(self):
        for edge in self.unique_edges:
            self.union(edge[0], edge[1])
        all_roots = [self.find(i) for i in range(len(self.points))]
        self.unique_classes = set(all_roots)
        print(f"I found {len(self.unique_classes)} distinct classifications!")
    
    # 5. Product top the 3 group values
    def product_top_3(self):
        all_roots = [self.find(i) for i in range(len(self.points))]
        counts = Counter(all_roots)
        group_sizes = sorted(counts.values(), reverse=True)
        top_3 = group_sizes[:3]
        result = math.prod(top_3)
        print(f"Top 3 group sizes: {top_3}")
        print(f"Product of top 3: {result}")
        return result
    
    def plot_kd_splits(self, ax, points, depth=0, bounds=[[0, 100], [0, 100], [0, 100]]):
        if len(points) <= 5:  
            return
    
        axis = depth % 3  # Cycles through X, Y, Z
        points = points[points[:, axis].argsort()]
        median_idx = len(points) // 2
        median_val = points[median_idx, axis]
    

        d1, d2 = (axis + 1) % 3, (axis + 2) % 3
        u = np.linspace(bounds[d1][0], bounds[d1][1], 2)
        v = np.linspace(bounds[d2][0], bounds[d2][1], 2)
        U, V = np.meshgrid(u, v)
        W = np.full_like(U, median_val)
    
        if axis == 0: ax.plot_surface(W, U, V, alpha=0.1, color='gray')
        elif axis == 1: ax.plot_surface(U, W, V, alpha=0.1, color='gray')
        else: ax.plot_surface(U, V, W, alpha=0.1, color='gray')
    
        left_bounds = [b[:] for b in bounds]
        left_bounds[axis][1] = median_val
        right_bounds = [b[:] for b in bounds]
        right_bounds[axis][0] = median_val
    
        if depth < 3: 
            self.plot_kd_splits(ax, points[:median_idx], depth + 1, left_bounds)
            self.plot_kd_splits(ax, points[median_idx:], depth + 1, right_bounds)
    
    # 6. Plot
    def plot_coord_space(self):
        # Get a color for each subgraph
        point_colors = [self.find(i) for i in range(len(self.points))]
        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(self.points[:, 0], self.points[:, 1], self.points[:, 2], 
                   c=point_colors, cmap='tab20', s=50)
        # Draw unique edges
        for edge in self.unique_edges:
            p1 = self.points[edge[0]]
            p2 = self.points[edge[1]]
            ax.plot([p1[0], p2[0]], [p1[1], p2[1]], [p1[2], p2[2]], c='orange', alpha=0.7)
        self.plot_kd_splits(ax, self.points)

        ax.set_title(f"Unique Nearest Neighbor Edges (Total: {len(self.unique_edges)})")
        plt.show()


ts = treeSearchSpace('./day_8_input.txt')
ts.processFile()
ts.build_tree()
ts.find_unique_edges(n=1000)
ts.group_edges()
ts.plot_coord_space()
ts.product_top_3()
print(f"Unique Nearest Neighbor Edges (Total: {len(ts.unique_edges)})")






