def missingNumber(nums):
        n=len(nums)
        freq={}
        for i in range(n+1):
            freq[i]=1
        for i in nums:
            if i in freq.keys():
                freq[i]-=1
        for key,value in freq.items():
            if value==1:
                return key

nums=[0,1,2,3,5]
print(nums)
print("the missing value is",missingNumber(nums))

        
        


                
        
    




