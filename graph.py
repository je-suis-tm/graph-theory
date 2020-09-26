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
        self.matrix=[[0 for _ in range(max(self.graph.keys())+1)] for i in range(max(self.graph.keys())+1)]        
        for i in self.graph:    
            for j in self.graph[i].keys():    
                self.matrix[i][j]=1        
        return self.matrix
    
    def remove(self,vertexid):  
        """remove a particular vertex and its underlying edges"""
        for i in self.graph[vertexid].keys():
            self.graph[i].pop(vertexid)
        self.graph.pop(vertexid)
        
    def disconnect(self,vertexid,edge):
        """remove a particular edge"""
        del self.graph[vertexid][edge]
    
    def clear(self,vertexid=None,whole=False):
        """unvisit a particular vertex"""
        if whole:
            self.visited=dict(zip(self.graph.keys(),[0 for i in range(len(self.graph))]))
        elif vertexid:
            self.visited[vertexid]=0
        else:
            assert False,"arguments must satisfy whole=True or vertexid=int number"
        
        
# In[2]:     
#algorithms
        
        
def bfs(ADT,current):
    """Breadth First Search"""
    
    #create a queue with rule of first-in-first-out
    queue=[]
    queue.append(current)
    
    while queue:
                
        #keep track of the visited vertices
        current=queue.pop(0)
        ADT.visit(current)
                
        for newpos in ADT.edge(current):
            
            #visit each vertex once
            if ADT.go(newpos)==0 and newpos not in queue:
                queue.append(newpos)


#
def dfs_itr(ADT,current):
    """Depth First Search without Recursion"""
    
    queue=[]
    queue.append(current)    
    
    #the loop is the backtracking part when it reaches cul-de-sac
    while queue:
        
        #keep track of the visited vertices
        current=queue.pop(0)
        ADT.visit(current)
        
        #priority queue
        smallq=[]        
        
        #find children and add to the priority
        for newpos in ADT.edge(current):
            if ADT.go(newpos)==0:
                
                #if the child vertex has already been in queue
                #move it to the frontline of queue
                if newpos in queue:
                    queue.remove(newpos)
                smallq.append(newpos)
                
        queue=smallq+queue


#
def dfs(ADT,current):
    """Depth First Search"""
    
    #keep track of the visited vertices
    ADT.visit(current)

    #the loop is the backtracking part when it reaches cul-de-sac
    for newpos in ADT.edge(current):
        
        #if the vertex hasnt been visited
        #we call dfs recursively
        if ADT.go(newpos)==0:
            dfs(ADT,newpos)


#            
def dijkstra(ADT,start,end):
    """Dijkstra's Algorithm"""
    
    #all weights in dcg must be positive 
    #otherwise we have to use bellman ford instead
    neg_check=[j for i in ADT.reveal() for j in ADT.reveal()[i].values()]
    assert min(neg_check)>=0,"negative weights are not allowed, please use Bellman-Ford"
    
    #queue is used to check the vertex with the minimum weight
    queue={}
    queue[start]=0
    
    #distance keeps track of distance from starting vertex to any vertex
    distance={}
    for i in ADT.vertex():
        distance[i]=float('inf')
    distance[start]=0
        
    #pred keeps track of how we get to the current vertex
    pred={}
        
    #dynamic programming
    while queue:
        
        #vertex with the minimum weight in queue
        current=min(queue,key=queue.get)
        queue.pop(current)
        
        for j in ADT.edge(current):
            
            #check if the current vertex can construct the optimal path
            if distance[current]+ADT.weight(current,j)<distance[j]:
                distance[j]=distance[current]+ADT.weight(current,j)
                pred[j]=current
            
            #add child vertex to the queue
            if ADT.go(j)==0 and j not in queue:
                queue[j]=distance[j]
        
        #each vertex is visited only once
        ADT.visit(current)
        
        #traversal ends when the target is met
        if current==end:
            break
    
    #create the shortest path by backtracking
    #trace the predecessor vertex from end to start
    previous=end
    path=[]
    while pred:
        path.insert(0, previous)
        if previous==start:
            break
        previous=pred[previous]
    
    #note that if we cant go from start to end
    #we may get inf for distance[end]
    #additionally, the path may not include start position
    return distance[end],path


#
def bellman_ford(ADT,start,end):
    """Bellman-Ford Algorithm,
    a modified Dijkstra's algorithm to detect negative cycle"""
    
    #distance keeps track of distance from starting vertex to any vertex
    distance={}
    for i in ADT.vertex():
        distance[i]=float('inf')            
    distance[start]=0  
    
    #pred keeps track of how we get to the current vertex
    pred={}
    
    #dynamic programming
    for _ in range(1,ADT.order()-1):
        for i in ADT.vertex():
            for j in ADT.edge(i):
                try:
                    if distance[i]+ADT.weight(i,j)<distance[j]:
                        distance[j]=distance[i]+ADT.weight(i,j)
                        pred[j]=i
                
                except KeyError:
                    pass
    
    #detect negative cycle
    for k in ADT.vertex():
        for l in ADT.edge(k):
            try:
                assert distance[k]+ADT.weight(k,l)>=distance[l],'negative cycle exists!'
            except KeyError:
                pass
    
    #create the shortest path by backtracking
    #trace the predecessor vertex from end to start
    previous=end
    path=[]
    while pred:
        path.insert(0, previous)
        if previous==start:
            break
        previous=pred[previous]
     
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


def create_ba_model(min_degree,num_of_v):
    """create Barabási-Albert Model"""
    
    assert min_degree<=num_of_v,"minimum degree cannot be smaller than the order of a graph"
    
    #create model
    bamodel=graph()

    #create a fully connected graph for first comers
    for i in range(min_degree+1):
        for j in range(min_degree+1):
            if i!=j:
                bamodel.append(i,j,1)

    #add new vertices
    for i in range(min_degree,num_of_v):

        #initialize counter and available vertices
        counter=0
        available=bamodel.vertex()

        #each newcomer has to suffice the minimum degree
        while counter<min_degree: 

            #get degree of each vertex
            degree_dst=[bamodel.degree(node) for node in available]   

            #compute the probability of attaching to one of the vertices
            prob=np.divide(degree_dst,sum(degree_dst))

            #select vertex based upon degree
            selected=np.random.choice(available,p=prob)

            #remove selected
            available.remove(selected)

            #create an edge
            bamodel.append(i,selected,1)
            bamodel.append(selected,i,1)

            counter+=1
            
    return bamodel


def create_er_model(num_of_v,prob):
    """create Erdős–Rényi Model"""
    
    ermodel=graph()

    #connect two vertices based upon probability
    for i in range(num_of_v):
        for j in range(i+1,num_of_v):
            if np.random.uniform()<prob:
                ermodel.append(i,j,1)
                ermodel.append(j,i,1)

    return ermodel


def create_ring_lattice(num_of_v,num_of_neighbors):
    """create ring lattice"""
    
    lattice=graph()

    assert num_of_neighbors%2==0,"number of neighbors must be even number"

    #connect neighbors
    for i in range(num_of_v):
        for j in range(1,num_of_neighbors//2+1):
            lattice.append(i,i+j if i+j<num_of_v else i+j-num_of_v,1)   
            lattice.append(i,i-j if i-j>=0 else i-j+num_of_v,1)
            lattice.append(i+j if i+j<num_of_v else i+j-num_of_v,i,1)   
            lattice.append(i-j if i-j>=0 else i-j+num_of_v,i,1)
            
    return lattice


def create_ws_model(num_of_v,num_of_neighbors,prob):
    """create Watts-Strogatz Model"""
    
    wsmodel=graph()

    assert num_of_neighbors%2==0,"number of neighbors must be even number"

    #first we create a regular ring lattice
    for i in range(num_of_v):
        for j in range(1,num_of_neighbors//2+1):
            wsmodel.append(i,i+j if i+j<num_of_v else i+j-num_of_v,1)   
            wsmodel.append(i,i-j if i-j>=0 else i-j+num_of_v,1)
            wsmodel.append(i+j if i+j<num_of_v else i+j-num_of_v,i,1)   
            wsmodel.append(i-j if i-j>=0 else i-j+num_of_v,i,1)

    #rewiring
    #remove a random edge and create a random edge
    for i in wsmodel.vertex():
        for j in wsmodel.edge(i):
            if np.random.uniform()<prob:
                wsmodel.disconnect(i,j)
                wsmodel.disconnect(j,i)
                rewired=np.random.choice(wsmodel.vertex())
                wsmodel.append(i,rewired,1)
                wsmodel.append(rewired,i,1)
                
    return wsmodel
