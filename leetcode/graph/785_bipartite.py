from typing import List

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # MIN_INT = -10 ** 10
        # colors = [MIN_INT] * len(graph)
        # colors[0] = 1

        colored = {}

        for i in range(len(graph)):
            # checks all node, begins with 0
            if i not in colored and graph[i]:
                colored[i] = 1
                q = [i]

                while len(q) > 0:
                    node = q.pop(0)

                    for adj_node in graph[node]:
                        if adj_node not in colored:
                            colored[adj_node] = -colored[node]
                            q.append(adj_node)
                        elif colored[adj_node] == colored[node]:
                            return False 

        return True


print(Solution().isBipartite([[1,3], [0,2], [1,3], [0,2]]))
# print(Solution().isBipartite([[1,2,3], [0,2], [0,1,3], [0,2]]))
# print(Solution().isBipartite([[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]]))
                # if adj_node not in colored:
                #     colored[adj_node] = -colored[node]
                #     queue.append(adj_node)
                # elif colored[adj_node] == colored[node]:
                #     return False


    # def dfs(self, root, current_color):
    #     if self.visited[root] == True: return

    #     self.visited[root] = True
    #     for edge in self.graph[root]:
    #         self.colors[edge] = current_color * -1

    #         for next_edge in self.graph[edge]:
    #             self.dfs(next_edge, current_color * -1)