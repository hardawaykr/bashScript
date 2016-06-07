import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import pytest
from bashScript.utils import Trie

def test1():
    trie = Trie()
    trie.insert("test")
    assert(trie.find("test").getWord() == "test")
