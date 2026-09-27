class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zeroes = 1, 0

        for num in nums: 
            if num == 0: 
                zeroes += 1
            else:
                prod *= num

        if zeroes > 1: return [0] * len(nums)

        result = [0] * len(nums)

        for i , c in enumerate(nums): 
            if c == 0: 
                result[i] = prod
            else: 
                if zeroes == 1: 
                    result[i] = 0
                else: 
                    result[i] = prod // c

        return result