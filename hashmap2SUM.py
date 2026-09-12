
def twoSum(nums, target):
        n=len(nums)
        hashmap = {}

        for i in range(n):
            complement = target - nums[i]

            if complement in hashmap:
                return [hashmap[complement], i]
            else:
                hashmap[nums[i]] = i     #dict[key]= value
        
        return []

nums=[2,3,4,5,3]
print(nums)
target=8
print("the 2sum indices are",twoSum(nums,target))
