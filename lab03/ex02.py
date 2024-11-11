from typing import List

def findWords(words: List[str]) -> List[str]:
    us_keyboard = [frozenset("qwertyuiop"), frozenset("asdfghjkl"), frozenset("zxcvbnm")]
    result = list()
    for word in words:
        if any(set(word.lower()).issubset(row) for row in us_keyboard):
            result.append(word)

    return result

print(findWords(["adsdf","sfd"]))