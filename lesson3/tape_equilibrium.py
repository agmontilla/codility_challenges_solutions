"""
Lesson learned: sum is very slow compare with +=/-=
link: https://stackoverflow.com/questions/19455058/tape-equilibrium-codility-training

This was the code that I had written:
def solution(A) -> int:
    pivot = A[0]
    result = []

    if len(A) >= 1:
        for idx in range(len(A) - 1):
            posi = idx + 1
            result.append(abs(sum(A[:posi]) - sum(A[posi:])))

        pivot = min(result)

    return pivot

But finally that solution is very slow (sometimes it reached 6 seconds, above upper limit in codility)
"""


async def solution(numbers: list[int]) -> int:
    """Returns the minimal difference between the sum of the first part and the sum of the second part of the list"""
    pivot = numbers[0]

    left, right = 0, sum(numbers)
    result = []

    if len(numbers) >= 1:
        for idx in range(len(numbers) - 1):
            left += numbers[idx]
            right -= numbers[idx]
            result.append(abs(left - right))

        pivot = min(result)

    return pivot
