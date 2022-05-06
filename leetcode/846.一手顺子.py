#
# @lc app=leetcode.cn id=846 lang=python3
#
# [846] 一手顺子
#

# @lc code=start
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        hand.sort()
        cnt = Counter(hand)
        for h in hand:
            if cnt[h] == 0:
                continue  # h这张牌已经不存在了
            for need in range(h, h + groupSize):
                if cnt[need] == 0:
                    return False
                else:
                    cnt[need] -= 1
        return True
# @lc code=end

