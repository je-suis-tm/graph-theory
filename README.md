# Graph Algorithms

1. Breath First Search

2. Depth First Search

3. Topological Sort

4. Dijkstra

5. Prim

6. A* Search

7. Bellman Ford

8. Ford Fulkerson

9. Kruskal

10. Nearest Neighbor

# Graph Problems

1. Maze

Walking out of a maze seems extremely complex in recursion algorithm. In graph theory, it is like a walk in the park. The only bit that takes some effort is building a data structure. Once we have graph ADT, we can use BFS/DFS/Dijkstra/A* to find the way out, although DFS may not be able to point out the shortest route out.

2. Broadcasting (Minimum Spanning Tree)

Consider a case where a postman is going to deliver mails to every house in the community. The distance between each house is completely different. The postman needs to deliver mails to each house with the least travel. Prim's algorithm is designed to solve this type of issue. The output of Prim's algorithm can be interpreted as a minimum spanning tree.

3. Shortest Path

4. Water Jug

5. Knight's Tour

6. Missionaries and Cannibals

7. Forex Arbitrage

8. Word Ladder

9. Text Mining

This is a self made BFS-like algorithm to travel through a graph structure built upon texts. The whole project is designed for MENA Newsfeed (https://github.com/tattooday/web-scraping/blob/master/MENA%20Newsfeed.py). The idea is to use graph structure to remove similar contents and extract key information from the texts. I highly recommend folks to take a peep at the project. Machine learning is absolutely not the best solution to text mining. Graph theory sometimes could be much more useful than expected. As usual, my own creation goes under a separate folder. The parent directory is for the self implementation of well-recognized algorithms. 

![alt text](https://github.com/tattooday/graph-theory/blob/master/Text%20Mining%20project/preview/result.png)

More details can be found at the following link.

https://github.com/tattooday/graph-theory/blob/master/Text%20Mining%20project/README.md

*Note that I mainly use Jupyter in this repo for the purpose of graph ADT visualization. However, ipynb takes longer to load compared to py files. That is why I also include a py version with graph ADT and all related algorithms for your reference.*
