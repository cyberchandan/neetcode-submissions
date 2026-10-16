import copy
class Solution:
    def hasDuplicate(self, nums):
        number=copy.deepcopy(nums)
        for n in number:
            if number.count(n)>1 :
                return True
        
        return False