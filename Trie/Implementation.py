class Node:
    def __init__(self):    
        self.childrenAt=defaultdict(Node)
        self.wordEnd=0


class Trie:
    def __init__(self):
        self.t=Node()

    def add(self, s):
        temp=self.t
        for ch in s:
            temp=temp.childrenAt[ch]
        temp.wordEnd=1

    def exists(self, s):
        temp=self.t

        for ch in s:
            if ch not in temp.childrenAt:return False
            temp=temp.childrenAt[ch]
        return temp.wordEnd>0
        

    def startswith(self, p):
        temp=self.t

        for ch in p:
            if ch not in temp.childrenAt:return False
            temp=temp.childrenAt[ch]
        
        return True
