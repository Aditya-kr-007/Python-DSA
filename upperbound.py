"""
Search Insert Position:-
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.
Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2
"""

def lowerbound(nums, target):
        n= len(nums)
        l=0
        r=n-1
        ans=n

        while l<=r:
            mid =(l+r)//2
            if nums[mid]>target:  #Only "=" will be removed in  if nums[mid]>=target:
                ans=mid #maybe but not sure
                r=mid-1
            else:
                #right
                l=mid+1
        
        return ans

def searchInsert(nums, target): 
     return lowerbound(nums, target)

nums=list(map(int, input("enter the elements=").split()))
print(nums)
target=int(input("enter the targeted no.="))
print("the inserted element index should be=",searchInsert(nums, target))
        