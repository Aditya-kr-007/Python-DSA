def partition(nums,l,r):
    # Choose the last element as the pivot.
    key=nums[r]
    start=l

    # Move all values less than or equal to the pivot to the left side.
    for j in range(l,r+1):
        if nums[j]<=key:
            temp=nums[start]
            nums[start]=nums[j]
            nums[j]=temp
            start+=1

    # Pivot is now at its correct sorted position.
    return start-1

def quickSort(nums,l,r):
    # Stop when the current part has zero or one element.
    if l>=r:
        return

    # Partition the array and sort the parts before and after the pivot.
    pivot=partition(nums,l,r)
    quickSort(nums,l,pivot-1)
    quickSort(nums,pivot+1,r)

def sortArray(nums):
    n=len(nums)
    # Sort the whole array in place.
    quickSort(nums,0,n-1)
    return nums

# Take all array elements in one line and print the sorted result.
nums=list(map(int,input("Enter the elements of the array separated by space: ").split()))
print("the sorted array is ",sortArray(nums))
