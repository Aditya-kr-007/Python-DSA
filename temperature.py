temp=int(input("enter the temperature in C'= "))

if temp<=50 and temp>=25:
    print("hot")
elif temp<25 and temp>=10:
    print("cold")
else:
    print("extremely cold")

if 25<=temp<=50:
    print("hot")
elif 10<=temp<25:
    print("cold")
else:
    print("extremely cold")

#ternary operator

age=int(input("enter ur age= "))
result="eligible" if age>=18 else "not eligible"
print(result)

