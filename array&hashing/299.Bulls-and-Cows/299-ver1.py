from collections import Counter


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        cow = 0
        bull = 0
        lookup = Counter(secret)

        for i in range(len(guess)):
            if guess[i] == secret[i]:
                bull += 1
                lookup[guess[i]] -= 1

        for i in range(len(guess)):
            if guess[i] in lookup and guess[i] != secret[i] and lookup[guess[i]] > 0:
                cow += 1
                lookup[guess[i]] -= 1

        # print(bull, cow, flag)
        return str(bull) + "A" + str(cow) + "B"
