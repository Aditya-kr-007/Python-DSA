def sortArray(nums):
        n=len(nums)
        for i in range(n):
            min=nums[i]  #initialize a variable min to the current element at index i
            index=i      #initialize a variable index to the current index i
            for j in range(i+1,n): 
                if nums[j]<min:
                    min=nums[j]  #update min to the new minimum value found at index j
                    index=j     #update index to the new index j where the minimum value was found
            
            temp=nums[i]          
            nums[i]=nums[index]  #move the minimum value found to the current index i
            nums[index]=temp
                
        
        return nums
nums=list(map(int,input(
     "Enter the elements of the array separated by space: ").split()))
print("the sorted array is ",sortArray(nums))