from collections import deque
n, m, k =map(int, input().split())

directcount = [0] * n # node_iが直接接続しているノードの数
visited = [-1]  * n # nodeの色,
colorcount = [-1] * n # 各色が何個のノードを持つか
# グラフの初期化
g = []
for _ in range(n):
    g.append(deque(list()))

# グラフの生成
for i in range(m):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1 # 1origin -> 0 origin
    g[a].append(b)
    g[b].append(a)
    # 直接接続されているノードの数
    directcount[a] += 1
    directcount[b] += 1

# dfs 連結したグラフごとにそのグラフの最初に探索したnodeの色に染める
q = deque(list()) #探索キュー
for i in range(n):
    q.append(i)
    color = i
    cnt = 1
    while len(q) > 0:
        nextnode = q.popleft() # 次の探索
        if visited[nextnode] != -1:
            continue
        visited[nextnode] = color
        q.extend(g[nextnode]) # nextnodeの辺を足す
        cnt += 1
    # 探索が終わったらその色のノードの数を記録
    colorcount[color]  = cnt - 1

# res[i] = ノードの色, その色のノードの数 - そのノードが直接接続しているノード数 - 自分自身(1)　で初期化する
# res = [[visited[i], colorcount[visited[i]] - (directcount[i] + 1)] for i in range(n)]
res = []
for i in range(n):
    res.append([visited[i], colorcount[visited[i]] - (directcount[i] + 1)])

# ブロックリスト
for i in range(k):
    c, d = map(int, input().split())
    c, d = c - 1, d - 1 # 1 origin -> 0 origin
    # ブロック関係が同じ色だとするなら
    if res[c][0] == res[d][0]:
        # 友達になれると思っていた数を1つ減らす
        res[c][1] -= 1
        res[d][1] -= 1

import pdb; pdb.set_trace()
# 結果の表示
print(" ".join(list(map(lambda x: str(x[1]), res))))