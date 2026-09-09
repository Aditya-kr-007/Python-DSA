"""
Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""
def lowerbound(nums, target):
        n= len(nums)
        l=0
        r=n-1
        ans=n

        while l<=r:
            mid =(l+r)//2
            if nums[mid]>=target:
                ans=mid #maybe but not sure
                r=mid-1
            else:
                #right
                l=mid+1
        
        return ans
def upperbound(nums, target):
        n= len(nums)
        l=0
        r=n-1
        ans=n

        while l<=r:
            mid =(l+r)//2
            if nums[mid]>target:
                ans=mid #maybe but not sure
                r=mid-1
            else:
                #right
                l=mid+1
        
        return ans
def searchRange(nums,target):
        lb = lowerbound(nums,target)
        ub = upperbound(nums,target)

        if lb==ub:
            return [-1,-1]
        else:
            return [lb,ub-1]

nums=[3,3,5,5,5,5,6,6,9,10,10]
print(nums)
target=int(input("enter the target="))
print(searchRange(nums,target))