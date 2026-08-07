class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        mpp = {0: 1}
        count = 0
        presum  = 0

        for num in nums:
            presum += num
            find = presum - k
            if find in mpp:
                count += mpp[find]

            if presum in mpp:
                mpp[presum] += 1
            else:
                mpp[presum] = 1
        return count                