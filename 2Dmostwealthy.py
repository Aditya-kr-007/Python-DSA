from typing import List
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ans=0
        for account in accounts:
            ans=max(ans,sum(account))
        return ans
rows = int(input("enter rows: "))
cols = int(input("enter columns: "))
matrix = []
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)
print(matrix)
print("The most wealthy account has",Solution().maximumWealth(matrix))


