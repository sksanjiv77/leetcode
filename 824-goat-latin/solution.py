class Solution:
    def toGoatLatin(self, S: str) -> str:
        #count =0
        words = S.split()
        res = []
        for idx, word in enumerate(words):
            #count+=1
            if word[0].lower() in ['a','e','i','o','u']:
                res.append(word+"ma"+"a"*(idx+1))
            else:
                res.append(word[1:]+word[0]+"ma"+"a"*(idx+1))
        res =" ".join(res)     
        return res
    
    
    
