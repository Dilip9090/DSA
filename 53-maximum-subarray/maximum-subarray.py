class Solution(object):
    def maxSubArray(self, nums):
        maxi = float('-inf')
        sum1 = 0
        n = len(nums)

        for i in range(n):
            sum1 += nums[i]

            if sum1 > maxi :
                maxi = sum1
            if sum1 <= 0:
                sum1 = 0
        return maxi        
        
        
        
        # #2 Batter
        # maxi = float('-inf')
        # n = len(nums)

        # for i in range(n):
        #     sum1 = 0
        #     for j in range(i,n):
        #         sum1 += nums[j]
        #         maxi = max(sum1,maxi)
        # return maxi             

        
        
        
        #1 brute force
        # maxi = float('-inf')
        # n = len(nums)

        # for i in range(n):
        #     for j in range(i,n):
        #         sum1 = 0
        #         for m in range(i,j+1):
        #             sum1 += nums[m]
        #         maxi = max(sum1,maxi)
        # return maxi             

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # n = len(nums)
        # ans = nums[0]
        # cur_sum = 0
        # for i in nums:
        #     cur_sum+=i
        #     if cur_sum>ans:
        #         ans = cur_sum
        #     if cur_sum<0:
        #         cur_sum=0

        # return ans               





        """
        :type nums: List[int]
        :rtype: int
        """
        