class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        
        # getting letter frequency of each word
        # groups words where key is freq of letters
        # value is words of that frequency
        letters_freq = {}
        for word in strs:
            letters_dict = {}
            for i in word:
                letters_dict[i] = letters_dict.get(i, 0) + 1
            key = frozenset(letters_dict.items())
            letters_freq.setdefault(key,[]).append(word)
        result = []
        for elem in letters_freq.values():
            result.append(elem)

        return result


            
            

            