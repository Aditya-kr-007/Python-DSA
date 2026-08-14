class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        dict1={}
        for i in range(n):
            rem = target - nums[i]
            if rem in dict1:
                return [dict1[rem],i]
            else:
                dict1[nums[i]]=i
nums=[2,3,1,5,7]
target=9
print(Solution().twoSum(nums,target))