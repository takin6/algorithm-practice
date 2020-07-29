# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        q = [node]
        nodeCopy = Node(node.val)
        dic = {node: nodeCopy}

        while q:
            cur_node = q.pop(0)
            deepCopyGraph = Node(cur_node)

            for neighbor in cur_node.neighbors:
                if neighbor not in dic:
                    neighborCopy = Node(neighbor.val)
                    dic[neighbor] = neighborCopy
                    dic[cur_node].neighbors.append(neighborCopy)
                    q.append(neighbor)
                else:
                    dic[cur_node].neighbors.append(dic[neighbor])

        return nodeCopy

# [[2,4],[1,3],[2,4],[1,3]]
node1, node2, node3, node4 = Node(1), Node(2), Node(3), Node(4)
node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]

print(Solution().cloneGraph(node1))