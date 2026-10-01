class Solution:
    def reverse(self, x: int) -> int:
        if(x < 0): 
            x_s = str(abs(x))
            x_st = list(reversed(x_s))
            x_st.insert(0, '-')
            ans = int(''.join(x_st))
            if(ans < -2**31): 
                return 0
            return ans
        else: 
            x_s = str(abs(x))
            x_st = list(reversed(x_s))
            ans = int(''.join(x_st))
            if( ans > 2**31 - 1): 
                return 0
            return ans