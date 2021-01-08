
# coding: utf-8

# In[1]:


#this is a cross repository project for web scraping
#at first, the idea was to get as much info on MENA region as possible
#the initial idea was to scrape news from various websites
#somehow i realized, many contents were similar
#reuters, al jazeera, bbc, cnn, they all covered the major news
#it was basically a waste of time and energy to read the similar content more than once
#that was when i began to think about using different approaches to extract key information
#and graph structure turned out to be the ideal approach for this scenario
#in order to make this script fully functional, some assumptions need to be made
#the major news should be headlined on every big news website
#if it is important enough, every media should cover the topic
#and the title for this topic from different sources should share some common words
#for instance, 'he goes to school on foot' from website alpha
#on website beta, the title is probably 'he walks to school'
#on website gamma, it could be 'he goes to school using his feet'
#therefore, if we build a graph network to connect all the titles together based on common words
#the major news must be the nodes with the highest degree in strongly connected components
#all we need to do is to use a traversal algorithm to get these nodes

#in terms of scraping news content from different online sources
#plz refer to the following link for more details
# https://github.com/je-suis-tm/web-scraping/blob/master/MENA%20Newsletter.py

#this file is a python script
#the demonstration of graph theory vs machine learning is in the following link
# https://github.com/je-suis-tm/graph-theory/blob/master/Text%20Mining%20project/text_mining.ipynb

import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
import os
os.chdir('k:/a')


# In[2]:


#the selection of stopword is crucial
#for our particular problem, some location names should be included
#for instance, we could get a title, 'minister in iran get arrested'
#and another title, 'the economy in iran is slowing down'
#they can be connected via common word iran
#yet, they share no similar content at all
stopword=stopwords.words('english')+['algeria',
 'algerian',
 'arabia',
 'arabian',
 'around',
 'b',
 'back',
 'bahrain',
 'beyond',
 'c',
 'e',
 'egyptian',
 'emirates',
 'f',
 'first',
 'g',
 'h',
 'iran',
 'iranian',
 'iranians',
 'iraq',
 'israel',
 'israeli',
 'j',
 'jerusalem',
 'jordan',
 'k',
 'kuwait',
 'l',
 'lebanon',
 'lebanonese',
 'moroccan',
 'morocco',
 'n',
 'oman',
 'p',
 'pakistan',
 'palestinian',
 'palestinians',
 'q',
 'qatar',
 'qatari',
 'r',
 'russia',
 'russian',
 'saudi',
 'syria',
 'syrian',
 'tunisia',
 'tunisian',
 'turkey',
 'turkish',
 'u',
 'us',
 'v',
 'w',
 'within',
 'would',
 'x',
 'yemen',
 'yemeni',
 'z']


# In[3]:


#convert text into a list of words
#we can use stemming and lemmatization to improve efficiency
#for instance, we have words walked,walking,walks
#with nltk package, we can revert all of them to walk
def text2list(text,stopword,lower=True,
              lemma=True,stemma=False):

    text_clean=text if lower==False else text.lower()
    
    #tokenize and remove stop words
    token=[i for i in nltk.tokenize.RegexpTokenizer(r'\w+').tokenize(text_clean) if i not in stopword]
    
    #lemmatization
    if lemma:
        text_processed=[nltk.stem.wordnet.WordNetLemmatizer().lemmatize(i) for i in token]
    else:
        text_processed=token
        
    #stemming
    if stemma:
        output=[nltk.stem.PorterStemmer().stem(i) for i in text_processed]
    else:
        output=text_processed
    
    #remove numbers as they are stopword as well
    for i in [ii for ii in output]:
        try:
            float(i)
            output.remove(i)
        except:
            pass
    
    return [i for i in output if i not in stopword]


# In[4]:


#find common words between two texts
#return the number of common words as the weight of the edge
def find_common(text1,text2,stopword):
    
    common=set(text1).intersection(set(text2)).difference(set(stopword))       

    return len(common)


# In[5]:


#this is just a function to add one more column in dataframe
#so the dataframe has a column which breaks texts into lists of words
def add_wordlist(df,stopword,**kwargs):
    
    temp=[]
    for i in df['title']:
        temp.append(text2list(i,stopword,lower=True,**kwargs))
    df['word']=temp
    
    return df


# &nbsp;
# ### Graph Theory
# &nbsp;

# In[6]:


#building undirected weighted graph using networkx
#we cannot use the original title as the node name
#it is simply too long for a node name
#thus, we have to use dataframe index as the node name
#we only connect two nodes if they share common words (exclude stopword)
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
def plot_graph(graph,position,nodecolor=[],nodesize=[],
               nodecmap=plt.cm.copper,title=None,colorbartitle=None,
               plot_colorbar=False,**kwargs):
    
    if not nodecolor:
        nodecolor=[0]*len(graph)
    if not nodesize:
        nodesize=300
    
    ax=plt.figure(figsize=(20,10)).add_subplot(111)
          
    nx.draw(graph,node_size=nodesize,pos=position,
            node_color=nodecolor,cmap=nodecmap,**kwargs)

    #remove axes
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)
          
    #plot colorbar for node color
    if plot_colorbar:
        sm=plt.cm.ScalarMappable(cmap=nodecmap,
                                 norm=plt.Normalize(vmin=min(nodecolor),
                                                    vmax=max(nodecolor)))
        sm._A=[]
        cb=plt.colorbar(sm,ticks=[min(nodecolor),max(nodecolor)])
        cb.ax.set_yticklabels(cb.ax.get_yticklabels(), fontsize=11)
        cb.ax.set_ylabel(colorbartitle,fontsize=11,rotation=270)
    
    plt.xticks([])
    plt.yticks([])
    plt.title(title,fontsize=15)
    plt.show()


# In[8]:


#for some titles, they may not share any common words with others
#in another word, they are not included in the graph structure
#we gotta add them back to the output list, cant leave the minority behind
#even though they are not key information published by every website
#they could still be some exclusive or niche information that has value to us
def add_non_connected(df,output,graph):
    
    for i in range(len(df)):
        if i not in list(graph.nodes):
            output.append(i)
    
    return output


# In[9]:


#graph traversal
def algo(graph):
    
    #dictionary of all nodes and degrees in graph
    D=dict(graph.degree)
    
    #order dict by each node's degree
    D=dict(sorted(D.items(),key=lambda x:x[1],reverse=False))

    queue=list(D.keys())
    result=[]
    
    #in each iteration, find the node with the highest agree in the queue
    #remove the node's neighbors in the queue until the queue is empty
    while queue:

        V=queue.pop()
        result.append(V)

        redundant=set(queue).intersection(set(graph.neighbors(V)))

        for i in redundant:
            queue.remove(i)
            
    return result


# In[10]:


#use graph theory to remove similar content
def remove_similar(df,stopword,plot_original=False,
                    plot_result=False,**kwargs):
    
    #tokenization
    df=add_wordlist(df,stopword,**kwargs)
    
    #graph building
    graph=build_graph(df,stopword,**kwargs)
    
    #fix node position for visual comparison
    pos=nx.spring_layout(graph,k=0.3)
        
    #plot original
    if plot_original:  
        plot_graph(graph,position=pos,
                   title='Original',**kwargs)
    
    #traversal
    result=algo(graph)

    #plot result, highlight the result
    if plot_result:        
        nodecolor=[]
        for i in graph.nodes:
            if i in result:
                nodecolor.append(1)
            else:
                nodecolor.append(0)
        
        nodesize=[]
        for i in graph.nodes:
            if i in result:
                nodesize.append(700)
            else:
                nodesize.append(300)
                
        plot_graph(graph,position=pos,nodecolor=nodecolor,
                   nodesize=nodesize,title='Graph Theory Result',**kwargs)
    
    #some of the exclusive or niche news content may share no common words with others at all
    #we still need the last puzzle to get the output
    output=add_non_connected(df,result,graph)
    
    #return the selected nodes in a dataframe format
    data=df.loc[[i for i in set(output)]]    
    data.reset_index(inplace=True,drop=True)    
    del data['word']

    return data


# In[11]:


def main():
    
    df=pd.read_csv('mid east.csv',encoding='latin-1')

    #the following line demonstrates how to use this script
    print(remove_similar(df,stopword,plot_original=True,plot_result=True))


if __name__ == "__main__":
    main()
