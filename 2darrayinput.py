#PREFERED FORMAT
rows = int(input("enter rows: "))
cols = int(input("enter columns: "))
matrix = []
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

print(matrix) 

#LONG METHOD IN WHICH INPUT IS TAKEN ONE BY ONE BUT NOT WHOLE COLUMN OF EACH ROW AT ONCE.
"""
rows = int(input("enter rows: "))
cols = int(input("enter cols: "))

matrix = []

for i in range(rows):
    row = []
    for j in range(cols):
        c = int(input())
        row.append(c)
    matrix.append(row)

print(matrix)
"""