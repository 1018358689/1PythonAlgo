#
# @lc app=leetcode.cn id=506 lang=python
#
# [506] 相对名次
#

# @lc code=start
class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        helper = {1: 'Gold Medal', 2: 'Silver Medal', 3: 'Bronze Medal'}
        score_index = {v: k for k, v in enumerate(score)}  # score-index
        rank = sorted(score, reverse=True)  # 成绩从大到小排序
        res = [0] * len(score)  # 存放获奖结果
        for i, r in enumerate(rank, 1):
            if i in helper:
                res[score_index[r]] = helper[i]  # 根据score-index找到原始索引并放入res
            else:
                res[score_index[r]] = str(i)
        return res
# @lc code=end

