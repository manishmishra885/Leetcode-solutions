class Solution:
    def romanToInt(self, s: str) -> int:
        value= {
            "I":1,
            "V":5,
            "X": 10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        res = 0 
        for i in range(len(s)) :
            if i < (len(s)-1) and value[s[i]] < value[s[i+1]]:
                # yaha pr i < len(s)-1 isliye kiya , to avoid arrayindexOutOfBound Error
                res -= value[s[i]]
            else:
                res += value[s[i]]
        return res