from typing import List


class FrogRiverOne:
    def solution(self, X: int, A: List[int]) -> int:

        leaves = {}

        if sum(set(A)) - (X * (X + 1) // 2) != 0:
            return -1

        for second, position in enumerate(A):
            if position not in leaves:
                leaves[position] = second

        return max(leaves.values())


if __name__ == "__main__":
    # data_input = [1, 1, 2, 3, 5, 6, 4]
    # x = 6

    # data_input = [3, 1, 4, 2, 3, 5, 4]
    data_input = [1, 3, 1, 4, 2, 3, 5, 4]
    # data_input = [1, 2, 4, 5]
    x = 5
    print(FrogRiverOne().solution(x, data_input))
