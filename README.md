<<<<<<< HEAD
## IMTool
this package aims to contain Influence Maximization tools as much as possible.

## Function
So far, with the following algorithm models, it will continue to expand in the future:
- IMRank
- IC based on Monte Carlo
- IC based on LT
- Greedy based on IC


# IMTool
this repository is a Influence Maximization tools kit, including Classic methods and algorithms for papers in recent years. Hopes to fill the gap in Maximizing Impact Problem in github. 


# EXAMPLE
```python
## test based on IMRank
data = np.loadtxt('./graph.txt')
data = list(data)

IMRank(data)
```

```python
 ## test Greedy based on IC
source = [0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,2,3,4,5]
target = [2,3,4,5,6,7,8,9,2,3,4,5,6,7,8,9,6,7,8,9]

g = Graph(directed=True)
g.add_vertices(range(10))
g.add_edges(zip(source, target))

greed_res = greedy(g, 2, p=0.2, mc=1000)

print(greed_res)
```

