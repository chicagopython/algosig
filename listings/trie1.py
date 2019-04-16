class Node:

    def __init__(self, letter):
        self.letter = letter
        self.children = {}
        self.end = False

class Trie:

    def __init__(self):
        self.root = Node('root')

    def insert(self, word):
        node = self.root
        for letter in word:
            if letter not in node.children:
                node.children[letter] = Node(letter)
            node = node.children[letter]
        node.end = word
        
    def search(self, word):
        node = self.root
        for letter in word:
            if letter in node.children:
                node = node.children[letter]
            else:
                return False
        if node.end:
            return True
        else:
            return False

    def startsWith(self, prefix):
        node = self.root
        for letter in prefix:
            if letter in node.children:
                node = node.children[letter]
            else:
                return False
        return True

    def autocomplete(self, word):
        node = self.root
        for letter in word:
            if letter in node.children:
                node = node.children[letter]
            else:
                return []
        words = []
        autocomplete_helper(node, words)
        return words


def autocomplete_helper(node, words):
    if node.end:
        words.append(node.end)
        return
    for child in node.children:
        autocomplete_helper(node, words)