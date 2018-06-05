# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 15:44:57 2018

@author: Administrator
"""

class graph:
        def __init__(self):
            self.graph={}
            self.visited={}
    
        def append(self,vertexid,edge,weight):
            if vertexid not in self.graph.keys():          
                self.graph[vertexid]={}
                self.visited[vertexid]=0
            self.graph[vertexid][edge]=weight
            
        def reveal(self):
            return self.graph
        
        def vertex(self):
            return list(self.graph.keys())
    
        def edge(self,vertexid):
            return list(self.graph[vertexid].keys())
        
        def weight(self,vertexid,edge):
            return (self.graph[vertexid][edge])
        
        def size(self):
            return len(self.graph)
        
        def visit(self,vertexid):
            self.visited[vertexid]=1
            
        def go(self,vertexid):
            return self.visited[vertexid]
        
        def route(self):
            return self.visited
        
        
def bfs(df,start):
    temp=[]
    temp.append(start)
    
    while temp:
        x=temp.pop(0)
        df.visit(x)
        print(df.route())
        for newpos in df.edge(x):
            if df.go(newpos)==0 and newpos not in temp:
                temp.append(newpos)
                

def dfs(df,start):
    df.visit(start)
    print(df.route())
    for newpos in df.edge(start):
        if df.go(newpos)==0:
            dfs(df,newpos)
            
            
def dijkstra(start,end,df):
    queue=[]
    distance={}
    queue.append(start)
    for i in df.vertex():
        distance[i]=float('inf')
    distance[start]=0    
        
    while queue:
        temp=queue.pop(0)
        
        for j in df.edge(temp):
            if distance[temp]+df.weight(temp,j)<distance[j]:
                distance[j]=distance[temp]+df.weight(temp,j)
            if df.go(j)==0 and j not in queue:
                queue.append(j)
            
        df.visit(temp)
    return distance[end]


def prim(df,start,end):
    queue={}
    queue[start]=0
    result=[]
    
    while queue:
        key=min(queue,key=queue.get)
        queue.pop(key)
        result.append(key)
        df.visit(key)
        print(df.route())
        if key==end:
            return result
        
        for i in df.edge(key):
            if i not in queue and df.go(i)==0:
                queue[i]=df.weight(key,i)
            if i in queue and queue[i]>df.weight(key,i):
                queue[i]=df.weight(key,i)
        
    return result