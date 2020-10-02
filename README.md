# Graph Theory

&nbsp;

*Currently the directory is a lil bit messy due to the massive expansion of its content. The repository was originally set up for graph traversal algorithms (the interview stuff). Unfortunately, I fell in love with the graph theory and gradually did more and more network analysis :see_no_evil: I promise I will redesign the directory to make it easier for users to navigate. You have to be patient with me though :snail:*

&nbsp;

## Intro

Graph theory, sometimes we call it complex network or network science or network analysis, is one of the most avant-garde research areas in discrete mathematics, also one of my favorite subjects. Here, “graph” is the preferred name, because too many people associate the word “network” with internet. Given the bonanza of data science, graph theory is constantly overshadowed by the hype of machine learning. Yet some of the top-notch technology companies such as Google and Facebook heavily rely on the research of graph theory. 

This repository intends to increase the exposure of graph theory to all my readers. It contains common graph algorithms, popular network models, interesting agent-based simulations and amazing complex systems. The codes range from the level of elementary to sophisticated with wide applications in ecology, epidemiology, sociology, economics, finance, etc. Both Julia and Python are used to construct different scripts. As I am slowly climbing up the learning curve, more and more fascinating content will emerge en masse. Stay tuned!

&nbsp;

## Table of Contents

### Algorithms

<a href=https://github.com/je-suis-tm/graph-theory/blob/master/BFS%20DFS%20on%20DCG.ipynb>1. Breadth First Search</a>

<a href=https://github.com/je-suis-tm/graph-theory/blob/master/BFS%20DFS%20on%20DCG.ipynb>2. Depth First Search</a>

<a href=https://github.com/je-suis-tm/graph-theory/blob/master/topological%20sort.ipynb>3. Topological Sort</a>

<a href=https://github.com/je-suis-tm/graph-theory/blob/master/dijkstra%20shortest%20path.ipynb>4. Dijkstra</a>

<a href=https://github.com/je-suis-tm/graph-theory/blob/master/minimum%20spanning%20tree.ipynb>5. Prim/Kruskal/Borůvka</a>

<a href=https://github.com/je-suis-tm/graph-theory/blob/master/a_star%20maze.ipynb>6. A* Search</a>

<a href=https://github.com/je-suis-tm/graph-theory/blob/master/bellman_ford%20forex%20arbitrage.ipynb>7. Bellman Ford</a>

<a href=https://github.com/je-suis-tm/graph-theory/blob/master/k%20core.ipynb>8. Matula Beck</a>

<a href=https://github.com/je-suis-tm/graph-theory/blob/master/k%20core.ipynb>9. Batagelj Zaveršnik</a>

<a href=https://github.com/je-suis-tm/graph-theory/blob/master/maximal%20clique.ipynb>10. Bron Kerbosch</a>

<a href=https://github.com/je-suis-tm/graph-theory/blob/master/habitat%20competition.ipynb>11. Gillespie</a>

&nbsp;

### Applications

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

<a href=https://github.com/je-suis-tm/graph-theory#14-habitat-occupancy>14. Habitat Occupancy</a>

<a href=https://github.com/je-suis-tm/graph-theory#15-habitat-competition>15. Habitat Competition</a>

&nbsp;

### Models

<a href=https://github.com/je-suis-tm/graph-theory/blob/master/watts%20strogatz%20model.ipynb>1. Erdős–Rényi</a>

<a href=https://github.com/je-suis-tm/graph-theory/blob/master/watts%20strogatz%20model.ipynb>2. Watts-Strogatz</a>

<a href=https://github.com/je-suis-tm/graph-theory/blob/master/barabasi%20albert%20model.ipynb>3. Barabási-Albert</a>

<a href=https://github.com/je-suis-tm/graph-theory/blob/master/bianconi%20barabasi%20model.ipynb>4. Bianconi-Barabási</a>

&nbsp;

## Applications

### 1. Maze

Walking out of a maze seems extremely complex in recursion algorithm. In graph theory, it is just a walk in the park. The only bit that takes some effort is building the data structure. Once we got graph ADT, we can use BFS/DFS/Dijkstra/A* to find the way out of the maze, although DFS may not be able to point out the shortest route.

*Click <a href=https://github.com/je-suis-tm/graph-theory/blob/master/a_star%20maze.ipynb>here</a> to be redirected to the script.*

![alt text](https://github.com/je-suis-tm/graph-theory/blob/master/preview/a_star.png)

### 2. Minimum Spanning Tree

Consider a case where a postman is going to deliver mails to every house in the community. The distance between each house is completely different, some are shorter, some are longer. Ideally the postman wants to deliver mails to each house with the least travel distance and visit each house only once. There are a few algorithms to solve this type of issue. In this case, we choose Borůvka, Prim and Kruskal. And the topological output of these algorithms can be interpreted as a <a href=https://en.wikipedia.org/wiki/Minimum_spanning_tree>minimum spanning tree</a>. It is a subset of the edges of a connected, edge-weighted undirected graph that connects all the vertices together, without any cycles and with the minimum possible total edge weight.

*Click <a href=https://github.com/je-suis-tm/graph-theory/blob/master/minimum%20spanning%20tree.ipynb>here</a> to be redirected to the script.*

![alt text](https://github.com/je-suis-tm/graph-theory/blob/master/preview/minimum%20spanning%20tree%20subset.jpg)

### 3. Shortest Path

Whenever we hear the phrase 'shortest path', we should instinctively shout out Dijkstra's algorithm in our mind. This Dutchman came up with the revolutionary algorithm named after himself while searching for the shortest path to Rotterdam without pencil and paper. The algorithm is a special case of A* algorithm without heuristic function. It is also widely used as a subroutine for other traversal algorithms, such as Bellman-Ford. Apart from Dijkstra, the shortest path problem, which could be thought as an optimization problem, can also be solved in <a href=https://github.com/je-suis-tm/recursion-and-dynamic-programming>dynamic programming</a>.

*Click <a href=https://github.com/je-suis-tm/graph-theory/blob/master/dijkstra%20shortest%20path.ipynb>here</a> to be redirected to the script.*

![alt text](https://github.com/je-suis-tm/graph-theory/blob/master/preview/dijkstra.jpg)

### 4. Water Jug

Water jug is a simple and interesting problem. Assuming there are two jugs, a m-gallon and a n-gallon. And the target is to get x gallon water in either jug. There are many ways to solve this problem. Recursion can also solve water jug problem but it is very costly. Building a graph data structure would be a much easier way. The key is to set up edges based upon the rule of the game to connect all possible scenarios together. With BFS starts from the initial status, it can efficiently find the target status and return the route for us which would be the answer.

*Click <a href=https://github.com/je-suis-tm/graph-theory/blob/master/water%20jug%20problem.ipynb>here</a> to be redirected to the script.*

### 5. Knight's Tour

Knight's tour is a game where a knight travels all the squares on a k by k chessboard. And each square can only be travelled once. The solution can be obtained by DFS with a list that records whether each square on the chessboard has been visited. The rules of a knight's movement are very different from pawns or king. The edges of the graph should indicate the valid move from one square to another.
 
*Click <a href=https://github.com/je-suis-tm/graph-theory/blob/master/knights%20tour.ipynb>here</a> to be redirected to the script.*

### 6. Missionaries and Cannibals

Missionaries and cannibals is a classic river problem. I actually prefer its alternative version called jealous husband. There are k missionaries and k cannibals. They need to cross a river. There is a boat with the capacity of only two people. There should be at least one person to sail the boat. These rules are subjected to one constraint. Cannibals cannot outnumber missionaries on both sides of the river. Again, the solution is similar to water jug problem. We have to set up edges based upon the rule of the game to connect all possible and valid scenarios together. As usual, BFS always return the optimized result rather than DFS.

*Click <a href=https://github.com/je-suis-tm/graph-theory/blob/master/missionaries%20and%20cannibals%20problems.ipynb>here</a> to be redirected to the script.*

### 7. Forex Arbitrage

Finding the shortest path on a map is not the only problem Dijkstra can solve. Financial market is another application. As we all know, currency pairs have both bid and ask price. The market is weak-efficient. There could be an opportunity for triangle arbitrage or rectangle arbitrage. We can exchange from currency A to currency B then to currency C if we can churn out more profit rather than directly exchanging currency A to currency C. We set each currency as the vertex and the exchange rate from one currency to another as the weight of the edge. The arbitrage with some logarithm transformation would be the criteria for Dijkstra. However, Dijkstra cannot properly handle a graph structure with negative weights. We will introduce an improved version called Bellman-Ford which is able to detect the negative cycle during the traversal.

*Click <a href=https://github.com/je-suis-tm/graph-theory/blob/master/bellman_ford%20forex%20arbitrage.ipynb>here</a> to be redirected to the script.*

![alt text](https://github.com/je-suis-tm/graph-theory/blob/master/preview/arbitrage.png)

### 8. Word Ladder

Word ladder problem is a game developed by the author of Alice in Wonderland. Given one word, we try to change it into another word. Each time we can only change one letter and it should also be a valid word. This is a great test for vocabulary. The difficult part of building a graph structure is to build edges. Connect one word to another with only one letter changed takes a bit of work. BFS is the perfect solution for this.

*Click <a href=https://github.com/je-suis-tm/graph-theory/blob/master/word%20ladder.ipynb>here</a> to be redirected to the script.*

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

### 12. Epidemic Outbreak

Amid the outbreak of the novel corona virus, we have observed a bonanza of agent-based simulation in epidemiology. By leveraging the probability generating function of a random graph, whether it is <a href=https://github.com/je-suis-tm/graph-theory/blob/master/barabasi%20albert%20model.ipynb>Barabási-Albert</a> following power-law distribution or <a href=https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93R%C3%A9nyi_model>Erdős–Rényi</a> following Poisson distribution, we are able to consume the least computing power to estimate the prevalence and the duration of COVID-19.

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


