class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        seen = []
        for char in s:
            if char in seen:
                longest = max(longest, len(seen))
                first_occurence = seen.index(char)
                seen = seen[first_occurence+1:]
                seen.append(char)
            else:
                seen.append(char)
                
        return max(longest, len(seen))
                
            
