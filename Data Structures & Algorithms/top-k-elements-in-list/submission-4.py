class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # store frequency
        # sorted structure (priority queue) -- O(n log n)

        # array of # of items: [[1],[2],[3], [], []]
        # [item exists one time, ... , list of items that exist n times]

        hm = {} # element: frequency
        for num in nums:
            if num in hm:
                hm[num] += 1
            else:
                hm[num] = 1
        freq_list = [[] for _ in range(len(nums) + 1)]
        for key in hm.keys():
            index = hm[key]
            freq_list[index].append(key)

        print(freq_list)
        ret_val = []
        freq_list_idx = len(freq_list) - 1
        while len(ret_val) < k and freq_list_idx > 0:
            idx = 0
            while len(ret_val) < k and idx < len(freq_list[freq_list_idx]):
                ret_val.append(freq_list[freq_list_idx][idx])
                idx += 1
            freq_list_idx -= 1
        return ret_val