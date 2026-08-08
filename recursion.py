def printNum(i,n):
    #base case
    if i>n:
        return
    #recursive case
    print(i,end=" ")
    printNum(i+1,n)


i=int(input("enter the first of range= "))
n=int(input("enter the second of range= "))
printNum(i,n)
