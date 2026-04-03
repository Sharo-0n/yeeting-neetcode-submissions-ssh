class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_numbers = set()

        for num in nums:
            if num in unique_numbers:
                return True
            else:
                unique_numbers.add(num)
        
        return False