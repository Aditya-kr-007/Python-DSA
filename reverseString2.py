s=list(input("enter the string ="))
i=0
j=len(s)-1
while i<j:
    temp=s[i]
    s[i]=s[j]
    s[j]=temp
    i+=1
    j-=1
print("the reverse string is =" ,"".join(s))