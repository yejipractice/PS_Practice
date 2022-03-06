class Trie:
    def __init__(self):  # 초기화 해줘야 한다.
        self.head = {}

    def add(self, word):
        cur = self.head
        for ch in word:
            if ch not in cur:
                cur[ch] = {}
            cur = cur[ch]
        cur["*"] = True

    def search(self, word):
        cur = self.head

        for ch in word:
            if ch not in cur:
                return False
            cur = cur[ch]
        if '*' in cur:
            return True
        else:
            return False


for tc in range(1, int(input())+1):
    dic = Trie()
    n, m = map(int, input().split())
    a = set()
    b = set()
    for _ in range(n):
        a.add(input())
    for _ in range(m):
        dic.add(input())
    count = set()
    for word in a:
        for idx in range(1, len(word)+1):
            w = word[:idx]
            if dic.search(w):
                count.add(w)
    print("#"+str(tc), end=" ")
    print(len(count))
