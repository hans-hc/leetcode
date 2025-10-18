class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashmapS = {}
        hashmapT = {}
        for letter in s:
            hashmapS[letter] = hashmapS.get(letter, 0) + 1
        for letter in t:
            hashmapT[letter] = hashmapT.get(letter, 0) + 1
        
        return hashmapS == hashmapT
