# coding: utf-8

# In[1]:

#this is a cross repo project for web scraping
#at first, the idea was to get as much info on MENA region as possible
#the initial idea was to scrape news from various websites
#somehow i realized, many contents were similar
#reuters, al jazeera, bbc, cnn, they all covered the major news
#it was basically a waste of time and energy to read the similar content more than once
#that was when i began to think about using different approaches to extract key information
#and graph structure turned out to be the best approach for this scenario
#in order to make this script fully functional, some assumptions need to be made
#the major news should be headlined on every big news website
#if it is important enough, every media should cover the topic
#and the title for this topic from different sources should share some common words
#for instance, 'he goes to school on foot' from website alpha
#on website beta, the title is probably 'he walks to school'
#on website gamma, it could be 'he goes to school using his feet'
#therefore, if we build a graph network to connect all the titles together based on common words
#the major news must be the nodes with the most edges in strongly connected components
#all we need to do is to use a traversal algorithm to get these nodes

#in terms of scraping news content from different online sources
#plz refer to the following link for more details
# https://github.com/je-suis-tm/web-scraping/blob/master/MENA%20Newsletter.py

import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import re
import copy
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer

# In[2]:


import os
os.chdir('h:/')


# In[3]:

#the selection of stopword is crucial
#for our particular problem, some location names should be included
#for instance, we could get a title, 'minister in iran get arrested'
#and another title, 'the economy in iran is slowing down'
#they can be connected via common word iran
#yet, they share no similar content at all
stopword=stopwords.words('english')+['i','we',
          'our','my','me','you', 'your','to',        
          'ours','yours','him','his', 'he',       
          'her','hers','she','they','their',           
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
         'israeli','pakistan','qatari','a','b','c','d','e',
          'f','g','h','i','j','k','l','m','n','o',
          'p','q','r','s','t','u','v','w','x','y',
          'z','not','first','egyptian','turkish','now']


# In[4]:

#tokenization, stemming and lemmatization
def text2list(text,stopword,lower=True):

    temp=text if lower==False else text.lower()
    tokenizer=RegexpTokenizer(r'\w+')
    temp2=[WordNetLemmatizer().lemmatize(i) for i in tokenizer.tokenize(temp)]
    output=[PorterStemmer().stem(i) for i in temp2 if i not in stopword]
    
    #remove numbers as they are stopword as well
    for i in output:
        try:
            float(i)
            output.remove(i)
        except:
            pass
    
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
#we cannot use the original title as the node name
#it is simply too long for a node name
#thus, we have to use dataframe index as the node name
#we only connect two nodes if they share common words (excluded from stopword)
#we set the number of common words as the weight of the edge
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
def plot_graph(graph,nodecolor,edgecolor,title=None,**kwargs):
    
    ax=plt.figure(figsize=(40,20)).add_subplot(111)
    labels = nx.get_edge_attributes(graph,'weight')
    pos=nx.spring_layout(graph,k=0.3)
          
    #if circular layout doesnt work
    #we would let networkx decides the layout
    #usually it is random and chaotic
    try:
        nx.draw_networkx(graph,pos,with_labels=True,edge_labels=labels,                     
                     node_size=1500,font_size=25,node_color=nodecolor, 
                    cmap=plt.get_cmap('autumn'),edge_color=edgecolor,
                     edge_cmap=plt.get_cmap('coolwarm'),width=2, 
                     pos=nx.circular_layout(graph),**kwargs)
        print('desired')
    except:
        nx.draw_networkx(graph,pos,with_labels=True,edge_labels=labels,                     
                     node_size=1500,font_size=25,node_color=nodecolor, 
                    cmap=plt.get_cmap('autumn'),edge_color=edgecolor,
                     edge_cmap=plt.get_cmap('coolwarm'),width=2,**kwargs)

    #remove axes
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)
          
    #plot colorbar for edge color which is just weight
    sm = plt.cm.ScalarMappable(cmap=plt.get_cmap('coolwarm'), 
                               norm=plt.Normalize(vmin=min(edgecolor), 
                                                  vmax=max(edgecolor)))
    sm._A = []
    cb=plt.colorbar(sm,ticks=[min(edgecolor),max(edgecolor)])
    cb.ax.set_yticklabels(cb.ax.get_yticklabels(), fontsize=22)
    cb.ax.set_ylabel('Edge Weight Colorbar',fontsize=22,rotation=270)
    
    plt.xticks([])
    plt.yticks([])
    plt.title(title,fontsize=30)
    plt.show()


# In[8]:

#the traversal algorithm is kinda like bfs
#that is why i call it alternative bfs
#one day when i become famous
#this algorithm will name after me, hehe

#for each node in the graph, we define that node as root node
#and only use its child nodes to construct a tree structure
#this tree structure would not include the node's grandchildren, siblings or parents
#so the tree structure is two-leveled
#level 0 is root node or call it parent node
#level 1 consists of different leaf nodes or call it child nodes
#all we need to is to find the node with most edges in a given tree structure
#and delete the rest of the nodes
def alter_bfs(graph):
    
    #temp is a list to keep track of all the nodes
    #think of it as a waiting list
    #output keeps the node with most edges in a given tree structure
    temp=list(graph.nodes)
    output=[]
    
    #we wanna find the node with most edges in a given tree structure
    #hence, we initialize the current node as the parent/root node
    #all its neighbors are defined as child/leaf nodes
    for i in temp:
    
        edge_num=len(graph.edges(i))
        node=i
    
        for j in graph.edges(i):
            
            #there are three cases
            #case 1 is when a new node has more edges than the current node
            #we keep the new node
            if len(graph.edges(j[1]))>edge_num:
                edge_num=len(graph.edges(j[1]))
                node=j[1]
            
            #case 2 is when two nodes have the same amount of edges
            #we have to compare the sum of weights of their edges
            #as usual, we keep the largest
            #if we cannot get a winner from that
            #we simply use the rule first come first serve
            #we keep the current node
            elif len(graph.edges(j[1]))==edge_num:
                weight1=sum([graph[k[0]][k[1]]['weight'] for k in graph.edges(i)])
                weight2=sum([graph[l[0]][l[1]]['weight'] for l in graph.edges(j[1])])
            
                if weight2>weight1:                
                    edge_num=len(graph.edges(j[1]))
                    node=j[1]
                    
            #case 3 is when the current node has more edges than a new node
            #nothing we need to do
            else:
                pass
            
        output.append(node)
    
    #there could be duplicates so we gotta remove them
    return list(set(output))


# In[9]:

#after alternative bfs
#we can still get similar contents
#for instance, we have node alpha
#node alpha connects to node beta and others
#node alpha has 4 edges and node beta only has 2 edges
#node beta has two edges, which connects to node alpha and node gamma
#and node gamma is a leaf node to node beta
#when we use alter_bfs to iterate the tree structure of node alpha and node beta
#both results are clearly node alpha
#when we use alter_bfs to iterate the tree structure of node gamma
#as node gamma is not connected to node alpha
#and node beta has more edges than node gamma
#we would append node beta in the output list
#but node beta and node alpha have already been through the travesal algo
#and previously we chose node alpha over node beta
#therefore, we need an algorithm to ensure each node in the given list is independent
#here, independent stands for not connceted to any other node in the given list
#the idea is pretty much the same as alter_bfs
#we use the given list to build a graph structure
#the selection criteria is still based on how many edges a node has
#there are 3 cases as well
#the only difference is the single child/leaf node scenario
def remove_child(output,graph,add_single_child=True):
    
    for i in copy.deepcopy(output):
        
        append_single_child=False
        
        for j in graph.edges(i):
            if j[1] in output:
                if len(graph.edges(j[1]))>len(graph.edges(i)):
                    if i in output:
                        output.remove(i)
                    
                elif len(graph.edges(j[1]))==len(graph.edges(i)):
                    weight1=sum(
                        [graph[k[0]][k[1]]['weight'] for k in graph.edges(i)])
                    weight2=sum(
                        [graph[l[0]][l[1]]['weight'] for l in graph.edges(j[1])])
            
                    if weight1>weight2: 
                        if j[1] in output:
                            output.remove(j[1])
                    else:
                        if i in output:
                            output.remove(i)
                        
                else:
                    if j[1] in output:
                        output.remove(j[1])
                    
            #this is the single child/leaf node scenario
            #i admit single child or the function name remove child sounds miserable
            #for each node we decide to kick out of the list
            #there should be no leaf node as the child node of the node we try to get rid of
            #if the ditched node has a child node with only one edge which connected back to the ditched node
            #we would include this child node as a compensation to kicking its parent node out of the list
            #the reason behind that is to make sure the single child is being taken care of
            #joking, actually it is to ensure some exclusive or niche news content will be in the output
            #and we can have a case where a ditched node has more than one leaf node as child nodes
            #we gotta apply first come first serve to multiple single child case
                    
            #in the following 3 lines
            #we simply keep track of the single child
            if len(graph.edges(j[1]))==1:
                append_single_child=True
                temp=j[1]
                
        #once the single child's parent node is abandoned
        #we adopt the single child as compensation
        if i not in output and \
        append_single_child==True and \
         add_single_child==True:
            output.append(temp)
    
    return output




# In[10]:

#for some titles, they may not share any common words with others
#in another word, they are not included in the graph structure
#so we gotta add them back to the output list
#even though they are not key information published by every website
#they could still be some exclusive or niche information that has value to us
def add_non_connected(df,output,graph):
    
    for i in range(len(df)):
        if i not in list(graph.nodes):
            output.append(i)
    
    return output


#this function is utilized to create a sub graph out of the main graph
#by connecting the nodes of alter_bfs result together
#to provide a cleaner version of visualization of alter_bfs result
def build_small_graph(input_list,original_graph):
    
    small_graph=nx.Graph()
    
    for i in input_list:
        for j in original_graph.edges(i):
            if j[1] in input_list:
                small_graph.add_edge(i,j[1],
                 weight=original_graph[i][j[1]]['weight'])
    
    
    return small_graph


# In[11]:

#this is just a function to add one more column in dataframe
#so the dataframe has a column which breaks texts into lists of words
def add_wordlist(df,stopword,**kwargs):
    
    temp=[]
    for i in df['title']:
        temp.append(text2list(i,stopword,lower=True,**kwargs))
    df['word']=temp
    
    return df


# In[12]:

#this is the ultimate function where everything happens in one place
#this gon be the function we need when this script is called
#there are several plotting options to help people understand what the algo is doing
#plot the original graph, plot the alter_bfs result in original graph
#plot the alter_bfs result in sub graph, plot the 1st remove_child result
#and plot the final result
def remove_similar(df,stopword,
                    plot_original=False,plot_bfs=False,
                    plot_temp_result=False,
                    plot_bfs_result=False,
                    plot_final_result=False,**kwargs):
    
    #tokenization
    df=add_wordlist(df,stopword,**kwargs)
    
    #graph building
    graph=build_graph(df,stopword)
    
    #edge color is dependent on the weight of each edge
    edgecolor=[]
    for i in graph.edges:
        edgecolor.append(graph[i[0]][i[1]]['weight'])
    
    #no need for highlighted nodes if we only plot the original
    #hence, node color is the same for all nodes
    if plot_original==True:
        nodecolor=['#FFFF00' for i in graph.nodes]
        plot_graph(graph,nodecolor,edgecolor,title='original')
        
    output=alter_bfs(graph)
    
    #plot the alter_bfs result in original graph
    #need to highlight the result in red
    if plot_bfs==True:
        nodecolor=[]
        for i in graph.nodes:
            if i in output:
                nodecolor.append(1)
            else:
                nodecolor.append(2)
        plot_graph(graph,nodecolor,
                   edgecolor,title='alternative bfs')
    
    #the first remove_child is to get VIP nodes
    #they are the major news content u cannot miss
    output2=remove_child(copy.deepcopy(output),
                         graph,**kwargs)
    
    #plot the first remove_child result
    if plot_temp_result==True:
        nodecolor=[]
        for i in graph.nodes:
            if i in output2:
                nodecolor.append(1)
            else:
                nodecolor.append(2)
        plot_graph(graph,nodecolor,
                   edgecolor,title='temporary result')
    
    #plot the alter_bfs result in a sub graph
    #only connect nodes inside the alter_bfs result
    if plot_bfs_result==True:
        small_graph=build_small_graph(output,graph)
        small_nodecolor=['r' for i in small_graph.nodes]
        
        small_edgecolor=[]
        for i in small_graph.edges:
            small_edgecolor.append(
                small_graph[i[0]][i[1]]['weight'])
        plot_graph(small_graph,small_nodecolor,
                   small_edgecolor,title='bfs result')
       
    #the second remove_child process is even more important
    #after the first remove_child, we end up with VIP nodes
    #we compare VIP nodes with the alter_bfs result
    #to eliminate any node in the alter_bfs result that connects to VIP nodes
    #for those which do not connect to VIP nodes but appear in the alter_bfs result
    #allow me to call those nodes lucky nodes
    #they are given a second chance to come back to the stage
    #plz note that these lucky nodes do not connect to VIP nodes
    #they may get eliminated by first phrase of remove_child
    #simply cuz they connect to the agent nodes that connect to VIP nodes
    #and agent nodes may have more edges than these lucky nodes
    #and VIP nodes have more edges than agent nodes
    #in short, the first phrase of remove_child drops lucky nodes then agent nodes
    #even though lucky nodes are given a second chance
    #lucky nodes can connect to each other without connecting to VIP nodes
    #a second phrase of remove_child is necessary to ensure only independent lucky nodes will survive
    excludelist=[j for i in output2 for j in graph.neighbors(i) if j in output]
    includelist=[i for i in output if i not in output2 and i not in excludelist]
    output2+=remove_child(copy.deepcopy(includelist),
                          graph,**kwargs)
    
    #some of the exclusive or niche news content may share no common words with others at all
    #we still need the last puzzle to get the output
    output3=add_non_connected(df,output2,graph)
    
    if plot_final_result==True:
        nodecolor=[]
        for i in graph.nodes:
            if i in output3:
                nodecolor.append(1)
            else:
                nodecolor.append(2)
        plot_graph(graph,nodecolor,
                   edgecolor,title='final result')
    
          
    #return the selected nodes in a dataframe format
    data=df.loc[[i for i in set(output3)]]    
    data.reset_index(inplace=True,drop=True)
    
    del data['word']
    
    return data


# In[13]:


def main():
    
    df=pd.read_csv('mid east.csv',encoding='latin-1')

    #the following line demonstrates how to use this script
    print(remove_similar(df,stopword,
                         plot_original=True,
                         plot_bfs=True,
                         plot_temp_result=True,
                         plot_bfs_result=True,
                         plot_final_result=True))


if __name__ == "__main__":
    main()
