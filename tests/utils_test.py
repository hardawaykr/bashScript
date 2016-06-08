import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import pytest
from bashScript.utils import Trie, parseTextFile

def test1():
    trie = Trie()
    trie.insert("test")
    assert(trie.find("test").getWord() == "test")

def test2():
    trie = Trie()
    words = parseTextFile("bashScript/keywords.txt")
    assert("pwd" in words)
    assert("alias" in words)
    assert("shortcut" in words)
    assert("export" in words)
    assert("ls" in words)
    assert("mv" in words)
    assert("" not in words)
    for w in words:
        trie.insert(w)
    for w in words:
        assert(trie.find(w).getWord() == w)
    assert(not trie.find("adkfjhasdfh"))
    assert(not trie.find("asdfhalivoioniodfio897(34)"))
    assert(set(trie.findAllWords()) == set(words))

def test3():
    trie = Trie()
    words = parseTextFile("bashScript/keywords.txt")

    for w in words:
        trie.insert(w)

    assert(set(trie.getSuggestions('sh')) == set(['shortcut', 'shell']))
