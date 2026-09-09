
def search(nums,target):
        n = len(nums)
        for i in range(n):
            if nums[i]==target:
                return i
        return -1

nums=list(map(int, input("enter the numbers= ").split()))
print(nums)
target=int(input("enter the target= "))
print(search(nums,target))

