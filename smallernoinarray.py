n=int(input())
arr=list(map(int,input().split()))
ans=[]
for i in arr:
    c=0
    for j in arr:
        if j<i:
            c=c+1
    ans.append(c)
print(ans)
