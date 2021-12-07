from math import ceil


def solution(X: int, Y: int, D: int) -> int:
    return ceil((Y - X) / D)


def main():
    print(solution(10, 85, 30))


if __name__ == "__main__":
    main()
