# 7
# abcdbbd
# 6
# 2 3 6
# 1 5 z
# 2 1 1
# 1 4 a
# 1 7 d
# 2 1 7

n = int(input())
s = input()

Q = int(input())

for i in range(Q):
  order = list(map(str, input().split()))

  if int(order[0]) == 1:
    iq, cq = int(order[1])-1, order[2]
    s = s[:iq] + cq + s[iq+1:]
  else:
    lq, rq = int(order[1])-1, int(order[2])-1
    substr = s[lq:rq+1]
    print(len(set(substr)))


今回こういうことがおきました

15~20m でディスカッション

デリバリーでお客さんのクラウド検証・本番環境で作業することにおいて、気をつけていることはあるか？
- パスワードの基準・管理
- どのレベルまでお客さんにコンセンサスを取っているのか
- Security (フリーソフト）
- Linux上での注意とWindows上での注意
- コンピュートの鍵のパスワードは？
- 

作業が完了したので、チェック宜しくお願い致します。