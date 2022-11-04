class Solution:
    def reverseVowels(self, s: str) -> str:
        i =0
        j = len(s)-1
        vow = {'a','e','i','o',"u",'A','E','I','O','U'}
        l = list(s)
        while(i<j):
            if l[i] in vow and l[j] in vow:
                l[i], l[j] = l[j], l[i]
                i += 1
                j -= 1
            elif l[i] in vow and l[j] not in vow:
                j -= 1
            else:
                i += 1
        return "".join(l)
            