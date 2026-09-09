def binarysearch(nums, target):
        start=0
        end=len(nums)-1
        while start<=end:
            mid=(start+end)//2
            if target==nums[mid]:
                return mid
            elif target>nums[mid]:
                start=mid+1
            else:
                end=mid-1
        return -1
nums=list(map(int,input("enter the numbers= ").split()))
print(nums)
target=int(input("enter the target="))
print("the target is at index=", binarysearch(nums, target))

