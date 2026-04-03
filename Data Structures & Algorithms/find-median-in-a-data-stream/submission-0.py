import heapq

class MedianFinder:
    def __init__(self):
        self.small, self.large = [], []

    def addNum(self, num:int) -> None:
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -1 * num)

        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1*val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        return (-1 * self.small[0] + self.large[0])/ 2.0


    # min heap, max heap
    # [1,2,3]
    # 1, 2 in max heap
    # 3 in min heap
    # 2.5 -> 1,2 in max heap and 2.5, 3 in min heap
    # len(max/left) > len(min/right)
    '''
    def __init__(self):
        self.rightMinHeap = []
        self.rightMinHeapLen = 0 # is always equal to or + 1 of maxHeapLen
        self.leftMaxHeap = []
        self.leftMaxHeapLen = 0

    def addNum(self, num: int) -> None:
        if self.rightMinHeapLen == 0:
            heapq.heappush(self.rightMinHeap, num)
            self.rightMinHeapLen += 1
            return
        if self.leftMaxHeapLen == 0:
            heapq.heappush(self.leftMaxHeap, -1 * num)
            self.leftMaxHeapLen += 1
            return
        # add num
        maxLeft = -1 * self.leftMaxHeap[0]
        minRight = self.rightMinHeap[0]

        # if num is less than maxLeft.pop -> put in max left
        if num <= maxLeft:
            heapq.heappush(self.leftMaxHeap)
            self.leftMaxHeapLen += 1

        # if num is gt than minRight.pop -> put in max right
        elif num <= minRight:
            heapq.heappush(self.rightMinHeap)
            self.rightMinHeapLen += 1

        else:
            if self.rightMinHeapLen + 1 <= self.leftMaxHeapLen:
                heapq.heappush(self.rightMinHeap, num)
                self.rightMinHeapLen += 1
            else:
                heapq._heappush_max(self.leftMaxHeap, num)
                self.leftMaxHeapLen += 1

        # check sizes, make sure leftMaxHeapLen is always equal to or + 1 of rightMinHeapLen
        while self.rightMinHeapLen > self.leftMaxHeapLen:
            # pop and push until above rule
            moving = heapq.heappop(self.rightMinHeapLen)
            heapq._heappush_max(self.leftMaxHeapLen, moving)
            self.rightMinHeapLen -= 1        
            self.leftMaxHeapLen += 1        

    def findMedian(self) -> float:
        if self.rightMinHeapLen > self.leftMaxHeapLen:
            return self.rightMinHeap[0]
        else:
            return (self.rightMinHeap[0] + self.leftMaxHeap[0]) / 2.0
    '''
        