class CombinationIterator:

    def __init__(self, char: str, ll : int):
        self.comb = []
        visited = set()
        
        def generate(index , s):
            if index == len(char) :
                return 
            if len(s) == ll:
                self.comb.append(s)
                
            for i in range(index ,len(char)):
                if char[i] in visited :
                    continue
                visited.add(char[i])
                generate(i , s + char[i])
                visited.remove(char[i])
        
        generate(0 , "")
        self.comb.sort();
        self.c = -1 

    def next(self) -> str:
        self.c += 1
        return self.comb[self.c]

    def hasNext(self) -> bool:
        
        if self.c >= len(self.comb)-1:
            return False
        return True


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()