class Solution:

    def isPalindrome(self, s: str) -> bool:
       alpha = "abcdefghijklmnopqrstuvwxyz"
       end = len(s)-1
       start = 0
       sLower = s.lower()
       while start != end:
           for start in range(len(sLower)):
                if sLower[start] not in alpha:
                    start =+ 1
                    print(sLower[start])
                if sLower[end] not in alpha:
                    end =- 1
                    print(sLower[end])
                if sLower[start] == sLower[end]:
                    end =- 1
                    start =+ 1
                else :
                    return False
       return True


#ideas to handles caps:
#make a copy of the string to be lower case
#use hashmap? if key == value.lower() and etc
