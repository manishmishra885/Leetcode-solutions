class Solution:
    def frequencySort(self, s: str) -> str:
        result = ""
        #hasing basic code 
        hashmap={}
        for ch in s:
            hashmap[ch] = hashmap.get(ch,0) + 1

        sorted_char = sorted(hashmap.items(), key = lambda x:x[1], reverse = True)
            #this line will generate the list of (key,value) pair 

        for ch,freq in sorted_char:
                result += ch*freq
        return result
