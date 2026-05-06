class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        last = m + n - 1
        # loop while there are still elements in nums2
        while j >= 0:
            # if there are still values nums1, try this case
            if i >= 0 and nums1[i] >= nums2[j]:
                nums1[last] = nums1[i]
                i -= 1
            # otherwise, we can just sequentially copy the values in nums2
            # into nums1, since we know only the smallest elements remain
            else:
                nums1[last] = nums2[j]
                j -= 1
            last -= 1
