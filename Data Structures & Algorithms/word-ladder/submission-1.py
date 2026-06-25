from collections import defaultdict, deque

def is_edge(a, b):
    assert len(a) == len(b)
    count = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1
        if count > 1:
            return False
    return True

def bfs(node, elem, adj):
    q = deque([])
    vis = defaultdict(bool)
    q.append((node, 1))
    while q:
        cur, level = q.popleft()
        if vis[cur]:
            continue
        vis[cur] = True
        if cur == elem:
            return level
        for child in adj[cur]:
            if not vis[child]:
                q.append((child, level+1))
    return None


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        adj = defaultdict(list)
        for i in [beginWord] + wordList + [endWord]:
            for j in [beginWord] + wordList + [endWord]:
                if i != j:
                    if is_edge(i ,j):
                        adj[i].append(j)
        pathlen = bfs(beginWord, endWord, adj)
        if pathlen is not None:
            return pathlen
        return 0
