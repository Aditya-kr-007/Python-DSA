class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        left=0
        right=n-1
        while(left<right):
            sum = numbers[left]+numbers[right]
            if sum==target:
                return [left+1,right+1]
            elif sum>target:
                right-=1
            else:
                left+=1
numbers=[2,3,4,5,6,8,9]
target=12
print(Solution().twoSum(numbers,target))

            
                
            
