def findDisappearedNumbers(nums):
        n=len(nums)
        numbers = set(nums)
        ans= []

        for i in range(1, n + 1):
            if i not in numbers:
                ans.append(i)
        
        return ans
nums=[2,4,1,5,8,3,2,2]
print(nums)
print(findDisappearedNumbers(nums))
    


             
            