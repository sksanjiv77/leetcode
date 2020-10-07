class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last = m+n-1
        m, n = m-1, n-1
        # if len(nums1) == 1 and len(nums2) == 1:
        #     nums1[0] = nums2[0]
        while (n>=0 and m>=0):
            if nums1[m] > nums2[n]:
                nums1[last] = nums1[m]
                m -= 1
            else:
                nums1[last] = nums2[n]
                n -= 1
            last -= 1
        for j in range(n+1):
            nums1[j]=nums2[j]
    
    
