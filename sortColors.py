def sortColors(nums):
        left=0
        right = len(nums)-1
        i=0
        while i<=right:
            if nums[i]==1:
                i+=1
            elif nums[i]==0:
                temp=nums[i]        #SWAP
                nums[i]=nums[left]
                nums[left]=temp
                i+=1
                left+=1
            else:
                temp=nums[i]        #SWAP
                nums[i]=nums[right]
                nums[right]=temp
                right-=1
        return nums
nums=list(map(int,input("enter the 0,1 or 2's only= ").split()))
print(sortColors(nums))
