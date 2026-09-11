def searchMatrix(matrix,target):
        rows=len(matrix)
        cols=len(matrix[0])

        left=0
        right=rows*cols-1

        while left<=right:
            mid=(left+right)//2
            #find real indices for matrix[i][j]
            i= mid//cols   
            j= mid%cols     #formula
            
            if matrix[i][j]==target:
                return True
            elif matrix[i][j]>target:
                #target is in left side
                right=mid-1
            else:
                #if mid value < target
                #target is in right side
                left=mid+1
        
        return False

rows=int(input("enter the no. of rows="))
cols=int(input("enter the no. of cols="))
matrix=[]
for i in range(rows):
     row=list(map(int,input().split()))
     matrix.append(row)
print(matrix)
target=int(input("enter the target for searching="))
print("the target is present=",searchMatrix(matrix,target))