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
