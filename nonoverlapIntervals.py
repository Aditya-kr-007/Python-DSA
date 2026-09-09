"""
Example 1:
Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
"""

def eraseOverlapIntervals(intervals):
        intervals.sort(key = lambda x: x[1])
        n = len(intervals)
        prev=0
        count=1
        for i in range(1,n):
            if intervals[i][0]>=intervals[prev][1]:
                count+=1
                prev=i
        return n-count

n = int(input("Enter number of intervals: "))
intervals = []
for i in range(n):
    while True:
        row = list(map(int, input("Enter 2 values: ").split()))

        if len(row) == 2:
            intervals.append(row)
            break
        else:
            print("Please enter exactly 2 values.")
print(intervals)

print(eraseOverlapIntervals(intervals))