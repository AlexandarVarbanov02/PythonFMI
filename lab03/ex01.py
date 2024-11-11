def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t): return False

    characters = {chr(letter): 0 for letter in range(ord('a'), ord('z') + 1)}
    for c in s:
        characters[c] += 1

    for c in t:
        characters[c] -= 1

    return all(x == 0 for x in characters.values())


print(isAnagram("anagram", "nagaram"))

"""
    Slow solution
    class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        s_list = sorted(list(s))
        t_list = sorted(list(t))
        
        return s_list == t_list
"""