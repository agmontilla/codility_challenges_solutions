from collections import Counter
from typing import List


def solution(sample: List) -> int:

    stats = Counter(sample)

    unpaired_element = 0

    for k, v in stats.items():
        if v % 2 != 0:
            unpaired_element = k
            break

    return unpaired_element


def main():
    sample = [9, 3, 9, 3, 9, 7, 9]
    print(solution(sample))


if __name__ == "__main__":
    main()
