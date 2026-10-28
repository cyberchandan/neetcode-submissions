class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap = {}
        for num in nums:
            if num not in hashmap:
                 hashmap[num]=1

           
        longest=0
        for num in hashmap:
            if num-1 not in hashmap:
                current = num 
                count=1

                while current + 1 in hashmap:

                    current +=1
                    count +=1
                
          
                longest=max(count,longest)
        
        return longest