import heapq
# heapq._heapify_max(listForTree) 
# heapq._heappop_max(maxheap)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # create hashmap k: v :: value: freq O(n)
        hm = {}
        for num in nums:
            hm[num] = hm.get(num, 0) + 1
        print(hm)
        
        # turn this into an array O(n)
        heap_arr = []
        for key in hm.keys():
            heap_arr.append((hm[key],key))

        # implement max heap with key: values :: frequency: value O(n)
        heapq._heapify_max(heap_arr)

        # pop k elements (k log n)
        retList = []
        for i in range(k):
            retList.append(heapq._heappop_max(heap_arr)[1])

        return retList
