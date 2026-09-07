def reverseString(s):
    if len(s)==0:
         return 
    s=list(s)
    s.reverse()
    print("the reverse string is = " ,"".join(s))
s=input("enter the string =")
reverseString(s)



 