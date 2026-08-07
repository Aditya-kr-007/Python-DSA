x=int(input())
temp=x
rev=0
while temp>0:
            r=temp%10
            temp=temp//10
            rev=rev*10+r
if rev==x:
    print(True)
else:
    print(False)    

#WE CAN ALSO WRITE DIRECTLY......return rev==x (if boolean is used)
