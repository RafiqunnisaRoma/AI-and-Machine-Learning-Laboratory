from collections import deque
import heapq

# Graph Input
G = {}

n = int(input("Enter number of edges: "))

for i in range(n):
    a, b = input("Enter edge (node1 node2): ").split()
    G.setdefault(a, []).append(b)
    G.setdefault(b, []).append(a)

# Heuristic Input
h = {}
nodes = input("Enter all nodes separated by space: ").split()

for node in nodes:
    G.setdefault(node, [])
    h[node] = int(input("Heuristic of " + node + ": "))

# BFS
def bfs(s, goal):
    q = deque([(s, [s])])
    visited = {s}
    count = 0

    while q:
        node, path = q.popleft()
        count += 1

        if node == goal:
            return path, count

        for x in G[node]:
            if x not in visited:
                visited.add(x)
                q.append((x, path + [x]))

    return None, count

# DFS
def dfs(s, goal):
    stack = [(s, [s])]
    visited = set()
    count = 0

    while stack:
        node, path = stack.pop()

        if node in visited:
            continue

        visited.add(node)
        count += 1

        if node == goal:
            return path, count

        for x in reversed(G[node]):
            if x not in visited:
                stack.append((x, path + [x]))

    return None, count

# Bidirectional Search
def bi(s, goal):
    if s == goal:
        return [s], 1

    q1, q2 = deque([s]), deque([goal])
    p1, p2 = {s: [s]}, {goal: [goal]}
    v1, v2 = {s}, {goal}
    count = 0

    while q1 and q2:
        node = q1.popleft()
        count += 1

        for x in G[node]:
            if x not in v1:
                v1.add(x)
                p1[x] = p1[node] + [x]
                q1.append(x)

                if x in v2:
                    return p1[x] + p2[x][-2::-1], count

        node = q2.popleft()
        count += 1

        for x in G[node]:
            if x not in v2:
                v2.add(x)
                p2[x] = p2[node] + [x]
                q2.append(x)

                if x in v1:
                    return p1[x] + p2[x][-2::-1], count

    return None, count

# Greedy Best-First Search
def greedy(s, goal):
    pq = [(h[s], s, [s])]
    visited = set()
    count = 0

    while pq:
        _, node, path = heapq.heappop(pq)

        if node in visited:
            continue

        visited.add(node)
        count += 1

        if node == goal:
            return path, count

        for x in G[node]:
            if x not in visited:
                heapq.heappush(pq, (h[x], x, path + [x]))

    return None, count

# Main
start = input("Enter start node: ")
goal = input("Enter goal node: ")

if start not in G or goal not in G:
    print("Invalid start or goal node!")
elif start not in h or goal not in h:
    print("Enter heuristic values for all nodes!")
else:
    for name, search in [
        ("BFS", bfs),
        ("DFS", dfs),
        ("Bidirectional", bi),
        ("Greedy Best-First", greedy)
    ]:
        path, count = search(start, goal)

        if path:
            print(f"\n{name}: {path}")
            print("Path length:", len(path) - 1)
        else:
            print(f"\n{name}: No path found")

        print("Expanded nodes:", count)



'''

G = {
    "A":["B","C"], "B":["A","D","E"],
    "C":["A","F"], "D":["B","G"],
    "E":["B","G"], "F":["C","G"],
    "G":["D","E","F"]

}
'''