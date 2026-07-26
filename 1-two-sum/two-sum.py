class Solution(object):
    def twoSum(self, arr, target):
        nums = []

        for i in range(len(arr)):
            nums.append((arr[i], i))

        nums.sort()

        left = 0
        right = len(nums) - 1

        while left < right:
            sum1 = nums[left][0] + nums[right][0]

            if sum1 == target:
                return [nums[left][1], nums[right][1]]

            elif sum1 < target:
                left += 1

            else:
                right -= 1

        return nums   
        
        
        
        
        # mpp  = {}
        # need = 0

        # for i in range(len(arr)):
        #     need = target - arr[i]
        #     if need in mpp:
        #         return [mpp[need], i]
        #     else:
        #         mpp[arr[i]] = i    

        
        
        
        
        
        # n = len(arr)
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if arr[i] == arr[j]:
        #             continue
        #         if arr[i] + arr[j] == target:
        #             return [i,j]

        
        # seen = {}

        # for i, num in enumerate(nums):
        #     complement = target - num

        #     if complement in seen:
        #         return [seen[complement], i]
        #     seen[num] = i

        # seen = {}
        
        # for i, num in enumerate(nums):
        #     complement = target - num
            
        #     if complement in seen:
        #         return [seen[complement], i]
        #     seen[num] = i




        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        