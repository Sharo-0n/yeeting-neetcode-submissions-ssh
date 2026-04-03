class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupSet = set()
        for num in nums:
            if num not in dupSet:
                dupSet.add(num)
            else:
                return True

        return False