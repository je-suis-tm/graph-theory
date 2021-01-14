# Graph Theory

&nbsp;

## Intro

Graph theory, sometimes we call it complex network or network science or network analysis, is one of the most avant-garde research areas in discrete mathematics, also one of my favorite subjects. Here, “graph” is the preferred name, because too many people associate the word “network” with internet. Given the bonanza of data science, graph theory is constantly overshadowed by the hype of machine learning. Yet some of the top-notch technology companies such as Google and Facebook heavily rely on the research of graph theory. 

This repository intends to increase the exposure of graph theory to all my readers. It contains common graph algorithms, popular network models, interesting agent-based simulations and amazing complex systems. The codes range from the level of elementary to sophisticated with wide applications in ecology, epidemiology, sociology, economics, finance, etc. Both Julia and Python are used to construct different scripts. As I am slowly climbing up the learning curve, more and more fascinating content will emerge en masse. Stay tuned!

&nbsp;

## Table of Contents

### Algorithms

* <a href=https://github.com/je-suis-tm/graph-theory/blob/master/a_star%20maze.ipynb>A* Search</a> 

* <a href=https://github.com/je-suis-tm/graph-theory/blob/master/k%20core.ipynb>Batagelj Zaveršnik</a> 

* <a href=https://github.com/je-suis-tm/graph-theory/blob/master/bellman_ford%20forex%20arbitrage.ipynb>Bellman Ford</a> 

* <a href=https://github.com/je-suis-tm/graph-theory/blob/master/BFS%20DFS%20on%20DCG.ipynb>BiDirectional BFS</a> 

* <a href=https://github.com/je-suis-tm/graph-theory/blob/master/minimum%20spanning%20tree.ipynb>Borůvka</a> 

* <a href=https://github.com/je-suis-tm/graph-theory/blob/master/BFS%20DFS%20on%20DCG.ipynb>Breadth First Search</a> 

* <a href=https://github.com/je-suis-tm/graph-theory/blob/master/maximal%20clique.ipynb>Bron Kerbosch</a> 

* <a href=https://github.com/je-suis-tm/graph-theory/blob/master/BFS%20DFS%20on%20DCG.ipynb>Depth First Search</a> 

* <a href=https://github.com/je-suis-tm/graph-theory/blob/master/dijkstra%20shortest%20path.ipynb>Dijkstra</a> 

* <a href=https://github.com/je-suis-tm/graph-theory/blob/master/habitat%20competition.ipynb>Gillespie</a> 

* <a href=https://github.com/je-suis-tm/graph-theory/blob/master/topological%20sort.ipynb>Kahn</a> 

* <a href=https://github.com/je-suis-tm/graph-theory/blob/master/minimum%20spanning%20tree.ipynb>Kruskal</a> 

* <a href=https://github.com/je-suis-tm/graph-theory/blob/master/k%20core.ipynb>Matula Beck</a> 

* <a href=https://github.com/je-suis-tm/graph-theory/blob/master/minimum%20spanning%20tree.ipynb>Prim</a> 

&nbsp;

### Applications

* <a href=https://github.com/je-suis-tm/graph-theory#12-epidemic-outbreak>Epidemic Outbreak</a> 

* <a href=https://github.com/je-suis-tm/graph-theory#7-forex-arbitrage>Forex Arbitrage</a> 

* <a href=https://github.com/je-suis-tm/graph-theory#15-habitat-competition>Habitat Competition</a> 

* <a href=https://github.com/je-suis-tm/graph-theory#14-habitat-occupancy>Habitat Occupancy</a> 

* <a href=https://github.com/je-suis-tm/graph-theory#10-k-core>K Core</a> 

* <a href=https://github.com/je-suis-tm/graph-theory#5-knights-tour>Knight's Tour</a> 

* <a href=https://github.com/je-suis-tm/graph-theory#11-maximal-clique>Maximal Clique</a> 

* <a href=https://github.com/je-suis-tm/graph-theory#1-maze>Maze</a> 

* <a href=https://github.com/je-suis-tm/graph-theory#2-minimum-spanning-tree>Minimum Spanning Tree</a> 

* <a href=https://github.com/je-suis-tm/graph-theory#6-missionaries-and-cannibals>Missionaries and Cannibals</a> 

* <a href=https://github.com/je-suis-tm/graph-theory#13-portfolio-optimization>Portfolio Optimization</a> 

* <a href=https://github.com/je-suis-tm/graph-theory#3-shortest-path>Shortest Path</a> 

* <a href=https://github.com/je-suis-tm/graph-theory#9-text-mining>Text Mining</a> 

* <a href=https://github.com/je-suis-tm/graph-theory#4-water-jug>Water Jug</a> 

* <a href=https://github.com/je-suis-tm/graph-theory#8-word-ladder>Word Ladder</a> 

&nbsp;

### Models

* <a href=https://github.com/je-suis-tm/graph-theory/blob/master/barabasi%20albert%20model.ipynb>Barabási-Albert</a>

* <a href=https://github.com/je-suis-tm/graph-theory/blob/master/bianconi%20barabasi%20model.ipynb>Bianconi-Barabási</a>

* <a href=https://github.com/je-suis-tm/graph-theory/blob/master/watts%20strogatz%20model.ipynb>Erdős–Rényi</a>

* <a href=https://github.com/je-suis-tm/graph-theory/blob/master/watts%20strogatz%20model.ipynb>Watts-Strogatz</a>

* <a href=https://github.com/je-suis-tm/graph-theory/blob/master/habitat%20occupancy.ipynb>Levins</a>

* <a href=https://github.com/je-suis-tm/graph-theory/blob/master/habitat%20competition.ipynb>Schelling’s</a>

* <a href=https://github.com/je-suis-tm/graph-theory/blob/master/habitat%20competition.ipynb>Tilman</a>

&nbsp;

## Applications

### 1. Maze

Walking out of a maze seems extremely complex in recursion algorithm. In graph theory, it is just a walk in the park. The only bit that takes some effort is building the data structure. Once we got graph ADT, we can use BFS/DFS/Dijkstra/A* to find the way out of the maze, although DFS may not be able to point out the shortest route.

*Click <a href=https://github.com/je-suis-tm/graph-theory/blob/master/a_star%20maze.ipynb>here</a> to be redirected to the script.*

![alt text](https://github.com/je-suis-tm/graph-theory/blob/master/preview/a_star.png)

### 2. Minimum Spanning Tree

Imagine a telecommunications company Orange tries to create a cable network connecting every family in Côte d’Azur. There are possibly millions of different routes to build such a network. Yet, the company only wants to satisfy every customer with the minimum cost. This creates a typical minimum spanning tree problem. Minimum spanning tree is a subset of a graph to connect all vertices without any cycle to achieve the minimum total weight. In this chapter, we will demonstrate how Borůvka’s algorithm, Kruskal’s algorithm and Prim’s algorithm obtain such a topological output. 

*Click <a href=https://github.com/je-suis-tm/graph-theory/blob/master/minimum%20spanning%20tree.ipynb>here</a> to be redirected to the script.*

![alt text](https://github.com/je-suis-tm/graph-theory/blob/master/preview/minimum%20spanning%20tree%20subset.jpg)

### 3. Shortest Path

Whenever we hear the phrase 'shortest path', we should instinctively shout out Dijkstra's algorithm in our mind. This Dutchman came up with the revolutionary algorithm named after himself while searching for the shortest path to Rotterdam without pencil and paper. The algorithm is a special case of A* algorithm without heuristic function. It is also widely used as a subroutine for other traversal algorithms, such as Bellman-Ford. Apart from Dijkstra, the shortest path problem, which could be thought as an optimization problem, can also be solved in <a href=https://github.com/je-suis-tm/recursion-and-dynamic-programming>dynamic programming</a>.

*Click <a href=https://github.com/je-suis-tm/graph-theory/blob/master/dijkstra%20shortest%20path.ipynb>here</a> to be redirected to the script.*

![alt text](https://github.com/je-suis-tm/graph-theory/blob/master/preview/dijkstra.jpg)

### 4. Water Jug

Water jug is a simple and interesting problem. Assuming there are two jugs, a m-gallon and a n-gallon. And the target is to get x gallon water in either jug. There are many ways to solve this problem. Recursion can also solve water jug problem but it is very costly. Building a graph data structure would be a much easier way. The key is to set up edges based upon the rule of the game to connect all possible scenarios together. With BFS starts from the initial status, it can efficiently find the target status and return the route for us which would be the answer.

*Click <a href=https://github.com/je-suis-tm/graph-theory/blob/master/water%20jug%20problem.ipynb>here</a> to be redirected to the script.*

![alt text](https://github.com/je-suis-tm/graph-theory/blob/master/preview/water%20jug.gif)

### 5. Knight's Tour

Knight's tour is a game where a knight travels all the squares on a k by k chessboard. And each square can only be travelled once. The solution can be obtained by DFS with a list that records whether each square on the chessboard has been visited. The rules of a knight's movement are very different from pawns or king. The edges of the graph should indicate the valid move from one square to another.
 
*Click <a href=https://github.com/je-suis-tm/graph-theory/blob/master/knights%20tour.ipynb>here</a> to be redirected to the script.*

![alt text](https://github.com/je-suis-tm/graph-theory/blob/master/preview/knights%20tour.gif)

### 6. Missionaries and Cannibals

Missionaries and cannibals is a classic river problem. I actually prefer its alternative version called jealous husband. There are k missionaries and k cannibals. They need to cross a river. There is a boat with the capacity of only two people. There should be at least one person to sail the boat. These rules are subjected to one constraint. Cannibals cannot outnumber missionaries on both sides of the river. Again, the solution is similar to water jug problem. We have to set up edges based upon the rule of the game to connect all possible and valid scenarios together. As usual, BFS always return the optimized result rather than DFS.

*Click <a href=https://github.com/je-suis-tm/graph-theory/blob/master/missionaries%20and%20cannibals%20problems.ipynb>here</a> to be redirected to the script.*

![alt text](https://github.com/je-suis-tm/graph-theory/blob/master/preview/missionaries%20and%20cannibals.gif)

### 7. Forex Arbitrage

Finding the shortest path on a map is not the only problem Dijkstra can solve. Financial market is another application. As we all know, currency pairs have both bid and ask price. The market is weak-efficient. There could be an opportunity for triangle arbitrage or rectangle arbitrage. We can exchange from currency A to currency B then to currency C if we can churn out more profit rather than directly exchanging currency A to currency C. We set each currency as the vertex and the exchange rate from one currency to another as the weight of the edge. The arbitrage with some logarithm transformation would be the criteria for Dijkstra. However, Dijkstra cannot properly handle a graph structure with negative weights. We will introduce an improved version called Bellman-Ford which is able to detect the negative cycle during the traversal.

*Click <a href=https://github.com/je-suis-tm/graph-theory/blob/master/bellman_ford%20forex%20arbitrage.ipynb>here</a> to be redirected to the script.*

![alt text](https://github.com/je-suis-tm/graph-theory/blob/master/preview/arbitrage.png)

### 8. Word Ladder

Word ladder problem is a game developed by the author of Alice in Wonderland. Given one word, we try to change it into another word. Each time we can only change one letter and it should also be a valid word. This is a great test for vocabulary. The difficult part of building a graph structure is to build edges. Connect one word to another with only one letter changed takes a bit of work. BFS is the perfect solution for this.

*Click <a href=https://github.com/je-suis-tm/graph-theory/blob/master/word%20ladder.ipynb>here</a> to be redirected to the script.*

![alt text](https://github.com/je-suis-tm/graph-theory/blob/master/preview/word%20ladder.png)

### 9. Text Mining

Is machine learning the best solution to text mining? What if graph theory beats it in both time and space complexity?

The whole project is designed for <a href=https://github.com/je-suis-tm/web-scraping/blob/master/MENA%20Newsletter.py>MENA Newsletter</a>. The idea is to use graph structure traversal algorithm to remove similar contents and extract key information from the metadata of text.

*For more details, please refer to the <a href=https://github.com/je-suis-tm/graph-theory/blob/master/Text%20Mining%20project/README.md>read me</a> page of a separate directory or <a href=https://je-suis-tm.github.io/graph-theory/text-mining>graph theory</a> section on my personal blog.*

![alt text](https://github.com/je-suis-tm/graph-theory/blob/master/Text%20Mining%20project/preview/wordcloud.png)

### 10. K Core

K core, also known as k degenerate, is a subset of the original graph in which all vertices have degree at least k. By some definition, k core is required to be a connected graph. The standard algorithm to find a k core graph is to remove all the vertices that have degree less than k. We must be careful that removing a vertex reduces the degree of all the vertices adjacent to it, hence the degree of adjacent vertices can also drop below k. And thus, we may have to remove those vertices as well.

*Click <a href=https://github.com/je-suis-tm/graph-theory/blob/master/k%20core.ipynb>here</a> to be redirected to the script.*

![alt text](https://github.com/je-suis-tm/graph-theory/blob/master/preview/kcore.png)

### 11. Maximal Clique

A <a href=https://en.wikipedia.org/wiki/Clique_(graph_theory)>clique</a> is a subset of vertices of an undirected graph such that every two distinct vertices in the clique are adjacent. A maximal clique is a clique that cannot be extended by including one more adjacent vertex, meaning it is not a subset of a larger clique. Think of maximal clique as a maximum social group where everybody knows each other. Finding a maximal clique is an <a href=https://en.wikipedia.org/wiki/NP-completeness>NP-complete</a> problem. <a href=https://en.wikipedia.org/wiki/Bron–Kerbosch_algorithm>Bron–Kerbosch algorithm</a> with degeneracy ordering is the most efficient way to find out all maximal cliques. Its time complexity can be optimized to O(3**(n/3)).

*Click <a href=https://github.com/je-suis-tm/graph-theory/blob/master/maximal%20clique.ipynb>here</a> to be redirected to the script.*

![alt text](https://github.com/je-suis-tm/graph-theory/blob/master/preview/maximal%20clique.jpg)

### 12. Epidemic Outbreak

Amid the outbreak of the novel corona virus, we have observed a bonanza of agent-based simulation in epidemiology. By leveraging the probability generating function of a random graph, whether it is <a href=https://github.com/je-suis-tm/graph-theory/blob/master/barabasi%20albert%20model.ipynb>Barabási-Albert</a> following power-law distribution or <a href=https://github.com/je-suis-tm/graph-theory/blob/master/watts%20strogatz%20model.ipynb>Erdős–Rényi</a> following Poisson distribution, we are able to consume the least computing power to estimate the prevalence and the duration of COVID-19.

*For more details, please refer to the <a href=https://github.com/je-suis-tm/graph-theory/blob/master/Epidemic%20Outbreak%20project/README.md>read me</a> page of a separate directory or <a href=https://je-suis-tm.github.io/graph-theory/epidemic-outbreak>graph theory</a> section on my personal blog.*

![alt text](https://github.com/je-suis-tm/graph-theory/blob/master/Epidemic%20Outbreak%20project/preview/gillespie.gif)

### 13. Portfolio Optimization

Modern portfolio theory was introduced in 1952 by Nobel laureate Harry Markowitz. It is part of investment class 101. But I watched a video by <a href=https://www.wolfram.com/training/videos/FIN015>Wolfram</a> recently. It challenged the traditional approach and introduced graph theory to asset diversification. There are plenty of quant shops deploying fancy mathematic tools to solve the market. The real question for us is, as fancy as it sounds, does graph theory work on portfolio optimization?

*For more details, please refer to the <a href=https://github.com/je-suis-tm/graph-theory/blob/master/Portfolio%20Optimization%20project/README.md>read me</a> page of a separate directory or <a href=https://je-suis-tm.github.io/graph-theory/portfolio-optimization>graph theory</a> section on my personal blog.*

![alt text](https://github.com/je-suis-tm/graph-theory/blob/master/Portfolio%20Optimization%20project/preview/outta%20sample%20mean%20variance.png)

### 14. Habitat Occupancy

In the traditional study of community ecology, metapopulation model is used to map out the patchy habitat occupancy and extinction. It only requires one ordinary differential equation to monitor a single species. However, one of the biggest malaise is its landscape connectivity. With complex network, we can incorporate spatial structure into the deterministic system to create an agent-based simulation.

*Click <a href=https://github.com/je-suis-tm/graph-theory/blob/master/habitat%20occupancy.ipynb>here</a> to be redirected to the script. Please note this script is written in Julia.*

![alt text](https://github.com/je-suis-tm/graph-theory/blob/master/preview/levins%20model.gif)

### 15. Habitat Competition

<a href=https://github.com/je-suis-tm/graph-theory/blob/master/habitat%20occupancy.ipynb>Levins model</a> has exceptional explanatory power for habitat fragmentation. Tilman model expands it to a more generalized form for multiple species. The stronger species can out-compete and displace weaker species. In this example, our agent-based simulation will illustrate the vis-à-vis among native species and invasive species. With the blessing of the spatial structure, some of the native species in remote area may be able to survive the invasion. 

![alt text](https://github.com/je-suis-tm/graph-theory/blob/master/preview/tilman%20model.gif)

In the later chapter of this script, we will introduce Schelling’s model from sociology to investigate how the segregation is formed when multiple groups are presented in the system. Schelling’s model shows some unique traits such as <a href=https://github.com/je-suis-tm/graph-theory/blob/master/maximal%20clique.ipynb>maximal clique</a> when implemented on a random geometric graph.

*Click <a href=https://github.com/je-suis-tm/graph-theory/blob/master/habitat%20competition.ipynb>here</a> to be redirected to the script. Please note this script is written in Julia.*

![alt text](https://github.com/je-suis-tm/graph-theory/blob/master/preview/schelling's%20model.gif)

&nbsp;


