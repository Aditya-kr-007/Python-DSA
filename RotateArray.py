
def rotate(nums,k):
        n = len(nums)
        k = k % n
        
        reverse(nums,0, n - 1)
        reverse(nums,0, k - 1)
        reverse(nums,k, n - 1)
        return nums
    
def reverse(nums, left: int, right: int):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

nums=list(map(int,input("enter the array= ").split()))
print(nums)
k=int(input("enter k= "))
print("the array rotated by k is",rotate(nums,k))