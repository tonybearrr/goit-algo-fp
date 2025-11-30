"""Dijkstra's algorithm using binary heap (priority queue)"""
import heapq


def dijkstra(graph, start):
    """Find shortest paths from start to all vertices using binary heap"""
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    prev = {vertex: None for vertex in graph}
    heap = [(0, start)]
    visited = set()

    while heap:
        cur_dist, cur = heapq.heappop(heap)

        if cur in visited:
            continue

        visited.add(cur)

        for neighbor, weight in graph[cur].items():
            dist = cur_dist + weight

            if dist < distances[neighbor]:
                distances[neighbor], prev[neighbor] = dist, cur
                heapq.heappush(heap, (dist, neighbor))

    return distances, prev


def get_path(prev, start, end):
    """Reconstruct path from start to end"""
    if prev[end] is None and end != start:
        return []
    path = []
    cur = end
    while cur is not None:
        path.append(cur)
        cur = prev[cur]
    return path[::-1]


if __name__ == "__main__":
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'A': 4, 'C': 1, 'D': 5},
        'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
        'D': {'B': 5, 'C': 8, 'E': 2},
        'E': {'C': 10, 'D': 2}
    }

    start_vertex = 'A'
    distances, prev = dijkstra(graph, start_vertex)

    print("=" * 50)
    print(f"НАЙКОРОТШІ ШЛЯХИ ВІД '{start_vertex}'")
    print("=" * 50)

    for vertex in sorted(graph.keys()):
        if vertex != start_vertex:
            path = get_path(prev, start_vertex, vertex)
            print(f"\n{start_vertex} -> {vertex}:")
            print(f"  Відстань: {distances[vertex]}")
            print(f"  Шлях: {' -> '.join(path)}")
