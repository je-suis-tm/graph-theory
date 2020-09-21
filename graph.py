# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 15:44:57 2018

@author: Administrator
"""

import numpy as np
    
# In[1]:
#graph adt


class graph:
    
    """Graph ADT"""    
    def __init__(self):
        self.graph={}
        self.visited={}
    
    def append(self,vertexid,edge,weight):        
        """add/update new vertex,edge,weight"""        
        if vertexid not in self.graph.keys():      
            self.graph[vertexid]={}
            self.visited[vertexid]=0
        if edge not in self.graph.keys():      
            self.graph[edge]={}
            self.visited[edge]=0
        self.graph[vertexid][edge]=weight
        
    def reveal(self):
        """return adjacent list"""
        return self.graph
    
    def vertex(self):
        """return all vertices in the graph"""
        return list(self.graph.keys())
    
    def edge(self,vertexid):
        """return edge of a particular vertex"""
        return list(self.graph[vertexid].keys())
    
    def weight(self,vertexid,edge):
        """return weight of a particular vertex"""
        return (self.graph[vertexid][edge])
    
    def order(self):
        """return number of vertices"""
        return len(self.graph)
    
    def visit(self,vertexid):
        """visit a particular vertex"""
        self.visited[vertexid]=1
        
    def go(self,vertexid):
        """return the status of a particular vertex"""
        return self.visited[vertexid]
    
    def route(self):
        """return which vertices have been visited"""
        return self.visited
    
    def degree(self,vertexid):
        """return degree of a particular vertex"""
        return len(self.graph[vertexid])
    
    def mat(self):
        """return adjacent matrix"""        
        self.matrix=[]        
        for i in self.graph:    
            self.matrix.append([0 for _ in range(len(self.graph))])        
            for j in self.graph[i].keys():    
                self.matrix[i][j]=1        
        return self.matrix
    
    def remove(self,vertexid):  
        """remove a particular vertex and its underlying edges"""
        for i in self.graph[vertexid].keys():
            self.graph[i].pop(vertexid)
        self.graph.pop(vertexid)
      
        
# In[2]:     
#algorithms
        
        
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
def bellman_ford(df,start,end):
    
    distance={}
    pred={}

    for i in df.vertex():
        distance[i]=float('inf')
            
    distance[start]=0    
    
    for counter in range(1,len(df.vertex())-1):
        for i in df.vertex():
            for j in df.edge(i):
                try:
                    if distance[i]+df.weight(i,j)<distance[j]:
                        distance[j]=distance[i]+df.weight(i,j)
                        pred[j]=i
                
                except KeyError:
                    pass
    
    #
    for k in df.vertex():
        for l in df.edge(k):
            try:
                assert distance[k]+df.weight(k,l)>=distance[l],'negative cycle exists!'
            except KeyError:
                pass
    
    k=end
    path=[]
    while pred:
        path.insert(0,k)
        if k==start:
            break
        k=pred[k]
     
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
        heuristic[i]=abs(i[0]-end[0])+abs(i[1]-end[1])

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


#
def trace_root(disjointset,target):

    if disjointset[target]!=target:
        trace_root(disjointset,disjointset[target])
    else:
        return target


def kruskal(df):
    
    d={}
    output=[]
    
    for i in df.vertex():
        for j in df.edge(i):
            if f'{j}-{i}' not in d.keys():
                d[f'{i}-{j}']=df.weight(i,j)

    sort=sorted(d.items(), key=lambda x: x[1])
    
    disjointset={}
    
    for i in df.vertex():
        disjointset[i]=i
    
    for i in sort:
        
        parent=int(i[0].split('-')[0])
        child=int(i[0].split('-')[1])
        
        print(f'from {parent} to {child} at {df.weight(parent,child)}')
        
        if disjointset[parent]!=disjointset[child]:
            if trace_root(disjointset,parent)!=trace_root(disjointset,child):
                disjointset[child]=parent
                output.append([parent,child])                   
                
    return output


def boruvka(df):
    
    output=graph()
    
    for i in df.vertex():
        temp=999
        target=None
        for j in df.edge(i):
            if df.weight(i,j)<temp:
                temp=df.weight(i,j)
                target=[i,j]
        
        output.append(target[0],target[1],df.weight(target[0],target[1]))
        output.append(target[1],target[0],df.weight(target[0],target[1]))

    connected_components=[]
    for i in output.vertex():
        #use jump to break out of multiple loops
        jump=False
        for j in connected_components:
            if i in j:
                jump=True
                break
        if jump:
            continue
        connected_components.append(dfs_itr(output,i))
        
    print(connected_components)

    for i in range(len(connected_components)):
        for j in range(i+1,len(connected_components)):
            temp=999
            target=None
            for k in connected_components[i]:
                for l in df.edge(k):
                    if l in connected_components[j]:
                        if df.weight(k,l)<temp:
                            temp=df.weight(k,l)
                            target=[k,l]
            output.append(target[0],target[1],df.weight(k,l))
            output.append(target[1],target[0],df.weight(k,l))

    mst=[]
    for i in output.vertex():
        for j in output.edge(i):
            if [j,i] not in mst:
                mst.append([i,j])
                  
    return mst


# In[3]:
#random graph models


def create_bb_model(min_degree,num_of_v,etas):
    """create Bianconi-Barabási Model"""
    
    assert min_degree<=num_of_v,"minimum degree cannot be smaller than the order of a graph"
    assert len(etas)==num_of_v,"each vertex must have fitness"
    
    #create model
    bbmodel=graph()

    #create a fully connected graph for first comers
    for i in range(min_degree+1):
        for j in range(min_degree+1):
            if i!=j:
                bbmodel.append(i,j,1)

    #add new vertices
    for i in range(min_degree,num_of_v):

        #initialize counter and available vertices
        counter=0
        available=bbmodel.vertex()

        #each newcomer has to suffice the minimum degree
        while counter<min_degree: 

            #get degree of each vertex
            degree_dst=[bbmodel.degree(node) for node in available]

            #degree times eta
            #we obtain its fitness
            fitness=np.multiply(degree_dst,[etas[node] for node in available])
            fitness_prob=dict(zip(available,fitness/fitness.sum()))

            #select vertex based upon fitness
            selected=np.random.choice(available,p=list(fitness_prob.values()))

            #remove selected
            available.remove(selected)
            del fitness_prob[selected]

            #create an edge
            bbmodel.append(i,selected,1)
            bbmodel.append(selected,i,1)

            counter+=1
            
    return bbmodel