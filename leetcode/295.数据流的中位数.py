#
# @lc app=leetcode.cn id=295 lang=python3
#
# [295] 数据流的中位数
#


# @lc code=start
class MedianFinder:
    def __init__(self):
        self.max_h = []
        self.min_h = []
        heapify(self.max_h)
        heapify(self.min_h)

    def addNum(self, num: int) -> None:
        heappush(self.min_h, num)  # 先放入小顶堆 再放入大顶堆 保证 小顶堆元素逗比大顶堆大
        heappush(self.max_h, -heappop(self.min_h))
        if len(self.min_h) < len(self.max_h):  # 保证小顶堆最多比大顶堆多一个元素或相等
            heappush(self.min_h, -heappop(self.max_h))

    def findMedian(self) -> float:
        if len(self.min_h) == len(self.max_h):
            return (-self.max_h[0] + self.min_h[0]) / 2
        else:
            return self.min_h[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end
