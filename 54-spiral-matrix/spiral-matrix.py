class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        n = len(matrix)
        m = len(matrix[0])

        left = 0
        right = m - 1

        top = 0
        bottom = n - 1
        arr1 = []


        while top <= bottom and left <= right:
            for i in range(left, right + 1):
                arr1.append(matrix[top][i])
            top += 1
            for i in range(top, bottom + 1):
                arr1.append(matrix[i][right])
            right -= 1
            if top <= bottom:
                for i in range(right, left - 1, -1 ):
                    arr1.append(matrix[bottom][i])
            bottom -= 1
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    arr1.append(matrix[i][left])
            left += 1          
        return arr1          