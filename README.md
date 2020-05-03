# Graph Theory

&nbsp;

## Table of Contents

<a href=https://github.com/je-suis-tm/graph-theory#1-maze>1. Maze</a>

<a href=https://github.com/je-suis-tm/graph-theory#2-minimum-spanning-tree>2. Minimum Spanning Tree</a>

<a href=https://github.com/je-suis-tm/graph-theory#3-shortest-path>3. Shortest Path</a>

<a href=https://github.com/je-suis-tm/graph-theory#4-water-jug>4. Water Jug</a>

<a href=https://github.com/je-suis-tm/graph-theory#5-knights-tour>5. Knight's Tour</a>

<a href=https://github.com/je-suis-tm/graph-theory#6-missionaries-and-cannibals>6. Missionaries and Cannibals</a>

<a href=https://github.com/je-suis-tm/graph-theory#7-forex-arbitrage>7. Forex Arbitrage</a>

<a href=https://github.com/je-suis-tm/graph-theory#8-word-ladder>8. Word Ladder</a>

<a href=https://github.com/je-suis-tm/graph-theory#9-text-mining>9. Text Mining</a>

<a href=https://github.com/je-suis-tm/graph-theory#10-k-core>10. K Core</a>

<a href=https://github.com/je-suis-tm/graph-theory#11-maximal-clique>11. Maximal Clique</a>

<a href=https://github.com/je-suis-tm/graph-theory#12-epidemic-outbreak>12. Epidemic Outbreak</a>

<a href=https://github.com/je-suis-tm/graph-theory#13-portfolio-optimization>13. Portfolio Optimization</a>

&nbsp;

## Algorithms

<a href=https://github.com/je-suis-tm/graph-theory/blob/master/BFS%20DFS%20on%20DCG.ipynb>1. Breath First Search</a>

<a href=https://github.com/je-suis-tm/graph-theory/blob/master/BFS%20DFS%20on%20DCG.ipynb>2. Depth First Search</a>

<a href=https://github.com/je-suis-tm/graph-theory/blob/master/topological%20sort.ipynb>3. Topological Sort</a>

<a href=https://github.com/je-suis-tm/graph-theory/blob/master/dijkstra%20shortest%20path.ipynb>4. Dijkstra</a>

<a href=https://github.com/je-suis-tm/graph-theory/blob/master/minimum%20spanning%20tree.ipynb>5. Prim/Kruskal/Borůvka</a>

<a href=https://github.com/je-suis-tm/graph-theory/blob/master/a_star%20maze.ipynb>6. A* Search</a>

<a href=https://github.com/je-suis-tm/graph-theory/blob/master/bellman_ford%20forex%20arbitrage.ipynb>7. Bellman Ford</a>

<a href=https://github.com/je-suis-tm/graph-theory/blob/master/maximal%20clique.ipynb>8. Bron Kerbosch</a>

&nbsp;

## Graph Problems

### 1. Maze

Walking out of a maze seems extremely complex in recursion algorithm. In graph theory, it is just a walk in the park. The only bit that takes some effort is building the data structure. Once we got graph ADT, we can use BFS/DFS/Dijkstra/A* to find the way out of the maze, although DFS may not be able to point out the shortest route.

### 2. Minimum Spanning Tree

Consider a case where a postman is going to deliver mails to every house in the community. The distance between each house is completely different, some are shorter, some are longer. Ideally the postman wants to deliver mails to each house with the least travel distance and visit each house only once. There are a few algorithms to solve this type of issue. In this case, we choose Borůvka, Prim and Kruskal. And the topological output of these algorithms can be interpreted as a <a href=https://en.wikipedia.org/wiki/Minimum_spanning_tree>minimum spanning tree</a>. It is a subset of the edges of a connected, edge-weighted undirected graph that connects all the vertices together, without any cycles and with the minimum possible total edge weight.

### 3. Shortest Path

Whenever we look at the phrase, 'shortest path', we should naturally come up with Dijkstra's algorithm in our mind. This Dutchman came up with the revolutionary algorithm named after himself while searching for the shortest path to Rotterdam without pencil and paper. The algorithm is a special case of A* algorithm without heuristic function. It is also widely used as a subroutine for other traversal algorithms. Besides Dijkstra's algorithm, the shortest path problem, which could be thought as an optimization problem, can also be solved in dynamic programming.

### 4. Water Jug

Water jug is a simple and interesting problem. Assuming there are two jugs, a m-gallon and a n-gallon. And the target is to get x gallon water in either jug. There are many ways to solve this problem. Recursion can also solve water jug problem but it is very costly. Building a graph data structure would be a much easier way. The key is to set up edges based upon the rule of the game to connect all possible scenarios together. With BFS starts from the initial status, it can efficiently find the target status and return the route for us which would be the answer.

### 5. Knight's Tour

Knight's tour is a game where a knight travels all the squares on a k by k chessboard. And each square can only be travelled once. The solution can be obtained by DFS with a list that records whether each square on the chessboard has been visited. The rules of a knight's movement are very different from pawns or king. The edges of the graph should indicate the valid move from one square to another.
 
### 6. Missionaries and Cannibals

Missionaries and cannibals is a classic river problem. I actually prefer its alternative version called jealous husband. There are k missionaries and k cannibals. They need to cross a river. There is a boat with the capacity of only two people. There should be at least one person to sail the boat. These rules are subjected to one constraint. Cannibals cannot outnumber missionaries on both sides of the river. Again, the solution is similar to water jug problem. We have to set up edges based upon the rule of the game to connect all possible and valid scenarios together. As usual, BFS always return the optimized result rather than DFS.

### 7. Forex Arbitrage

Finding the shortest path on a map is not the only problem Dijkstra can apply to. Financial market is another application. As we all know, currency pairs have both bid and ask price. The market is weak-efficient. There is always opportunity for triangle arbitrage or rectangle arbitrage. We can exchange from currency A to currency B then to currency C if we can gain profit rather than directly exchanging currency A to currency C. We set each currency as the node, the rate from one currency to another as the edge. And the return from arbitrage would be the criteria for Dijkstra. However, Dijkstra cannot detect the negative return among currency pairs. There is an improved version called Bellman-Ford that can detect the negative cycle during the traversal.

### 8. Word Ladder

Word ladder problem is a game developed by the author of Alice in Wonderland. Given one word, we try to change it into another word. Each time we can only change one letter and it should also be a valid word. This is a great test for vocabulary. The difficult part of building a graph structure is to build edges. Connect one word to another with only one letter changed takes a bit of work. BFS is the perfect solution for this.

### 9. Text Mining

Is machine learning the best solution to text mining? What if graph theory beats it in both time and space complexity?

The whole project is designed for <a href=https://github.com/je-suis-tm/web-scraping/blob/master/MENA%20Newsletter.py>MENA Newsletter</a>. The idea is to use graph structure traversal algorithm to remove similar contents and extract key information from the metadata of text.

![alt text](https://github.com/je-suis-tm/graph-theory/blob/master/Text%20Mining%20project/preview/wordcloud.png)

For more details, please refer to the <a href=https://github.com/je-suis-tm/graph-theory/blob/master/Text%20Mining%20project/README.md>read me</a> page of a separate directory or <a href=https://je-suis-tm.github.io/graph-theory/text-mining>graph theory</a> section on my personal blog.

### 10. K Core

K core, also known as k degenerate, is a subset of the original graph in which all vertices have degree at least k. By some definition, k core is required to be a connected graph. The standard algorithm to find a k core graph is to remove all the vertices that have degree less than k. We must be careful that removing a vertex reduces the degree of all the vertices adjacent to it, hence the degree of adjacent vertices can also drop below k. And thus, we may have to remove those vertices as well.

### 11. Maximal Clique

A <a href=https://en.wikipedia.org/wiki/Clique_(graph_theory)>clique</a> is a subset of vertices of an undirected graph such that every two distinct vertices in the clique are adjacent. A maximal clique is a clique that cannot be extended by including one more adjacent vertex, meaning it is not a subset of a larger clique. Think of maximal clique as a maximum social group where everybody knows each other. Finding a maximal clique is an <a href=https://en.wikipedia.org/wiki/NP-completeness>NP-complete</a> problem. <a href=https://en.wikipedia.org/wiki/Bron–Kerbosch_algorithm>Bron–Kerbosch algorithm</a> with degeneracy ordering is the most efficient way to find out all maximal cliques. Its time complexity can be optimized to O(3**(n/3)).

### 12. Epidemic Outbreak

Amid the outbreak of the novel corona virus, we have observed a bonanza of agent-based simulation in epidemiology. By leveraging the probability generating function of a random graph, whether it is <a href=https://en.wikipedia.org/wiki/Barab%C3%A1si%E2%80%93Albert_model>Barabási-Albert model</a> following power-law distribution or <a href=https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93R%C3%A9nyi_model>Erdős–Rényi model</a> following Poisson distribution, we are able to consume the least computing power to estimate the prevalence and the duration of COVID-19.

![alt text](https://github.com/je-suis-tm/graph-theory/blob/master/Epidemic%20Outbreak%20project/preview/gillespie.gif)

For more details, please refer to the <a href=https://github.com/je-suis-tm/graph-theory/blob/master/Epidemic%20Outbreak%20project/README.md>read me</a> page of a separate directory or <a href=https://je-suis-tm.github.io/graph-theory/epidemic-outbreak>graph theory</a> section on my personal blog.

### 13. Portfolio Optimization

Modern portfolio theory was introduced in 1952 by Nobel laureate Harry Markowitz. It is part of investment class 101. But I watched a video by <a href=https://www.wolfram.com/training/videos/FIN015>Wolfram</a> recently. It challenged the traditional approach and introduced graph theory to asset diversification. There are plenty of quant shops deploying fancy mathematic tools to solve the market. The real question for us is, as fancy as it sounds, does graph theory work on portfolio optimization?

![alt text](https://github.com/je-suis-tm/graph-theory/blob/master/Portfolio%20Optimization%20project/preview/outta%20sample%20mean%20variance.png)

For more details, please refer to the <a href=https://github.com/je-suis-tm/graph-theory/blob/master/Portfolio%20Optimization%20project/README.md>read me</a> page of a separate directory or <a href=https://je-suis-tm.github.io/graph-theory/portfolio-optimization>graph theory</a> section on my personal blog.

&nbsp;

*For the purpose of the visualization of graph ADT, most scripts in this repository are Jupyter Notebook. Nevertheless, rendered ipynb files take longer time to load compared to py files. That is why I also include a py version with graph ADT and all related algorithms for your reference.*

