class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ele1, count1 = 0, 0
        ele2, count2 = 0, 0
        n = len(nums)

        for i in range(n):
            if count1 == 0 and nums[i] != ele2:
                ele1 = nums[i]
                count1 = 1
            elif count2 == 0 and nums[i] != ele1:
                ele2 = nums[i]
                count2 = 1
            elif ele1 == nums[i]:
                count1 += 1
            elif ele2 == nums[i]:
                count2 += 1        
            else:
                count1 -= 1
                count2 -= 1 
        count1 = 0
        count2 = 0
        arr = []             
        for i in range(n):          
            if nums[i] == ele1:
                count1 += 1
            elif nums[i] == ele2:
                count2 += 1    

        if count1 > n // 3:
            arr.append(ele1)
        if count2 > n // 3:
            arr.append(ele2)
        return arr   

        # mpp = {}
        # n = len(nums)
        # arr = []

        # for num in nums:
        #     if num in mpp:
        #         mpp[num] += 1
        #     else:
        #         mpp[num] = 1
        #     if mpp[num] > n // 3 and num not in arr:    
        #         arr.append(num)
        # return arr   


        # mpp = {}
        # n = len(nums)
        # arr = []

        # for num in nums:
        #     if num in mpp:
        #         mpp[num] += 1
        #     else:
        #         mpp[num] = 1

        # for key in mpp:
        #     if mpp[key] > n // 3:
        #         arr.append(key)
        # return arr                    


        # arr = []
        # n = len(nums)

        # for i in range(n):
        #     count = 0
        #     for j in range(n):
        #         if nums[i] == nums[j]:
        #             count += 1
        #             if count > n/3 and nums[i] not in arr:
        #                 arr.append(nums[i])
        # return arr                
        
        # count1 = count2 = 0
        # candidate1 = candidate2 = None

        # for num in nums:

        #     if num == candidate1:
        #         count1 += 1

        #     elif num == candidate2:
        #         count2 += 1

        #     elif count1 == 0:
        #         candidate1 = num
        #         count1 = 1

        #     elif count2 == 0:
        #         candidate2 = num
        #         count2 = 1

        #     else:
        #         count1 -= 1
        #         count2 -= 1

        # result = []

        # if nums.count(candidate1) > len(nums) // 3:
        #     result.append(candidate1)

        # if candidate2 != candidate1 and nums.count(candidate2) > len(nums) // 3:
        #     result.append(candidate2)

        # return result
        