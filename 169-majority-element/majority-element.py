class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # #1 Brute Force
        # n = len(nums)
        # valu = n/2
        # for i in range(n):
        #     count = 0
        #     for j in range(n):
        #         if nums[i] == nums[j]:
        #             count +=1
        #         if count > valu:
        #             return nums[i]     

        #2 Batter

        n = len(nums)
        mpp = {}

        for num in nums:
            if num in mpp: 
                mpp[num] += 1
            else:
                mpp[num] = 1

            for key in mpp:
                if mpp[key] > n//2:
                    return key             




        # nums.sort()
        # return nums[len(nums) // 2]
        
        


        