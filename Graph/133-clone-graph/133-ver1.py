
# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]

            copy = Node(node.val)
            oldToNew[node] = copy

            for n in node.neighbors:
                copy.neighbors.append(dfs(n))

            return copy

        return dfs(node) if node else None
#         if not node:
#             return []

#         q = collections.deque()
#         node = new Node(node.val)
#         q.append(node.neighbors)

#         while q:
#             neighbors = q.popleft()
#             for n in neighbors:
#                 # use bfs to find all neighbors of n
#                 newNeighbor = bfs(n)
#                 node.neigbors.append(newNeighbor)
