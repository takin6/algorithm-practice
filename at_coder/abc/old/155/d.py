n,k=map(int,input().split())
arr=list(map(int,input().split()))
arr=sorted(arr)
nc=0
zc=0
pc=0
for i in range(n): #負数の数(nc)、0の数(zc)、正数の数(pc)を数える
  if arr[i]<0:
    nc+=1
  elif arr[i]==0:
    zc+=1
  else:
    pc+=1
ncc=nc*pc #積が負となるペアの個数を求める
zcc=zc*(nc+pc)+(zc*(zc-1))//2 #積が0となるペアの個数を求める
pcc=(nc*(nc-1))//2+(pc*(pc-1))//2 #積が正となるペアの個数を求める
if k<=ncc: #K番目の値が負の場合
  arr1=[]
  arr2=[]
  for i in range(n): #負数、正数をそれぞれ昇順に並べる
    if arr[i]<0:
      arr1.append(-arr[i])
    elif arr[i]>0:
      arr2.append(arr[i])
  arr1=arr1[::-1]

  c1=len(arr1)
  c2=len(arr2)
  l=0
  r=10**18+1
  k=ncc-k #負数のマイナスを取って計算しているため積の大小が逆転するので、大きなほうからK番目、すなわち、小さなほうから(積が負となるペアの個数-K)番目の値を求める
  while r-l!=1:
    mid=(l+r)//2
    cnt=0
    pos=c2-1
    for i in range(c1): #各負数ごとに積が勝手に決めた値midよりも小さくなる正数の個数を求め足し合わせる(しゃくとり法)
      while pos!=-1:
        print(pos, mid, arr2[pos], mid//arr1[i])
        if arr2[pos]>mid//arr1[i]:
          pos-=1
        else:
          break        
      cnt+=pos+1
    if cnt>k: #勝手に決めた値mid以下の個数が(積が負となるペアの個数-K)個以上であれば真の値はmid以下
      r=mid
    else: #そうでなければ真の値はmid以上
      l=mid
  print(-r) #負数のマイナスを取って計算したので最後にマイナスを付けて出力する
elif k<=(ncc+zcc): #K番目の値が0の場合
  print(0)
else: #K番目の値が正の場合
  arr1=[]
  arr2=[]
  for i in range(n): #負数、正数をそれぞれ昇順に並べる
    if arr[i]<0:
      arr1.append(-arr[i])
    elif arr[i]>0:
      arr2.append(arr[i])
  arr1=arr1[::-1]
  c1=len(arr1)
  c2=len(arr2)
  l=0
  r=10**18+1
  k-=(ncc+zcc) #正数の中で小さい順にK番目の数を調べたいので負数、0の数を取り除く
  while r-l!=1:
    mid=(l+r)//2
    cnt1=0
    pos1=c1-1
    for i in range(c1): #各負数ごとに積が勝手に決めた値midよりも小さくなる負数の個数を求め足し合わせる(しゃくとり法)
      tmp=0
      while pos1!=-1:
        if arr1[pos1]>mid//arr1[i]:
          pos1-=1
        else:
          break
      tmp+=pos1+1
      if arr1[i]**2<mid: #各要素について、自身を2回選んだ場合の積が勝手に決めた値mid以下なら条件を満たすペアの個数を1減らす
        tmp-=1
      cnt1+=tmp
    cnt1=cnt1//2 #上記の処理では同じペアが2回数えられているので個数を半分にする
    cnt2=0
    pos2=c2-1
    for i in range(c2): #各正数ごとに積が勝手に決めた値midよりも小さくなる正数の個数を求め足し合わせる(しゃくとり法)
      tmp=0
      while pos2!=-1:
        if arr2[pos2]>mid//arr2[i]:
          pos2-=1
        else:
          break
      tmp+=pos2+1
      if arr2[i]**2<mid:
        tmp-=1 #各要素について、自身を2回選んだ場合の積が勝手に決めた値mid以下なら条件を満たすペアの個数を1減らす
      cnt2+=tmp
    cnt2=cnt2//2 #上記の処理では同じペアが2回数えられているので個数を半分にする
    cnt=cnt1+cnt2
    if cnt>=k: #勝手に決めた値mid以下の個数がK個以上であれば真の値はmid以下
      r=mid
    else: #そうでなければ真の値はmid以上
      l=mid
  print(r)