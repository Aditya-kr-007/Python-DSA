
def sortArray(nums):
        
        n=len(nums)
                             #iterate through the array starting from the second element
        for i in range(1,n):
            key = nums[i]    #store the current element in a variable called key
            j = i-1          #initialize a variable j to the index of the previous element
            while j>=0 and nums[j]>key:  
                nums[j+1] = nums[j]       
                j = j-1      #decrement j by 1
            
            nums[j+1]=key    #insert the key at the correct position in the sorted portion of the array
        return nums
nums=list(map(int,input("Enter the elements of the array separated by space: ").split()))
print("the sorted array is ",sortArray(nums))