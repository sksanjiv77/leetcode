class Solution:
    def canJump(self, nums):
        l = len(nums)
        if l < 2: return True
        temp_target = l-1
        for i in range(1, l):
            j = l - i - 1
            while j >= 0:
                if j + nums[j] >= temp_target:
                    temp_target = j
                    if j == 0:
                        return True
                    break
                elif j + nums[j] < temp_target and j == 0:
                    return False
                else:
                    j -= 1
            
        return False


