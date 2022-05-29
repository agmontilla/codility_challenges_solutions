"""
class MaxCounter:
    def solution(self, N: int, A: List[int]) -> List[int]:

        counters = N * [0]

        for posi, elem in enumerate(A):
            if elem == N + 1:
                counters[:] = len(counters) * [max(counters)]
                continue
            counters[elem - 1] += 1

        return counters
"""
from typing import List


class MaxCounter:
    def solution(self, N: int, A: List[int]) -> List[int]:

        counters = N * [0]
        length_counters = len(counters)
        maximum_value = 0

        for elem in A:
            if elem == N + 1:
                counters[:] = length_counters * [maximum_value]
                continue
            counters[elem - 1] += 1
            if maximum_value < counters[elem - 1]:
                maximum_value = counters[elem - 1]

        return counters


if __name__ == "__main__":
    num = 5
    sample = [3, 4, 4, 6, 1, 4, 4]
    print(MaxCounter().solution(num, sample))
