from ast import List
import collections


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        wordGraph = collections.defaultdict(list)
        wordList.append(beginWord)

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                wordGraph[pattern].append(word)

        visit = set([beginWord])
        q = collections.deque([beginWord])
        res = 1

        while q:
            # print(q)
            for j in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i + 1:]
                    neighbors = wordGraph[pattern]

                    for nei in neighbors:
                        if nei not in visit:
                            visit.add(nei)
                            q.append(nei)
                            # print(q, visit)
            res += 1
        return 0
