class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string = ''.join(s).lower()
        new_string = ''.join(ch for ch in new_string if ch.isalnum())
        i = 0
        j = len(new_string) - 1
        while ( i < (len(new_string) // 2)):
            if(new_string[i] != new_string[j]): 
                return False
            i += 1
            j -= 1
        return True
