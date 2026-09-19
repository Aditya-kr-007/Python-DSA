def maxProduct(nums):
        curr_max = nums[0]
        curr_min = nums[0]
        ans = nums[0]

        for num in nums[1:]:
            if num < 0:
                curr_max, curr_min = curr_min, curr_max

            curr_max = max(num, curr_max * num)
            curr_min = min(num, curr_min * num)

            ans = max(ans, curr_max)

        return ans
nums=[2,4,1,-3,2,-2,10]
print(nums)
print(maxProduct(nums))