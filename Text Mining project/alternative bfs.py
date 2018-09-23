# coding: utf-8

# In[1]:

#this is a cross repo project for web scraping
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


def text2list(text,lower=False):
    
    temp=text if lower==False else text.lower()
    regex=re.findall('\w*',temp)
    output=list(filter(lambda x: x!='',regex))
    
    return output


# In[5]:


def find_common(a,b,stopword):
    c=set(a+b)

    weight=0
    
    for i in c:
        if i not in stopword and a.count(i)!=0 and b.count(i)!=0:
            weight+=1

    return weight


# In[6]:


def build_graph(df,stopword):
    
    graph=nx.Graph()

    for i in range(len(df)):
        for j in range(i+1,len(df)):
            w=find_common(df['word'][i],df['word'][j],stopword)
            if w!=0:
                graph.add_edge(i,j,weight=w)
    
    return graph


# In[7]:

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


def alter_bfs(graph):
    
    temp=list(graph.nodes)
    output=[]

    for i in temp:
    
        edge_num=len(graph.edges(i))
        node=i
    
        for j in graph.edges(i):
        
            if len(graph.edges(j[1]))>edge_num:
                edge_num=len(graph.edges(j[1]))
                node=j[1]
            
            elif len(graph.edges(j[1]))==edge_num:
                weight1=sum([graph[k[0]][k[1]]['weight'] for k in graph.edges(i)])
                weight2=sum([graph[l[0]][l[1]]['weight'] for l in graph.edges(j[1])])
            
                if weight2>weight1:                
                    edge_num=len(graph.edges(j[1]))
                    node=j[1]
            else:
            
                try:
                    temp.remove(j[1])
                except ValueError:
                    pass
            
        output.append(node)
    
    return list(set(output))


# In[9]:


def remove_child(output,graph):
    
    for i in output:
        for j in graph.edges(i):
            if j[1] in output:
                if len(graph.edges(j[1]))>len(graph.edges(i)):
                    output.remove(i)
                else:
                    output.remove(j[1])
    
    return output


# In[10]:


def add_non_connected(df,output,graph):
    
    for i in range(len(df)):
        if i not in list(graph.nodes):
            output.append(i)
    
    return output


# In[11]:


def add_wordlist(df):
    
    temp=[]
    for i in df['title']:
        temp.append(text2list(i,lower=True))
    df['word']=temp
    
    return df


# In[12]:


def remove_similar(df,stopword,plot_original=False,plot_result=False):
    
    df=add_wordlist(df)
    
    graph=build_graph(df,stopword)
    
    output=alter_bfs(graph)    
    output=remove_child(output,graph)    
    output=add_non_connected(df,output,graph)
    
    edgecolor=[]
    for i in graph.edges:
        edgecolor.append(graph[i[0]][i[1]]['weight'])
    
    if plot_original==True:
        nodecolor=['#FFFF00' for i in graph.nodes]
        plot_graph(graph,nodecolor,edgecolor,title='original')

    if plot_result==True:
        nodecolor=[]
        for i in graph.nodes:
            if i in output:
                nodecolor.append(1)
            else:
                nodecolor.append(2)
        plot_graph(graph,nodecolor,edgecolor,title='result')
    
    data=df.loc[[i for i in output]]    
    data.reset_index(inplace=True,drop=True)
    
    del data['word']
    
    return data


# In[13]:


def main():
    
    df=pd.read_csv('mid east.csv',encoding='utf_8_sig')

    print(remove_similar(df,stopword,plot_original=True,plot_result=True))


if __name__ == "__main__":
    main()
