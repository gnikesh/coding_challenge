# Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors. OJ's undirected graph serialization: Nodes are labeled uniquely. We use # as a separator for each node, and , as a separator for node label and each neighbor of the node. As an example, consider the serialized graph {0,1,2#1,2#2,2}. The graph has a total of three nodes, and therefore contains three parts as separated by #. First node is labeled as 0. Connect node 0 to both nodes 1 and 2. Second node is labeled as 1. Connect node 1 to node 2. Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle. Visually, the graph looks like the following: 1 / \ /   \ 0 --- 2 / \ \_/


"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # Time complexity: O(N + M), where N is the number of nodes and M is the number of edges.
        # Space complexity: O(N), where N is the number of nodes.
        
        if not node:
            return None
        
        visited = {}
        
        def dfs(node):
            if node in visited:
                return visited[node]
            
            clone_node = Node(node.val, [])
            visited[node] = clone_node
            
            for neighbor in node.neighbors:
                clone_node.neighbors.append(dfs(neighbor))
            
            return clone_node
        
        return dfs(node)
