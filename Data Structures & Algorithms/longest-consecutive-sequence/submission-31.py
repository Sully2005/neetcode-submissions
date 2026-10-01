class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        #[-1,-1,0,3,4,5,6,7,8,9]
        #[2,3,4,4,5,10,20]
        count = 1
        max_count = 1
        for i in range(1, len(nums)): 
            if(nums[i] == nums[i-1]): 
                continue
            elif (nums[i] == (nums[i-1] + 1)):
                count += 1
            else: 
                count = 1
            if(count > max_count): 
                    max_count = count
        return max_count
            
            