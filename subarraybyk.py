def subarraySum(nums,k):

        freq = {0:1}
        curr_sum=0
        count = 0

        for i in nums:
            curr_sum = curr_sum +  i
            
            if curr_sum - k in freq:
                count += freq[curr_sum-k]
            
            if curr_sum in freq:  #AVOID COUNT DUPLICATION
                freq[curr_sum] += 1
            else:
                freq[curr_sum] = 1

          
        return count

nums=[1,1,2,3,4,-2,1]
k=2
print(subarraySum(nums,k))
        
            