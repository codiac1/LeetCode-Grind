class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        one = {}
        two = {}
        
        for i in range(len(word1)):
            one[word1[i]] = one.get(word1[i] , 0) + 1
            two[word2[i]] = two.get(word2[i] , 0) + 1
            
        for ele in one:
            if ele not in two:
                return False
            
        for ele in two:
            if ele not in one :
                return False
        
        if sorted(one.values()) != sorted(two.values()):
            return False
        return True
        
            
            
        
        
        
            
        