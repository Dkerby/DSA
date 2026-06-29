class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}        

        # get the counts of each element
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        
        # create an array of buckets with size n 
        buckets = [ [] for _ in range(len(nums) + 1)]

        # put the numbers into the corresponding frequency buckets
        for num, count in hashmap.items():
            buckets[count].append(num)

        result = []
        # loop through the buckets backwards (to find the highest k frequent numbers))
        for i in range(len(buckets) - 1, 0, -1):
            # loop through the numbers in the buckets, in case there are multiple
            # numbers with the same frequency
            for num in buckets[i]:
                result.append(num)

            # when the length of the result hits k, return
            if len(result) == k:
                return result