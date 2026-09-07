def removeDuplicates(nums):
        n=len(nums)
        k=0
        for i in range(1,n):
            if nums[i]!=nums[k]:
                k+=1
                nums[k]=nums[i]
        return k+1, nums[:k+1]
nums=list(map(int,input().split()))
print(removeDuplicates(nums))
