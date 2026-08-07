n=int(input("enter the integer= "))
temp=n
Sum=0
Prod=1
while temp>0:
         r=temp%10
         Prod=Prod*r
         Sum=Sum+r
         temp=temp//10
print("the product is ", Prod)
print("the sum is ", Sum)
print("the subtraction of product and sum is ", Prod-Sum)