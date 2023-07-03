graph = {
    'A': 'BDE',
    'B': 'AC',
    'C': 'BDEF',
    'D': 'ACF',
    'E': 'ACG',
    'F': 'CD',
    'G': 'E',
    'H': 'I',
    'I': 'HJ',
    'J': 'I'
}


def bfs(graph, start):
    queue = [start]
    visited = set()

    while len(queue) != 0:
        current = queue.pop(0)
        visited.add(current)

        for node in graph[current]:
            if node not in visited:
                queue.append(node)

    return visited


print(bfs(graph, 'A'))
