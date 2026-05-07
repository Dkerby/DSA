class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low = 0;
        curr = 0;
        high = len(nums) - 1;

        # implement single-pass solution (Dutch flag algorithm)
        # loop until the current pointer passes the high pointer
        while curr <= high:
            # if we see a zero, swap it to the next place in the low section,
            # then bump the low pointer and the current pointer
            if nums[curr] == 0:
                tmp = nums[low]
                nums[low] = nums[curr]
                nums[curr] = tmp
                low += 1
                curr += 1
            # if we see a 1, then just keep it where it is an look at the
            # next value in the list
            elif nums[curr] == 1:
                curr += 1
            # if we see a 2, then swap the current value to the high section,
            # then decrement the high pointer. We don't increment curr because
            # we may need to reprocess the element that was just swapped into
            # the spot at the curr pointer
            else:
                tmp = nums[high]
                nums[high] = nums[curr]
                nums[curr] = tmp
                high -= 1