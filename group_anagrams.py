class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_word = {}
        
        if strs is None:
            return [""]
        elif len(strs) <= 1:
            return [strs]
        else:
            for word in strs:

                sorted_str = ''.join(sorted(word))
               
                if sorted_str in sorted_word:
                    sorted_word[sorted_str].append(word)
                else:
                    sorted_word[sorted_str] = [word]
            return sorted_word.values()
            