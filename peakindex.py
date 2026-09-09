"""
Peak Index in a Mountain Array
You are given an integer mountain array arr of length n where the values increase to a peak element and then decrease.
Return the index of the peak element.

Your task is to solve it in O(log(n)) time complexity.
Example 1:
Input: arr = [0,1,0]
Output: 1

Example 2:
Input: arr = [0,2,1,0]
Output: 1
"""
def peakIndexInMountainArray(nums):
        n=len(nums)
        l=0
        r=n-2
        ans=n-1

        while l<=r:
            mid=(l+r)//2
            if nums[mid]<nums[mid+1]:
                #right side got peak element
                l=mid+1
            else:
                ans=mid
                #left side
                r=mid-1
        return ans

nums=[2,5,9,12,7,6]
print(nums)
print("the peak index is ",peakIndexInMountainArray(nums))
