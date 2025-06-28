import heapq


#  dijkstra with priority queue
def dijkstra(adj, n, src):
    dist = [float("inf")] * n
    dist[src] = 0
    pq = [(0, src)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
    return dist


#  prim's algorithm with priority queue
#  The weight of a spanning tree is determined by the minimum sum of weight of all the edge involved in it.
def prim(adj, n):
    res = 0
    visited = [False] * n
    pq = [(0, 0)]  # (weight, node)
    while pq:
        w, u = heapq.heappop(pq)
        if visited[u]:
            continue
        visited[u] = True
        res += w
        for v, weight in adj[u]:
            if not visited[v]:
                heapq.heappush(pq, (weight, v))
    return res
