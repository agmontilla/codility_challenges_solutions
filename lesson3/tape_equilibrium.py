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


from typing import List


def solution(A: List) -> int:
    pivot = A[0]

    left, right = 0, sum(A)
    result = []

    if len(A) >= 1:
        for idx in range(len(A) - 1):
            left += A[idx]
            right -= A[idx]
            result.append(abs(left - right))

        pivot = min(result)

    return pivot


def main():
    # sample = [-1000, 1000]
    sample = [3, 1, 2, 4, 3]
    print(solution(sample))


if __name__ == "__main__":
    main()
