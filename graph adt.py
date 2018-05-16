# -*- coding: utf-8 -*-
"""
Created on Wed May 16 19:03:13 2018

@author: Administrator
"""

class graph:
    def __init__(self):
        self.graph={}

    def append(self,vertexid,edge,weight):
        if vertexid not in self.graph.keys():          
            self.graph[vertexid]={}  
        self.graph[vertexid][edge]=weight
    
    def reveal(self):
        return self.graph
    
    def vertex(self):
        return self.graph.keys()

    def edge(self,vertexid):
        return self.graph[vertexid].keys()
    


        
        
a=graph()
a.append('1','2',12)
a.append('1','3',10)
a.append('2','3',15)
print(a.reveal())
print(a.vertex())
print(a.edge('2'))
