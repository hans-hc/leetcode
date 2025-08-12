class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashsetSeen = set()
        for num in nums:
            if num in hashsetSeen:
                return True
            hashsetSeen.add(num)
        return False
