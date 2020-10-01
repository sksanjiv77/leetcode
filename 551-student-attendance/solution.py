class Solution:
    def checkRecord(self, s: str) -> bool:
        # if "LLL" in s or s.count("A")>=2:
        #     return False
        # return True
        
        count_a = 0
        cont = 0
        for i in range(len(s)):
            if s[i]=="A":
                count_a += 1
                if count_a > 1:
                    return False
            if s[i] == "L":
                cont += 1
                if cont > 2:
                    return False
            else:
                cont = 0
        return True
                    
