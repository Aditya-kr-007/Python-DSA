def merge(nums1,nums2,m, n):
        """
        Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
        Output: [1,2,2,3,5,6]
        Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
        The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
        """
        i=m-1
        j=n-1
        k=m+n-1
        while j>=0:
            if i<0 or nums2[j]>nums1[i]:
                nums1[k]=nums2[j]
                j=j-1
                k=k-1
            else:
                nums1[k]=nums1[i]
                i=i-1
                k=k-1
        return nums1
nums1=[1,2,3,0,0,0]
m=3
n=3
nums2=[2,5,6]
print(merge(nums1,nums2,m,n))

        