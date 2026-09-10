"""
 Koko Eating Bananas
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.
Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
Return the minimum integer k such that she can eat all the bananas within h hours.

Example 1:
Input: piles = [3,6,7,11], h = 8
Output: 4

Example 2:
Input: piles = [30,11,23,4,20], h = 5
Output: 30
"""
def gethours(piles,mid):
        ans=0
        for pile in piles:
            ans += (pile+mid-1)//mid
        return ans
    
def minEatingSpeed(piles,h):
        l=1 #minimum eating
        r=max(piles)
        k=r
        while l<=r:
            mid =(l+r)//2
            if gethours(piles,mid)>h:
                l=mid+1  #increase eating speed 
            else:
                k=mid   #maybe so check again by reducing r
                r=mid-1 #decrease eating speed
        return k
piles=[30,11,23,4,20]
h=int(input("enter the no. of hours the gaurds are gone="))
print(piles)
print("minimum bananas to eat per hour till all get finished is",minEatingSpeed(piles,h))
