from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.result = []
        return self.dfs(0, graph)
        # return self.dfs(graph, 0)

        # def dfs(cur, path):
        #     if cur == len(graph) - 1: res.append(path)
        #     else:
        #         for i in graph[cur]:
        #             dfs(i, path + [i])

        # res = []
        # dfs(0, [0])
        # return res

    def dfs(self, node, graph):
        # print(path)
        # if len(graph[node]) == 0 and visited[node] == False:
        #     self.result.append(path)
        #     return

        # if visited[node] == True:
        #     self.result.append(path)
        #     return

        # visited[node] = True
        # path.append(node)

        # for next_node in graph[node]:
        #     print(node, next_node, visited)
        #     # import pdb; pdb.set_trace()
        #     self.dfs(next_node, path, visited, graph)

        N = len(graph)
        if node == N-1: return [[N-1]]
        ans = []
        for nei in graph[node]:
            for path in self.dfs(nei, graph):
                ans.append([node] + path)
        return ans


print(Solution().allPathsSourceTarget([[1,2], [3], [3], []] ))