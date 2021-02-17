from collections import deque

# small world problem

def d_two_nodes_graph(g, num1, num2):
    count = 0
    q = deque()
    q.append(g[num1-1])
    current = 0
    while count < len(g):
        count += 1
        current = q.popleft()

        if (num2 in current):
            return count
        else:
            for i in current:
                q.append(g[i-1])
    return 404

graph = [[2, 4], [1, 3], [4, 2], [3, 1]]
graph = [ [2, 5], 
      [6, 5, 4], 
      [6, 9, 4], 
      [2, 3, 5, 8, 9], 
      [2, 3, 8, 7], 
      [6, 9], 
      [6, 5, 4], 
      [5, 3, 4, 7]]

print (d_two_nodes_graph(graph, 1, 9))
