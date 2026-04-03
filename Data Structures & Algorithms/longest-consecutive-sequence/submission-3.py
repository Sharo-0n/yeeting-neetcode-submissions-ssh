class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 5, 2, 20, 4, 10, 3
        # map(2:1) (check for 2-1) (check for 2+1)
        # map(2:1; 20:1) (check for 20-1) (check for 20+1)
        # map(2:1; 20:1; 4:1) (check for 4-1) (check for 4+1)
        # map(2:1; 20:1; 4:1; 10:1) ... 
        # map(2:1; 20:1; 4:1; 10:1; 3:2) ... (check for 3-1 ... found 2 +1 to value)
        #   (check for 3+1)-> (4:3) 

        # o(nlogn) sorting and 
        if len(nums) <= 0:
            return 0

        s = set(nums)
        beginnings = []
        # find beginning
        for num in nums:
            # check if num-1 exists
            if not num - 1 in s:
                beginnings.append(num)
        
        max_consec = 1
        for beginning in beginnings:
            curr = beginning
            curr_consec = 1
            while curr + 1 in s:
                curr_consec = curr_consec + 1
                max_consec = max(max_consec, curr_consec) 
                curr = curr + 1
        
        return max_consec