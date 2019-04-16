class Trie:

    def __init__(self):
       self.root = {}
        
    def insert(self, word):
        node = self.root
        for letter in word:
            if letter not in node:
                node[letter] = {}
            node = node[letter]
        node['$'] = {} # End of word
        
    def search(self, word):
        node = self.root
        for letter in word:
            if letter in node:
                node = node[letter]
            else:
                return False
        if '$' in node:
            return True
        else:
            return False
        
    def startsWith(self, prefix):
        node = self.root
        for letter in prefix:
            if letter in node:
                node = node[letter]
            else:
                return False
        return True

    def autoComplete(self, prefix):
        node = self.root
        for letter in prefix:
            if letter in node:
                node = node[letter]
            else:
                return []
        words = []
        autocomplete_helper(prefix, words, node)
        return words


def autocomplete_helper(parent, words, node):
    if '$' in node:
        words.append(parent)
    for letter in node:
        print_tree(parent + letter, words, node[letter])
