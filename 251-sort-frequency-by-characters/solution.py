class Solution:
    def frequencySort(self, s: str) -> str:
        d = {}
        ss = ""
        for char in s:
            if char not in d:
                d[char] = 1
            else:
                d[char] += 1
        
        sorted_d = sorted(d.keys(), key=lambda x:d[x], reverse=True)
        print(sorted_d)
        
        for char in sorted_d:
            ss += char*d[char]
        return ss        
        
            
            
