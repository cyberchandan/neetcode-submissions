
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}

        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1

        dic2 = dict(sorted(
            dic.items(),
            key=lambda item: item[1],
            reverse=True
        ))

        maxFreq = []

        for key in dic2:
            maxFreq.append(key)
            if len(maxFreq) == k:
                break

        return maxFreq
