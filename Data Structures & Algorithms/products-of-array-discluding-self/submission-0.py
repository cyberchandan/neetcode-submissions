
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        result = []
        zeroCount = nums.count(0)

        for num in nums:
            if num != 0:
                product *= num

        for i in range(len(nums)):
            if zeroCount > 1:
                result.append(0)
            elif zeroCount == 1:
                if nums[i] == 0:
                    result.append(product)
                else:
                    result.append(0)
            else:
                result.append(product // nums[i])

        return result
