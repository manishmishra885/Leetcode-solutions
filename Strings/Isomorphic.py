class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        else:
            mapS_T = {}
            mapT_S = {}
            
            for i in range (len(s)):
                c1 = s[i]
                c2=t[i]
                if c1 in mapS_T:
                    if mapS_T[c1]!=c2:
                        return False
                else:
                    mapS_T[c1]=c2
                
                if c2 in mapT_S:
                    if mapT_S[c2]!=c1:
                        return False
                else:
                    mapT_S[c2]=c1
            return True
                

