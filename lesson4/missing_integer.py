"""
This solution is O(n**2)
The solution is correct but it is not optimal. The time complexity of the solution is O(n**2) because of the line:
if i not in arr:
    return i

async def solution(arr: list[int]) -> int:
    arr.sort()
    for i in range(1, len(arr) + 1):
        if i not in arr:
            return i
    return len(arr) + 1

So we can improve it to O(n) by using a set to store the values of the array and
compare it with the ideal set of values from 1 to len(arr) + 1.
"""


async def solution(arr: list[int]) -> int:
    """Return the smallest positive integer that does not occur in a given sequence."""
    arr_set = set(arr)
    ideal_set = set(range(1, len(arr) + 1))

    difference = ideal_set.difference(arr_set)
    if difference == arr_set:
        return 1
    return min(difference, default=len(arr) + 1)
