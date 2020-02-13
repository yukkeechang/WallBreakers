s = "Aa"
#missing case:
#"a.b,."

def reverseVowels(s):
    ph = ''  #placeholder
    vp1 = 0 #pointer1, stays with the vowel
    vowels = "aeiouAEIOU"
    newStr = [None] * len(s)
    #convert newStr to finalStr
    finalStr = ''
    #case of [.e]
    if len(s) == 2 :
        if s[0] not in vowels or s[1] not in vowels:
            return s
        if s[0] and s[1] in vowels:
            newArr = [None]*2
            newArr[0] = s[1]
            newArr[1] = s[0]

            print(newArr)
            return finalStr.join(newArr)
    for letter in range(len(s)):
        if s[letter] in vowels :
            #first vowel
            if ph == '' :
                #set placeholder to first vowel
                ph = s[letter]

                #insert empty space for now
                newStr[letter] = ''

            else :
                #replace current vowel with the placeholder
                newStr[letter]=ph

                #set placeholder to current vowel
                ph = s[letter]

                #set newStr at vp1 with new placeholder aka current vowel
                newStr[vp1] = ph

                ph = newStr[letter]
            #move both pointers to current vowel
            vp1 = letter
            print("new str after inserting vowel: ", newStr)

        #non-vowels get appended to new str
        if s[letter] not in vowels :
            newStr[letter] = s[letter]

            print("new str after inserting consonant: ", newStr)

    return finalStr.join(newStr)

reverseVowels(s)
print(reverseVowels(s))
