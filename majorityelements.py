def majorityElement(nums):
        n=len(nums)
        freq={}
        k=n//2
        for i in nums:
            if i not in freq:
                freq[i]=1
            else:
                freq[i]+=1
        
        for key,value in freq.items():
            if value>k:
                return key
            
nums=[2,3,2,2,1,3,2,1,2]
print("the majority element is= ",majorityElement(nums))
                


        