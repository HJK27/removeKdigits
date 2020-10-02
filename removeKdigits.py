class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        removed = 0
        while "0" in num and len(num[:num.index("0")]) <= k-removed:
            removed += len(num[:num.index("0")])
            num = num[num.index("0")+1:]
            if not num: return "0"
        while removed < k:
            if len(num) == 1: return "0"
            for i in range(len(num)-1):
                if num[i] > num[i+1]:
                    num = num[:i] + num[i+1:]
                    removed += 1
                    break
                elif i == len(num)-2:
                    num = num[:i+1]
                    removed += 1
                    break
        return num