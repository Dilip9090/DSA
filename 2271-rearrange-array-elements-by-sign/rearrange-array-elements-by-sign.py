class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        arr = [0] * n 
        pos = 0
        neg  = 1

        for i in range(n):
            if nums[i] > 0:
                arr[pos] = nums[i]
                pos += 2
            else:
                arr[neg] = nums[i]
                neg += 2
        return arr            


        
        
        
        # 1 Brute Force Solution
        pos = []
        neg = []
        n = len(nums)
        for i in range(n):
            if nums[i] > 0:
                pos.append(nums[i])
            else:
                neg.append(nums[i]) 
        for i in range(n/2):
            nums[2*i] = pos[i]
            nums[2*i+1] = neg[i]           
        
        return nums                    
       
        