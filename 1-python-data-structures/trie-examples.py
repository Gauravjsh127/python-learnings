import collections
class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict()
        self.terminating = False
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insertWord(self, word):
        node = self.root
        lword = len(word)
        for i in range(lword):
            ch = word[i]
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.terminating = True

    def searchTrie(self, word):
        node = self.root
        lword = len(word)
        for i in range(lword):
            ch = word[i]
            if ch not in node.children:
                return False
            node = node.children[ch]
        if node is not None and node.terminating is True:
            return True
        return False

    def deleteTrie(self, word):
        print('Delete word : ' + word)
        node = self.root
        lword = len(word)
        for i in range(lword):
            ch = word[i]
            if ch not in node.children:
                print ("Word not found")
                return 0
            node = node.children[ch]
        if not node:
            print("Word not found")
            return -1
        else:
            node.terminating = False
            print("Word Deleted")
            return 0

    def updateTrie(self, old_word, new_word):
        val = self.deleteTrie(old_word)
        if val == 0:
            self.insertWord(new_word)

if __name__ == "__main__":
    strings = ["pqrs", "pprt", "psst", "qqrs", "pqrs"]
    t = Trie()
    for word in strings:
        t.insertWord(word)
    print(t.searchTrie("pqrs"))
    print(t.searchTrie("pprt"))
    print(t.searchTrie("abc"))
    print(t.searchTrie("psst"))
    print(t.searchTrie("pprt"))
    t.deleteTrie("pprt")
    print (t.searchTrie("pprt"))
    t.deleteTrie("abc")
    t.updateTrie("mnop", "pprt")
    print (t.searchTrie("mnop"))
    print (t.searchTrie("pprt"))