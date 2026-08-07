class Solution(object):
    def generate(self, n):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans = []

        for i in range(1, n + 1):
            temp = []
            total = 1
            temp.append(total)
            for j in range(1, i):
                total = total * (i - j)
                total = total // j
                temp.append(total)
            ans.append(temp)
        return ans         
