class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = defaultdict()
        array = list()

        for number in nums: 
            if number in dictionary:
                dictionary[number] += 1
            else: 
                dictionary[number] = 1

        sorted_dic = dict(sorted(dictionary.items(), key=lambda item:item [1], reverse=True))
        
        for index, key in enumerate(sorted_dic): 
            array.append(key)
            if(index == k - 1):
                return array
        return array
            