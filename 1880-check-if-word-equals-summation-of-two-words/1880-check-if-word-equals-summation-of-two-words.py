class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        num1 = "" 
        
        for i in range(len(firstWord)):
            num1 += str(ord(firstWord[i]) - ord ( "a"))
            
        
        num2 = ""
        for i in range(len(secondWord)):
            num2 += str(ord(secondWord[i]) - ord ( "a"))
        
        num3 = ""
        for i in range(len(targetWord)):
            num3 += str(ord(targetWord[i]) - ord ( "a"))
            
        if int(num3) == int(num2) + int(num1):
            return True
        return False