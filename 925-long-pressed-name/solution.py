class Solution:
    def isLongPressedName(self, name, typed):
        first, second = 0, 0
        while first < len(name):
            if second > len(typed)-1:
                return False
            if first < len(name) and name[first] == typed[second]:
                first += 1
                second += 1
            else:
                if second == 0:
                    return False
                while(typed[second] == typed[second - 1]):
                    second += 1
                    if second > len(typed)-1:
                        return False
                        
                if name[first] != typed[second]:
                    return False
        #print(first,second)
        while(second < len(typed)):
            if second == len(typed)-1:
                return True
            if typed[second] == typed[second + 1]:
                second += 1  
                continue
            else:
                return False

           
        if first == len(name) and len(typed) == second:
            return True
        else:
            return False
        
        
Method #2
def isLongPressedName(self, name, typed):
        i = 0
        for j in range(len(typed)):
            if i < len(name) and name[i] == typed[j]:
                i += 1
            elif j == 0 or typed[j] != typed[j - 1]:
                return False
        return i == len(name)