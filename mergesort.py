def merge(nums,l,mid,r):
        a=[]               #initialize an empty list a to store the left half of the array
        b=[]                #initialize an empty list b to store the right half of the array
        for i in range(l,mid+1):
            a.append(nums[i])
        for i in range(mid+1,r+1):
            b.append(nums[i])
        
        i,j,k=0,0,l    #initialize three variables i,j,k to 0,0,l respectively.
                       #i and j will be used to traverse the left and right halves of the array
                       #while k will be used to keep track of the index in the original array.
        while k<=r:      
            if j == len(b):
                nums[k]=a[i]
                i+=1
                k+=1
            elif i == len(a):
                nums[k]=b[j]
                j+=1
                k+=1
            elif a[i]<b[j]:
                nums[k]=a[i]
                i+=1
                k+=1
            else:
                nums[k]=b[j]
                j+=1
                k+=1
    
def mergeSort(nums,l,r):   #
        #base case
        if l>=r:   #if the left index is greater than or equal to the right index, return from the function
            return
        #recursive case
        mid =(l+r)//2
        mergeSort(nums,l,mid)   #recursively sort the left half of the array from index l to mid
        mergeSort(nums,mid+1,r)   #recursively sort the right half of the array from index mid+1 to r
 
        merge(nums,l,mid,r)   #merge the two sorted halves of the array from index l to r
    
def sortArray(nums) :
        mergeSort(nums,0,len(nums)-1)
        return nums

nums=list(map(int,input("Enter the elements of the array separated by space: ").split()))
print("the sorted array is ",sortArray(nums))