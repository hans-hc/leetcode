class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {} #mapping charCount to the list of Anagrams

        for s in strs:
            count = [0] * 26 #a...z
            for c in s:
                count[ord(c) - ord("a")] += 1
            key = tuple(count)
            if key in result:
                result[key].append(s)
            else:
                result[key] = [s]
        
        return list(result.values())