"""
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
 In this case, the max area of the container can contain is 49.
"""
def container(nums):
    n=len(nums)
    left=0
    right=n-1
    max_area=0
    while left<right:
        height=min(nums[left],nums[right])
        length= (right-left)
        area=height*length

        max_area=max(max_area,area)  #ANSWER
        if nums[left]<nums[right]:    #SMALLER HEIGHT WILL MOVE AND HIGHER WILL STAY
            left+=1
        else:
            right-=1
    return max_area
nums= [1,8,6,2,5,4,8,3,7]
print(nums)
print("the container with most water area is= ",container(nums))
