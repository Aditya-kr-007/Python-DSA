
def productExceptSelf(nums):
        n = len(nums)              # store length of nums array
        res = [0] * n              # create result array of same size, filled with 0

        pre = 1                    # pre stores product of all elements on the left side
        for i in range(n):         # loop from left to right
            res[i] = pre           # store product of all numbers before index i
            pre *= nums[i]         # update pre by multiplying current number

        suf = 1                    # suf stores product of all elements on the right side
        for i in range(n - 1, -1, -1):   # loop from right to left
            res[i] *= suf                # multiply current result with product of right side
            suf *= nums[i]               # update suf by multiplying current number

        return res                # return final answer array

nums=list(map(int,input("enter the numbers=").split()))
print("the input array=",nums)
print("the product except self =",productExceptSelf(nums))
    