# coding: utf-8

# In[1]:

#this is a cross repo project for web scraping
#at first, the idea was to get as much info on MENA as possible
#so i scraped MENA region news from different websites
#somehow i realized, many news contents are similar
#you got idlib air strike, yemen war crime from reuters, al jazeera, bbc, cnn
#it is basically a waste of time and energy to read all these similar contents
#that is when i began to think about using different approaches to extract key information
#and graph structure is the best approach for this scenario
#in order to make this fully funtional, we have to make some assumptions
#the key news should be broadcasted on every major news website
#if it is important, every media should cover the topic
#and the title on this topic from different sources should somehow share some common words
#for instance, 'he goes to school on foot' from website alpha
#on website beta, the title is probably 'he walks to school'
#on website gamma, it could be 'he goes to school using his feet'
#therefore, if we build a graph network to connect all the titles together based on common words
#the key news must be strongly connected components with the most edges
#all we need to do is to use a traversal algorithm to get these nodes

#in terms of web scraping news content from different sources
#plz refer to the following link for more details
# https://github.com/tattooday/web-scraping/blob/master/MENA%20News%20Feeds.py

import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import re


# In[2]:


import os
os.chdir('h:/')


# In[3]:

#the selection of stopword is crucial
#for my particular problem, some location names should be included
#for instance, i could get a title 'minister in iran get arrested'
#and another title 'the economy in iran is slowing down'
#they would still be connected via common word iran
stopword=['i','we','our','my','me','you',           
          'your','to','ours','yours','him','his',           
          'he','her','hers','she','they','their',           
          'theirs','them','in','s','of','for',           
          'u', 'the', 'with', 'a', 'us', 'and',           
          'on', 'from','as', 'over', 'after',            
          'is', 'are', 'by','at','above','beyond',          
          'after','before','within','around','about',           
          'up','will','would','be','saudi','arabia',
          'yemen','yemeni','u','a','e','iran','iranian',
         'bahrain','qatar','syria','iraq','israel',
          'arabian','kuwait','lebanon','lebanonese',
         'jordan','turkey','oman','emirates','algeria',
         'morocco','moroccan','tunisia','tunisian',
         'algerian','back','syrian','russia','palestinian',
         'palestinians','iranians','russian','jerusalem',
         'israeli','pakistan']


# In[4]:

#using regex to convert a text into a list of words
def text2list(text,lower=False):
    
    temp=text if lower==False else text.lower()
    regex=re.findall('\w*',temp)
    output=list(filter(lambda x: x!='',regex))
    
    return output


# In[5]:

#find common words between two texts
#return the number of common words as the weight of the edge
def find_common(a,b,stopword):
    c=set(a+b)

    weight=0
    
    for i in c:
        if i not in stopword and a.count(i)!=0 and b.count(i)!=0:
            weight+=1

    return weight


# In[6]:

#building undirected weighted graph using networkx
#we cannot use title as the node name
#thus, we have to use dataframe index as the node name
#we only connect two nodes if they share common words excluded from stopword
#we set the number of common words as the weight
def build_graph(df,stopword):
    
    graph=nx.Graph()

    for i in range(len(df)):
        for j in range(i+1,len(df)):
            w=find_common(df['word'][i],df['word'][j],stopword)
            if w!=0:
                graph.add_edge(i,j,weight=w)
    
    return graph


# In[7]:

#plotting the graph structure
def plot_graph(graph,nodecolor,edgecolor,title=None):
    
    ax=plt.figure(figsize=(40,20)).add_subplot(111)
    labels = nx.get_edge_attributes(graph,'weight')
    pos=nx.spring_layout(graph,k=0.3)
    nx.draw_networkx(graph,pos,with_labels=True,edge_labels=labels,                     
                     node_size=1500,font_size=25,node_color=nodecolor, 
                    cmap=plt.get_cmap('autumn'),edge_color=edgecolor,
                     edge_cmap=plt.get_cmap('coolwarm'),width=2)
    
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    plt.xticks([])
    plt.yticks([])
    plt.title(title,fontsize=30)
    plt.show()



# In[8]:

#the traversal algo is kinda like bfs
#for each node in the graph defined as parent node
#we go to its child nodes and get the number of edges for each child node
#we compare the number of edges and only keep the node with the most edges
#we would keep the parent node if none of the child nodes have more edges than their parent
def alter_bfs(graph):
    
    #temp is a list to keep track of all the nodes
    #think of it as a waiting list
    #each time when we have traveled to a node
    #we do the following bfs
    #output is the list which keeps the nodes we need
    temp=list(graph.nodes)
    output=[]
          
    #this is sort of dynamic programming
    #we always keep the node with the largest number of edges
    #we initialize the current node as the parent node
    #and let child nodes to compete with it
    for i in temp:
    
        edge_num=len(graph.edges(i))
        node=i
    
        for j in graph.edges(i):
            
            #there are three cases
            #case 1 is just the number of edges of a new node is larger than the current node
            #we keep that new node
            if len(graph.edges(j[1]))>edge_num:
                edge_num=len(graph.edges(j[1]))
                node=j[1]
            
            #case 2 is when two nodes have the same number of edges
            #we would compare the sum of weights of their edges
            #as usual, we keep the largest
            #if we cannot get a winner from that
            #we simply use the rule first come first serve
            elif len(graph.edges(j[1]))==edge_num:
                weight1=sum([graph[k[0]][k[1]]['weight'] for k in graph.edges(i)])
                weight2=sum([graph[l[0]][l[1]]['weight'] for l in graph.edges(j[1])])
            
                if weight2>weight1:                
                    edge_num=len(graph.edges(j[1]))
                    node=j[1]
                    
            #case 3 is when the number of edges of a new node is smaller than the current node
            #nothing we need to do
            else:
                pass
            
        output.append(node)
    
    #there would be duplicates so we gotta remove them
    return list(set(output))


# In[9]:

#even for the output list
#we can still get similar contents
#for instance, we have node alpha
#node alpha has node beta and others
#node alpha has 4 edges and node beta only has 2 edges
#node beta has two edges, which connects node alpha and node gamma
#and node gamma only has one edge connected to node beta
#so when we use alter_bfs on node alpha and node beta, we only keep node alpha
#when we use alter_bfs on node gamma
#as node gamma is not connected to node alpha
#and node beta has more edges than node gamma
#we would also append node beta in the output list
#but node beta and node alpha have already gone through the travesal
#and we chose node alpha over node beta
#so in the output list we need another round of iteration to remove one of the connected nodes
#the idea is pretty much the same as alter_bfs
#there are 3 cases
def remove_child(output,graph):
    
    for i in output:
        for j in graph.edges(i):
            if j[1] in output:
                if len(graph.edges(j[1]))>len(graph.edges(i)):
                    try:
                        output.remove(i)
                    except ValueError:
                        pass
                    
                elif len(graph.edges(j[1]))==len(graph.edges(i)):
                    weight1=sum([graph[k[0]][k[1]]['weight'] for k in graph.edges(i)])
                    weight2=sum([graph[l[0]][l[1]]['weight'] for l in graph.edges(j[1])])
            
                    if weight1>weight2: 
                        try:
                            output.remove(j[1])
                        except ValueError:
                            pass
                    else:
                        try:
                            output.remove(i)
                        except ValueError:
                            pass
                        
                else:
                    try:
                        output.remove(j[1])
                    except ValueError:
                        pass
    
    return output


# In[10]:

#for some titles, they may not share any common words with others
#in another word, they are not included in the graph structure
#so we gotta add them back to the output list
#even though they are not key information broadcasted by every website
#they could be some niche information which is exclusive to one website
def add_non_connected(df,output,graph):
    
    for i in range(len(df)):
        if i not in list(graph.nodes):
            output.append(i)
    
    return output


# In[11]:

#this is just a function to add one more column in dataframe
#so the dataframe has a column which breaks texts into lists of words
def add_wordlist(df):
    
    temp=[]
    for i in df['title']:
        temp.append(text2list(i,lower=True))
    df['word']=temp
    
    return df


# In[12]:

#this is the ultimate function concat
#this would be the function we need when this script is called
#there are two possible plotting options
#plot the original and plot the highlighted results
def remove_similar(df,stopword,plot_original=False,plot_bfs=False,plot_result=False):
    
    df=add_wordlist(df)
    
    graph=build_graph(df,stopword)
    
    #edge color is depended on the weight of each edge
    edgecolor=[]
    for i in graph.edges:
        edgecolor.append(graph[i[0]][i[1]]['weight'])
    
    #no need for highlighted nodes if we only plot the original
    #hence, node color is the same for all nodes
    if plot_original==True:
        nodecolor=['#FFFF00' for i in graph.nodes]
        plot_graph(graph,nodecolor,edgecolor,title='original')
        
    output=alter_bfs(graph)
    
    #after our traversal, we would be able to get two types of nodes
    #so we highlight the selected nodes which is key information
    if plot_bfs==True:
        nodecolor=[]
        for i in graph.nodes:
            if i in output:
                nodecolor.append(1)
            else:
                nodecolor.append(2)
        plot_graph(graph,nodecolor,edgecolor,title='alternative bfs')
    
    output=remove_child(output,graph)    
    output=add_non_connected(df,output,graph)

    #clean up the output list and plot final results with highlights
    if plot_result==True:
        nodecolor=[]
        for i in graph.nodes:
            if i in output:
                nodecolor.append(1)
            else:
                nodecolor.append(2)
        plot_graph(graph,nodecolor,edgecolor,title='result')
    
    #return the selected nodes in a dataframe format
    data=df.loc[[i for i in output]]    
    data.reset_index(inplace=True,drop=True)
    
    del data['word']
    
    return data


# In[13]:


def main():
    
    df=pd.read_csv('mid east.csv',encoding='utf_8_sig')

    #this is how to use this script when called
    print(remove_similar(df,stopword,plot_original=True,plot_bfs=True,plot_result=True))


if __name__ == "__main__":
    main()
