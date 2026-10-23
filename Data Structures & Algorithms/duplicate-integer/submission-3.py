
class Solution:
    def hasDuplicate(self, nums):
        dic ={}
        for i in range(len(nums)):
            if(nums[i] not in dic): 
                dic[nums[i]]=1
            elif (nums[i] in dic):
                return True
        return False 
            
       