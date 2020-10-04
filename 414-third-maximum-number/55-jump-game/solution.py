class Solution:
    def canJump(self, nums):
        l = len(nums)
        temp_target = l-1
        for i in range(1, l):
            j = l - i - 1
            while j >= 0:
                if j + nums[j] >= temp_target:
                    temp_target = j
                    if j == 0:
                        return True
                    break
                else if j + nums[j] < temp_target and j == 0:
                    return False
                else:
                    j -= 1
            
        return False

if __name__ == '__main__':
    s = Solution()
    print s.canJump([6,5,4,3,2,1,1,0,0])