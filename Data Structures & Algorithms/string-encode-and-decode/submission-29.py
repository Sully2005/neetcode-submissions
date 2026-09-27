class Solution:

    def encode(self, strs: List[str]) -> str:
        array = list()
        for string in strs: 
            array.append(str(len(string)))
            array.append('#')
            array.append(string)
        return ''.join(array)


    def decode(self, s: str) -> List[str]:
        #each word being with a length
        result = []
        i = 0

        while(i < len(s)): 
            length_str = []

            while i < len(s) and s[i].isdigit(): 
                length_str.append(s[i])
                i+= 1
            i += 1
            length = int(''.join(length_str))

            result.append(s[i:i+length])
            i += length
        return result