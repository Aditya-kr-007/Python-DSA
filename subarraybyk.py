def subarraySum(nums,k):

        freq = {0:1}
        curr_sum=0
        count = 0

        for i in nums:
            curr_sum += i
            
            if curr_sum - k in freq:
                count += freq[curr_sum-k]
            
            freq[curr_sum] = 1 + freq.get(curr_sum, 0)
        
        return count
nums=[1,2,3,4,2,1]
k=3
print(subarraySum(nums,k))
        
            