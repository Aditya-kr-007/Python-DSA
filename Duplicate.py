
def containsDuplicate(nums):
        set1=set(nums)
        if len(nums)==len(set1):
            return False
        else:
            return True
nums=[1,2,3,4,1,2]
print(nums)
print("contains duplicate=",containsDuplicate(nums))
        
                
