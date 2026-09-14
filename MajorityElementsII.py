"""
229. Majority Element II
Given an integer array of size n, find all elements that appear more than ⌊n / 3⌋ times.

Example 1:

Input: nums = [3,2,3]
Output: [3]
Example 2:

Input: nums = [1]
Output: [1]
"""

def majorityElement(nums):
        n=len(nums)
        freq={}
        k=n//3
        ans=[]
        for i in nums:
            if i not in freq:
                freq[i]=1
            else:
                freq[i]+=1
        
        for key,value in freq.items():
            if value>k:
                ans.append(key)
        return ans
nums=[2,3,2,2,1,3,2,1,2]
print("the majority element is= ",majorityElement(nums))