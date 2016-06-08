class Trie(object):
    def __init__(self):
        self.entry = ""
        self.children = {}

    def find(self, s):
        node = self
        for c in s:
            if c in node.children.keys():
                node = node.children[c]
            else:
                return None
        return node

    def insert(self, s):
        node = self
        i = 0
        l = len(s)
        for c in s:
            if c in node.children.keys():
                node = node.children[c]
                i += 1
            else:
                break;

        while i < l:
            node.children[s[i]] = Trie()
            node = node.children[s[i]]
            i += 1
        node.entry = s

    def getWord(self):
        return self.entry

    def findAllWords(self):
        words = []
        if self.entry != "":
            words.append(self.entry)
        for n in self.children.values():
            words += n.findAllWords()

        return words

    def getSuggestions(self, s):
        node = self.find(s)
        suggestions = []
        if node:
            suggestions = node.findAllWords()

        return suggestions

#Converts text file to list of words
def parseTextFile(filePath):
    inputFile = open(filePath, 'r')
    words = inputFile.read().split("\n")
    inputFile.close()
    return [w for w in words if w]
