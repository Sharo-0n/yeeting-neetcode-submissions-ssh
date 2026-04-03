class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # [1,2,3,4], 
        #  l.    r
        # l + r = target return idx of l and r
        # if target < r then r--
        # else if target > r, then l++ 
        l = 0
        r = len(numbers) - 1

        while l < r:
            cur_sum = numbers[l] + numbers[r]
            if cur_sum == target:
                return [l + 1, r + 1]
            elif cur_sum > target:
                r = r - 1
            elif cur_sum < target:
                l = l + 1
        return []
