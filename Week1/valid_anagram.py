class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) :
            return False
        sdict = {}
        tdict = {}
        for i in s :
            if i not in sdict :
                sdict[i] = 1
            else :
                sdict[i] += 1
        for i in t :
            if i not in tdict :
                tdict[i] = 1
            else :
                tdict[i] += 1
        print(sdict, tdict)
        if sdict == tdict :
            return True

            
