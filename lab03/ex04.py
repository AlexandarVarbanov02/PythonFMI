from typing import List


def checkStraightLine(coordinates: List[List[int]]) -> bool:
    if len(coordinates) < 3:
        return True
    first = coordinates[0]
    second = coordinates[1]

    return all((y - first[1]) * (second[0] - first[0]) == (second[1] - first[1]) * (x - first[0])
               for x, y in coordinates[2:])


