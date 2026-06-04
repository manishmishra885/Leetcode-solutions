class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result =""
        count = 0 
        for ch in s:
            if ch == "(":
                count+=1
                if count>1: # yaha pr check kar rahe hai ki zero nhi hai, count zero nhi hai ! 
                    result += ch # toh result mai add kar diya 
            else:
                count -= 1
                if count>0:
                    result += ch
        return result
        