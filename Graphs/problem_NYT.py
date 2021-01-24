n,tar=map(int,input().split())
arr=[0]+[int(i) for i in input().split()]
cur=1
while cur<tar:cur+=arr[cur]
if cur==tar:print('YES')
else:print("NO")
    



