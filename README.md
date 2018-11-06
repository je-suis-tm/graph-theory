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

Walking out of a maze seems extremely complex in recursion algorithm. In graph theory, it is just a walk in the park. The only bit that takes some effort is building the data structure. Once we got graph ADT, we can use BFS/DFS/Dijkstra/A* to find the way out of the maze, although DFS may not be able to point out the shortest route out.

2. Broadcasting (Minimum Spanning Tree)

Consider a case where a postman is going to deliver mails to every house in the community. The distance between each house is completely different, some are shorter, some are longer. Ideally the postman should deliver mails to each house with the least travel. Prim's algorithm is designed to solve this type of broadcasting issue. And the topological output of Prim's algorithm can be interpreted as a minimum spanning tree.

3. Shortest Path

Whenever we look at the phrase, 'shortest path', we should naturally come up with Dijkstra's algorithm in our mind. This Dutchman came up with the revolutionary algorithm named after himself while searching for the shortest path to Rotterdam without pencil and paper. The algorithm is a special case of A* algorithm without heuristic function. It is also widely used as a subroutine for other traversal algorithms. Besides Dijkstra's algorithm, the shortest path problem, which could be thought as an optimization problem, can also be solved in dynamic programming.

4. Water Jug

Water jug is a simple but interesting problem. Assuming there are two jugs, a m-gallon and a n-gallon. And the target is to get x gallon water in either jug. There are many ways to solve this problem. Recursion can also solve water jug problem but it is very costly. Building a graph data structure would be a much easier way. The key is to set up edges based upon the rule of the game to connect all possible scenarios together. With BFS starts from the initial status, it can efficiently find the target status and return the route for us which would be the answer.

5. Knight's Tour

Knight's tour is a game where a knight travels all the squares on a k by k chessboard. And each square can only be travelled once. The solution can be obtained by DFS with a list that records whether each square on the chessboard has been visited. The rules of a knight's movement are very strange. The edges of the graph would indicate the valid move from one square to another.
 
6. Missionaries and Cannibals

7. Forex Arbitrage

8. Word Ladder

9. Text Mining

This is a self made BFS-like algorithm to travel through a graph structure built upon texts. The whole project is designed for MENA Newsfeed (https://github.com/tattooday/web-scraping/blob/master/MENA%20Newsfeed.py). The idea is to use graph structure to remove similar contents and extract key information from the texts. I highly recommend folks to take a peep at the project. Machine learning is absolutely not the best solution to text mining. Graph theory sometimes could be much more useful than expected. As usual, my own creation goes under a separate folder. The parent directory is for the self implementation of well-recognized algorithms. 

![alt text](https://github.com/tattooday/graph-theory/blob/master/Text%20Mining%20project/preview/result.png)

More details can be found at the following link.

https://github.com/tattooday/graph-theory/blob/master/Text%20Mining%20project/README.md

*Note that I mainly use Jupyter in this repo for the purpose of graph ADT visualization. However, ipynb takes longer to load compared to py files. That is why I also include a py version with graph ADT and all related algorithms for your reference.*
