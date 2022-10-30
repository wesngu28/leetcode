import abc


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        schar = 0
        tchar = 0
        while (schar < len(s) and tchar < len(t)):
            if (s[schar] == t[tchar]):
                # Only increment if there is a match
                schar += 1
            # This always needs to be incremented.
            tchar += 1
        # We do not need to worry about the relative positions this way. If there is no match, the string will iterate until the end of string t, where the while loop is broken, and 
        # this subsequent if results in a false since it isn't true. If we look at it with the given example ace vs aec in abcde. Index 0 for both is A, but for aec, the loop will continue
        # to the very end of abcde where there is an E, but at this point, there is no more T to go through, but for ace the match is found early enough for it to be true.
        if (schar == len(s)):
            return True
        return False

#         dict = {}
#         for sletter in s:
#             i = 0
#             if (len(dict) > 0):
#                 i = max(list(dict.values()))
#             print(i)
#             while i < len(t):
#                 if(sletter == t[i]):
#                     if (len(dict) > 0):
#                         if (i > max(list(dict.values()))):
#                             dict[sletter] = i
#                         else:
#                             return False
#                     else:
#                         dict[sletter] = i
#                 i += 1
#             if (sletter not in dict):
#                 return False
#         return True
                    