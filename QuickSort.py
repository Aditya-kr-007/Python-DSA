def partition(nums,l,r):
    key=nums[r]
    start=l
    for j in range(l,r+1):
        if nums[j]<=key:
            temp=nums[start]
            nums[start]=nums[j]
            nums[j]=temp
            start+=1
    return start-1

def quickSort(nums,l,r):
    if l>=r:
        return
    pivot=partition(nums,l,r)
    quickSort(nums,l,pivot-1)
    quickSort(nums,pivot+1,r)

def sortArray(nums):
    n=len(nums)
    quickSort(nums,0,n-1)
    return nums

nums=list(map(int,input("Enter the elements of the array separated by space: ").split()))
print("the sorted array is ",sortArray(nums))