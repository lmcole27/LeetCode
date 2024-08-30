strs = ["flower", "flute", "fly"]
# r = len(strs[0])
# n = 0


class Solution():
    ans = ""
    n = 0

    def wordle(self, words):
        r = len(words[0])
        for word in strs:
            if len(word) < r:
                r = len(word)

        while self.n < r:
            for i in range(len(strs)): 
                if strs[i][self.n] != strs[0][self.n]:
                    return self.ans
                self.ans += strs[0][self.n]
                self.n += 1
        return self.ans

ret = Solution().wordle(words = strs)
print(ret)
