# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 15:44:57 2018

@author: Administrator
"""
import numpy as np
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
    queue=[]
    queue.append(start)
    
    while queue:
        temp=queue.pop(0)
        df.visit(temp)
        print(df.route())
        for newpos in df.edge(temp):
            if df.go(newpos)==0 and newpos not in queue:
                queue.append(newpos)
                

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
        
        if temp==end:
            break
    return distance[end]


def astar(start,end,df):
    queue=[]
    distance={}
    heuristic={}
    route={}
    queue.append(start)

    for i in df.vertex():
        distance[i]=float('inf')
        heuristic[i]=np.abs(i[0]-end[0])+np.abs(i[1]-end[1])

    distance[start]=0 
    k=0    

    while queue:
        temp=queue.pop(0)
        minimum=float('inf')

        for j in df.edge(temp):
            distance[j]=distance[temp]+df.weight(temp,j)
            route[j]=distance[j]+heuristic[j]
            if route[j]<minimum:
                minimum=route[j]

        for j in df.edge(temp):
            if (route[j]==minimum) and (df.go(j)==0) and (j not in queue):
                queue.append(j)
                k+=1

        df.visit(temp)
        
        if temp==end:
                 break
    
    print('vertice travelled:',k)
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