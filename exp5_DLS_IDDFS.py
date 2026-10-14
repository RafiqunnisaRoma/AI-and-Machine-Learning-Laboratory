# Depth-Limited Search and IDDFS

tree = {
    "S": ["A", "B"],
    "A": ["C", "D"],
    "B": ["E", "F"],
    "C": [], "D": ["G"],
    "E": [], "F": [], "G": []
}

# Depth-Limited Search
def dls(graph, node, goal, limit, path=None):
    if path is None:
        path = [node]

    if node == goal:
        return path

    if len(path) - 1 >= limit:
        return None

    for child in graph[node]:
        if child not in path:
            result = dls(
                graph, child, goal, limit, path + [child]
            )
            if result is not None:
                return result

    return None


# Iterative Deepening DFS
def iddfs(graph, start, goal, max_depth):
    for limit in range(max_depth + 1):
        result = dls(graph, start, goal, limit)
        print("Limit", limit, ":", result)

        if result is not None:
            return limit, result

    return None, None


# Main program
print("Available nodes:", list(tree.keys()))

start = input("Enter start node: ").upper()
goal = input("Enter goal node: ").upper()

try:
    limit = int(input("Enter DLS depth limit: "))
    max_depth = int(input("Enter IDDFS maximum depth: "))

    if start not in tree or goal not in tree:
        print("Invalid node!")

    elif limit < 0 or max_depth < 0:
        print("Depth cannot be negative!")

    else:
        print("DLS result:", dls(tree, start, goal, limit))

        depth, path = iddfs(tree, start, goal, max_depth)
        print("IDDFS result:", (depth, path))

except ValueError:
    print("Please enter valid integer depth limits.")



'''
graph = {
    "S": ["A"],
    "A": ["B"],
    "B": ["S", "G"],
    "G": []
}
print("DLS limit 2:", dls(graph, "S", "G", 2))
print("DLS limit 3:", dls(graph, "S", "G", 3))
print("IDDFS:", iddfs(graph, "S", "G", 5))
'''

#print("DLS limit 2:", dls(tree, "S", "G", 2))
#print("DLS limit 3:", dls(tree, "S", "G", 3))
#print("IDDFS:", iddfs(tree, "S", "G", 5))