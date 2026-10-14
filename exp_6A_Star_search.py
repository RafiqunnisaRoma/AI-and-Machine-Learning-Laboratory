#A * Search
import heapq

G = {
    'S': [('A', 1), ('B', 5)],
    'A': [('C', 2), ('D', 4)],
    'B': [('D', 1)],
    'C': [('G', 5)],
    'D': [('G', 2)],
    'G': []
}

# Admissible heuristic
h = {'S': 4, 'A': 4, 'B': 3, 'C': 5, 'D': 2, 'G': 0}


def astar(start, goal, h):
    pq = [(h[start], 0, start, [start])]
    best = {start: 0}
    expanded = set()

    while pq:
        f, g, node, path = heapq.heappop(pq)

        if g != best[node]:
            continue

        if node in expanded:
            continue
        expanded.add(node)

        print(node, "g =", g, "h =", h[node], "f =", f)

        if node == goal:
            return path, g

        for neighbor, cost in G[node]:
            new_g = g + cost

            if new_g < best.get(neighbor, float('inf')):
                best[neighbor] = new_g
                new_f = new_g + h[neighbor]
                heapq.heappush(
                    pq, (new_f, new_g, neighbor, path + [neighbor])
                )

    return None, float('inf')


print("Admissible heuristic:")
path, cost = astar('S', 'G', h)
print("Optimal path:", ' -> '.join(path))
print("Total cost:", cost)

# Make the heuristic overestimate the cost at B
h_bad = h.copy()
h_bad['B'] = 10

print("\nOverestimating heuristic:")
path, cost = astar('S', 'G', h_bad)
print("Path:", ' -> '.join(path))
print("Total cost:", cost)
