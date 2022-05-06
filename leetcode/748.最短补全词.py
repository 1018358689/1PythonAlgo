#
# @lc app=leetcode.cn id=748 lang=python3
#
# [748] 最短补全词
#

# @lc code=start
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        need = Counter(re.findall(r'[a-z]', licensePlate.lower()))
        words.sort(key=len)
        for w in words:
            if not need - Counter(w):
                return w
# @lc code=end

