class Trie:
    class Node:
        def __init__(self):
            self.count = 0
            self.children = [None] * 26  # 'a' to 'z'

    def __init__(self):
        self.root = self.Node()

    def insert(self, s):
        cur = self.root
        for ch in s:
            idx = ord(ch) - ord("a")
            if cur.children[idx] is None:
                cur.children[idx] = self.Node()
            cur = cur.children[idx]
            cur.count += 1

    def query(self, s):
        cur = self.root
        for ch in s:
            idx = ord(ch) - ord("a")
            if cur.children[idx] is None:
                return 0
            cur = cur.children[idx]
        return cur.count
