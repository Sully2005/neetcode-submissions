class Solution:
    def maxArea(self, heights: List[int]) -> int:
        j = len(heights) - 1
        i = 0
        max_vol = 0

        while(i != j) :
            base = j - i
            height = min(heights[i],heights[j])
            max_vol = max(max_vol, height*base)

            if(heights[i] < heights[j]): 
                i += 1
            else: 
                j -= 1
        return max_vol


