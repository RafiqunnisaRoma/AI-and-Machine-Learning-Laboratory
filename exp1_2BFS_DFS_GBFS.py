
# BFS, DFS, GBFS and Bidirectional Search
from collections import deque
import heapq

G = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': ['G'],
    'F': ['G'],
    'G': []
}

h = {'A': 6, 'B': 4, 'C': 3, 'D': 2,
     'E': 2, 'F': 1, 'G': 0}

# Create reverse graph
RG = {n: [] for n in G}
for n in G:
    for x in G[n]:
        RG[x].append(n)


def bfs(s, goal):
    q = deque([(s, [s])])
    visited = {s}
    expanded = []
    while q:
        node, path = q.popleft()
        expanded.append(node)
        if node == goal:
            return path, expanded
        for x in G[node]:
            if x not in visited:
                visited.add(x)
                q.append((x, path + [x]))
    return None, expanded


def dfs(s, goal):
    stack = [(s, [s])]
    visited = set()
    expanded = []
    while stack:
        node, path = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        expanded.append(node)
        if node == goal:
            return path, expanded
        for x in reversed(G[node]):
            if x not in visited:
                stack.append((x, path + [x]))
    return None, expanded


def greedy(s, goal):
    pq = [(h[s], s, [s])]
    visited = set()
    expanded = []
    while pq:
        _, node, path = heapq.heappop(pq)
        if node in visited:
            continue
        visited.add(node)
        expanded.append(node)
        if node == goal:
            return path, expanded
        for x in G[node]:
            if x not in visited:
                heapq.heappush(pq, (h[x], x, path + [x]))
    return None, expanded


def bidirectional(s, goal):
    if s == goal:
        return [s], [s]

    q1, q2 = deque([s]), deque([goal])
    p1, p2 = {s: None}, {goal: None}
    expanded = []

    while q1 and q2:
        for q, graph, own, other in [
            (q1, G, p1, p2), (q2, RG, p2, p1)
        ]:
            for _ in range(len(q)):
                n = q.popleft()
                expanded.append(n)

                if n in other:
                    left, right = [], []
                    x = n
                    while x is not None:
                        left.append(x)
                        x = p1[x]

                    x = p2[n]
                    while x is not None:
                        right.append(x)
                        x = p2[x]

                    return left[::-1] + right, expanded

                for x in graph[n]:
                    if x not in own:
                        own[x] = n
                        q.append(x)

    return None, expanded


for name, search in [
    ('BFS', bfs), ('DFS', dfs),
    ('Greedy', greedy), ('Bidirectional', bidirectional)
]:
    path, expanded = search('A', 'G')
    print(f"\n{name}")
    print("Path:", ' -> '.join(path) if path else "No path")
    print("Expanded:", expanded)
    print("Path length:", len(path) - 1 if path else 0)
