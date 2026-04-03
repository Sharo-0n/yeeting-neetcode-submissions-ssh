class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1,2,4,6]
        # [1,1,2,8]
        # [48,24,6,1]
        # l->r O(n)
        lr = [0]*len(nums)
        # first index starts with 1
        lr[0] = 1
        for i in range(1,len(nums)):
            # afterwards, multiply previous position in og arr
            #   and prev position in lr array
            lr[i] = nums[i-1] * lr[i-1]

        # same with r -> 1 O(n)        
        rl = [0]*len(nums)
        rl[len(nums)-1] = 1
        for i in range(len(nums)-2, -1, -1):
            rl[i] = nums[i+1] * rl[i+1]

        # iterate both 1r rl and get resulting array O(n)
        ret_val = []
        for i in range(len(nums)):
            ret_val.append(rl[i]*lr[i])
        return ret_val
        
        