class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #[-4,-1,-1,0,1,2] after sorting 
        ## i = -1 target = 1 j = -1, k = 2
        ans_set = set()
        nums.sort()
        i = 0
        j = 1
        k = len(nums) - 1

        while(i < len(nums) - 2): 
            if(j >= k):
                i+= 1 
                j = i+1
                k = len(nums) - 1
                continue

            target = -nums[i]
            if(target < nums[j] + nums[k]): 
                k -= 1
            elif (target > nums[j] + nums[k]): 
                j += 1
            else: 
                ans_set.add((nums[i], nums[j], nums[k]))
                j += 1
                k -= 1
        return [list(triplet) for triplet in ans_set]




