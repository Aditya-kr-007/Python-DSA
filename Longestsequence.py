def longestConsecutive(nums):
        if len(nums)==0:
            return 0
        
        set1=set(nums)
        ans=list(set1)
        ans.sort()
        elements=[]
        count=1
        l=0
        while l<len(ans)-1:
            if ans[l+1]==ans[l]+1:
                count+=1
                l+=1
            else:
                elements.append(count)
                count=1
                l+=1
        elements.append(count)
        
        k=max(elements)
        return k
nums=[2,100,105,106,3,5,7,6,4,99,101]
print(nums)
print(longestConsecutive(nums))

