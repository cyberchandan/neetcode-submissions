class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap = {}

        for n in nums:
            if n not in hashmap:
                hashmap[n] = 1

        longest = 0

        for n in hashmap:
            if n - 1 not in hashmap:
                current = n
                count = 1

                while current + 1 in hashmap:
                    current += 1
                    count += 1

                longest = max(longest, count)

        return longest