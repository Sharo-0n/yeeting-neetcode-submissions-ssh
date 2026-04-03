class Solution:
    def findMin(self, nums: List[int]) -> int:
        # [3,4,5,6,1,2]
        #  ^   ^ ^.  ^
        # when there is win[0] > win[len(win) - 1] --> smallest number is here
        # if win[0] < win[end] and same with other half, then smallest number is first elem

        def helper(nums) -> int:
            print(nums)
            # bc
            if len(nums) == 1:
                return nums[0]
            if len(nums) == 2:
                if nums[0] > nums[1]: 
                    return nums[1]
                else:
                    return nums[0]
            if nums[0] < nums[len(nums) - 1]:
                return nums[0]
            
            midpt = int(len(nums)/2)
            print(midpt)
            if nums[midpt] > nums[len(nums) - 1]:
                return helper(nums[midpt:])
            elif nums[0] > nums[midpt-1]:
                return helper(nums[:midpt])
            elif nums[0] > nums[len(nums) - 1]:
                return helper(nums[midpt:])
        return helper(nums)
