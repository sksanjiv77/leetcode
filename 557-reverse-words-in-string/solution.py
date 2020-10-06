class Solution:
    def reverseWords(self, s: str) -> str:
        ss = s.split(" ")
        output = []
        for w in ss:
            output.append(self.reverseWord(w))
        return " ".join(output)
            
            
    def reverseWord(self, w):
        ww = list(w)
        l, r = 0, len(ww)-1
        
        while(l<r):
            ww[l], ww[r] = ww[r], ww[l]
            l += 1
            r -= 1
        return "".join(ww)

        