class Trie:

    def __init__(self):
        self.head = {}

    def insert(self, word: str) -> None:
        curr = self.head

        for w in word:
            if w not in curr:
                curr[w] = {}
            curr = curr[w]
        curr['*'] = True

    def search(self, word: str) -> bool:
        curr = self.head

        for w in word:
            if w not in curr:
                return False
            curr = curr[w]

        if '*' in curr:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        curr = self.head

        for w in prefix:
            if w not in curr:
                return False
            curr = curr[w]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
