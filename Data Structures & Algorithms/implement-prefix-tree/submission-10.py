class trieNode: 
    def __init__(self):
        self.children = {}
        self.end = False

class PrefixTree:
    def __init__(self):
        self.root = trieNode()
        

    def insert(self, word: str) -> None:
        current = self.root
        for c in word: 
            if c not in current.children: 
                current.children[c] = trieNode()
            current = current.children[c]
        current.end = True
            

    def search(self, word: str) -> bool:
        current = self.root
        for c in word: 
            if c not in current.children: 
                return False
            current = current.children[c]
        if current.end == True: 
            return True
        else: 
            return False
        

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for c in prefix: 
            if c not in current.children: 
                return False
            current = current.children[c]

        return True

        
        