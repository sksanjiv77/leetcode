class Solution:
    def reverseWords(self, s: str) -> str:
        S = s.split()
        l, r = 0, len(S)-1
        SS = ""
        while(l<r):
            S[l], S[r] = S[r], S[l]
            l += 1
            r -= 1
        
        SS = " ".join(S)
        return(SS)
    

