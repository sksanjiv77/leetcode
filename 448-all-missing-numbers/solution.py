class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
             if nums[abs(num)-1] > 0:
                #print(num, "->",  nums[abs(num)-1])
                nums[abs(num)-1] = -nums[abs(num)-1]
        #print(nums)
        a = []
        for i in range(len(nums)):
            if nums[i] > 0:
                a.append(i+1)
        return(a)
    
