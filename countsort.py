def countSort(nums):
    n=len(nums)
    mx=max(nums)        #find the maximum element in the array to determine the size of the frequency array
    freq=[0]*(mx+1)     #initialize a frequency array of size mx+1 with all elements set to 0

    for i in nums:      #iterate through each element in the input array nums
        freq[i]+=1      #increment the frequency count of the element i in the frequency array freq

    nums=[]             
    for i in range(len(freq)):
        while freq[i]>0:
            nums.append(i)
            freq[i]-=1
    return nums

nums=list(map(int,input("enter the elements= ").split()))
print(countSort(nums))