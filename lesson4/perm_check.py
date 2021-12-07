from typing import List


class PermCheck:
    def solution(self, A: List) -> int:
        N = max(A)
        return (
            1 if len(A) == len(set(A)) and sum(set(A)) - (N * (N + 1) // 2) == 0 else 0
        )


if __name__ == "__main__":
    # sample = [4, 1, 3, 2]
    # sample = [4, 1, 3]
    sample = [1, 1]
    print(PermCheck().solution(sample))
