from typing import List


def kWeakestRows(mat: List[List[int]], k: int) -> List[int]:
    result = [index for index, _ in sorted(enumerate(mat), key=lambda x: sum(x[1]))]
    return result[:k]