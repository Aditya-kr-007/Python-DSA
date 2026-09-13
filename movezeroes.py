def moveZeroes(nums):
        n=len(nums)
        start=0
        for i in range(n):
            if nums[i]!=0:
                #swap
                temp=nums[start]
                nums[start]=nums[i]
                nums[i]=temp
                start+=1
        return nums

nums=[0,2,0,3,0,4]
print(moveZeroes(nums))