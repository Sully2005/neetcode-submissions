class Solution:
    def firstUniqChar(self, s: str) -> int:
        dictionary = {}
        min_index = float('inf')

        for index, c in enumerate(s): 
            if dictionary.get(c) is None: 
                dictionary[c] = (1, index)
            else: 
                value, i = dictionary[c]
                value += 1
                dictionary[c] = (value, i)

        sorted_by_value = dict(sorted(dictionary.items(), key=lambda item: item[1][0]))

        for key, (value, index) in sorted_by_value.items(): 
            if value == 1: 
                min_index = min(min_index, index)
            

        return min_index if min_index != float('inf') else  -1
