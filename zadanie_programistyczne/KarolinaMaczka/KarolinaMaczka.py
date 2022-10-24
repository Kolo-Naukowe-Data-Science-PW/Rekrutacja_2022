import numpy as np
from queue import PriorityQueue

def shortest_path(Graph, n, v1, v2):
  V = [[-1 for i in range(n)] for j in range(n)]
  vertex=[]

  for i in Graph:
    V[ord(i[0])-65][ord(i[1])-65]=Graph[i]
    V[ord(i[1]) - 65][ord(i[0]) - 65] = Graph[i]
    vertex.append(i[0])
    vertex.append(i[1])

  vertex = np.array(vertex)
  vertex = np.unique(vertex)

  distances = {v: float('inf') for v in vertex}
  distances[v1]=0

  pq = PriorityQueue()
  pq.put((0, v1))
  visited = []

  while not pq.empty():
    distance1, vertex_cur = pq.get()
    visited.append(vertex_cur)

    for i in range(n):
      if V[ord(vertex_cur)-65][i]!=-1:
        distance = V[ord(vertex_cur)-65][i]
        if chr(i+65) not in visited:
          distance_old = distances[chr(i+65)]
          distance_new = distances[vertex_cur] + distance
          if distance_new < distance_old:
            pq.put((distance_new, chr(i+65)))
            distances[chr(i+65)] = distance_new

  return distances[v2]

def main():
  Graph = {
    ("B", "D"): 2,
    ("D", "A"): 1,
    ("B", "A"): 4,
    ("A", "C"): 2,
    ("B", "E"): 3,
    ("C", "D"): 7,
    ("E", "C"): 3
  }

  n = 5

  print(shortest_path(Graph, n, "A", "B"))
  print(shortest_path(Graph, n, "E", "D"))

if __name__=='__main__':
  main()