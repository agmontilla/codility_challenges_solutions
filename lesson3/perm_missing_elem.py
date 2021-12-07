from typing import List


def solution(A: List) -> int:
    maximum_element = len(A) + 1

    gauss_sum = int(maximum_element * (maximum_element + 1) / 2)

    return gauss_sum - sum(A)


def main():
    sample = [5]
    print(solution(sample))


if __name__ == "__main__":
    main()
