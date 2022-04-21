class Node:
    def __init__(self):
        self.children = {}
        self.isTerminal = False
    

class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert_recur(self, word, root=self.root):
        letter = word[0]
        if letter not in root.children:
            root.children[letter] = Node()        
        # base case here for last insertion
        if len(word) == 1:
            root.children[letter].isTerminal = True
        else:
            self.insert_recur(word[1:], root.children[letter])

    def insert_iter(self, word):
        node = self.root
        
        for i in range(len(word)):
            letter = word[i]
            if letter not in node.children:
                node.children[letter] = Node()
            node = node.children(letter)        
        # set the terminal condition after last letter
        node.isTerminal = True
        
    def search_recur(self, word, root=self.root):
        # base case, word='' case has to be terminal
        if len(word) == 0:
            if root.isTerminal:
                return True
            else:
                return False       
        
        letter = word[0]
        if letter in root.children:
            return self.search_recur(word[1:], root.children[letter])
        else:
            return False

    def search_iter(self, word):
        node = self.root
        
        for i in range(len(word)):
            letter = word[i]
            if letter not in node.children:
                return False
            node = node.children(letter)        
        # return terminal condition after last letter
        return node.isTerminal

    def wordsWithPrefix(self, prefix, root=self.root):
        if len(prefix)==0:
            results = []
            if root.isTerminal:
                results.append('')
            for letter in root.children:
                childNode = root.children[letter]
                suffixs = wordsWithPrefix(prefix, childNode)
                words = [(letter + suffix) for suffix in suffixs]
                results = results.concat(words)
            return results
        else:
            firstLetter = prefix[0]
            childNode = root.children[firstLetter]
            if not childNode:
                return []
            else:
                suffixs = wordsWithPrefix(prefix[1:], childNode)
                words = [(firstLetter + suffix) for suffix in suffixs]
            return words

    def startsWithRecur(self, word, root=self.root):
        # base case, word='' case has to be terminal
        if len(word) == 0:
            return True                   
        letter = word[0]
        if letter in root.children:
            return self.startsWithRecur(word[1:], root.children[letter])
        else:
            return False

    def startsWithIter(self, word):
        node = self.root        
        for i in range(len(word)):
            letter = word[i]
            if letter not in node.children:
                return False
            node = node.children(letter)        
        # return terminal condition after last letter
        return True