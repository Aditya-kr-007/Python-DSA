num=int(input()) 
temp=num
count=0
while temp>0:
    r=temp%10
    if num%r==0:
            count=count+1
    temp=temp//10
print(count)