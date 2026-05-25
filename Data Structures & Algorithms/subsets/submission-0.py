class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # start with the empty set
        arr = [[]]

        # loop over all of the numbers in the list of numbers 
        for i in range(len(nums)):
            # look at all of the items currently in the list, and add the new number onto each of them 
            for j in range(len(arr)):
                if(arr[j] != None and nums[i] != None):
                    arr.append(arr[j] + [nums[i]])

        return arr
