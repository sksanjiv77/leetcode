class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1
                
        #print(d)
        sorted_d = sorted(d, key=lambda x:d[x], reverse=True)
        #print(sorted_d)
        return(sorted_d[0])
                
            
        