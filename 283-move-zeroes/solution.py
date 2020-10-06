class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0,0
        # for num in nums:
        #     if num > 0:
        #         r = nums.index(num)
        #         break
        #for i in range(len(nums)-1):
        while(r <= len(nums)-1 and l<= len(nums)-1):
            if nums[l] !=0:
                l += 1
                continue
            if nums[r]==0:
                r += 1
                continue
            
            if l<r:
                nums[l], nums[r] = nums[r], nums[l]
            #print(nums)

            if nums[l] != 0:
                l += 1
            
            #if nums[r] == 0:
            r += 1
            
