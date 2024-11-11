from typing import List
from collections import Counter


def majorityElement(nums: List[int]) -> int:
    counts = Counter(nums)
    return max(counts, key=counts.get)

# def majorityElement(nums: List[int]) -> int:
#     counter = 0
#     major_element = None
#
#     for num in nums:
#         if counter == 0:
#             major_element = num
#         if major_element == num:
#             counter += 1
#         else:
#             counter -= 1
#
#     return major_element

