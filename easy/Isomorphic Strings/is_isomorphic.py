class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_letters = {}
        for count, letter in enumerate(s):
            if (letter not in s_letters):
                if(t[count] not in list(s_letters.values())):
                    s_letters[letter] = t[count]
                else:
                    if (t[count] in list(s_letters.values())):
                        return False
            elif (letter in s_letters):
                if (t[count] != s_letters[letter]):
                    return False
        return True