# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 15:44:57 2018

@author: Administrator
"""
import numpy as np

#
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
        
#        
def bfs(df,start,end):
    queue=[]
    queue.append(start)
    pred={}
    c=0
    
    while queue:
        temp=queue.pop(0)
        df.visit(temp)
        for newpos in df.edge(temp):
            if df.go(newpos)==0 and newpos not in queue:
                queue.append(newpos)
                pred[newpos]=temp
                
        
                
        if temp==end:
            break
        
        c+=1
        
    k=end
    path=[]
    while pred:
        path.insert(0,k)
        if k==start:
            break
        k=pred[k]
        
    return len(path)-1,path


#
def dfs_itr(df,start,end):
    queue=[]
    queue.append(start)
    pred={}
    c=0
    
    while queue:
        temp=queue.pop(0)
        smallq=[]
        df.visit(temp)
        for newpos in df.edge(temp):
            if df.go(newpos)==0:
                if newpos in queue:
                    queue.remove(newpos)
                smallq.append(newpos)
                pred[newpos]=temp
                
        queue=smallq+queue
        
        if temp==end:
            break
        
        c+=1
        
    k=end
    path=[]
    while pred:
        path.insert(0,k)
        if k==start:
            break
        k=pred[k]
        
    return len(path)-1,path


#
def dfs(df,start):
    df.visit(start)
    print(df.route())
    for newpos in df.edge(start):
        if df.go(newpos)==0:
            dfs(df,newpos)


#            
def dijkstra(df,start,end):
    queue={}
    distance={}
    queue[start]=0
    pred={}
    c=0

    for i in df.vertex():
        distance[i]=float('inf')
    distance[start]=0    
        
    while queue:
        temp=min(queue,key=queue.get)
        queue.pop(temp)
        for j in df.edge(temp):
            if distance[temp]+df.weight(temp,j)<distance[j]:
                distance[j]=distance[temp]+df.weight(temp,j)
                pred[j]=temp
                
            if df.go(j)==0 and j not in queue:
                queue[j]=distance[j]
            
            
        df.visit(temp)
        if temp==end:
            break
        
        c+=1
    
    k=end
    path=[]
    while pred:
        path.insert(0,k)
        if k==start:
            break
        k=pred[k]
     
    print('vertice travelled:',c)
    return distance[end],path


#
def astar(df,start,end):
    queue={}
    distance={}
    heuristic={}
    route={}
    queue[start]=0
    pred={}

    for i in df.vertex():
        distance[i]=float('inf')
        heuristic[i]=np.abs(i[0]-end[0])+np.abs(i[1]-end[1])

    distance[start]=0 
    c=0    

    while queue:
        temp=min(queue,key=queue.get)
        queue.pop(temp)
        minimum=float('inf')

        for j in df.edge(temp):
            distance[j]=distance[temp]+df.weight(temp,j)
            route[j]=distance[j]+heuristic[j]
            if route[j]<minimum:
                minimum=route[j]

        for j in df.edge(temp):
            if (route[j]==minimum) and (df.go(j)==0) and (j not in queue):
                queue[j]=route[j]
                pred[j]=temp
                
        df.visit(temp)
        
        if temp==end:
                 break
        
        c+=1
    
    k=end
    path=[]
    while pred:
        path.insert(0,k)
        if k==start:
            break
        k=pred[k]
        
    print('vertice travelled:',c)
    return distance[end],path


#
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