class Solution:
    def lengthOfLastWord(self, s):
        length = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ' ':
                continue
            else:
                for i in range(i, -1, -1):
                    if s[i] == ' ':
                        break
                    length += 1
                return length
        return length
