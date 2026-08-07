class Solution(object):
    def subarraySum(self, nums, k):
        mpp = {0: 1}
        count = 0
        presum  = 0

        for num in nums:
            presum += num
            remove = presum - k
            if remove in mpp:
                count += mpp[remove]
            if presum in mpp:    
                mpp[presum] += 1
            else:
                mpp[presum] = 1     
        return count    
        
        
        
        
        # n = len(nums)
        # count = 0
        
        # for i in range(n):
        #     for j in range(i, n):
        #         sum1 = 0

        #         for m in range(i, j + 1):
        #             sum1 += nums[m]
                
        #         if sum1 == k:
        #             count += 1
        # return count                



        # count = 0

        # for i in range(len(nums)):
        #     total = 0
        #     for j in range(i, len(nums)):
        #         total += nums[j]
        #         if total == k:
        #             count += 1

        # return count




        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        