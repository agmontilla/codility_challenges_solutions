from datetime import time
from itertools import permutations


def solution(a, b, c, d):
    possible_times = set(permutations((a, b, c, d)))

    valid_time = []

    for value in possible_times:
        print(value)
        hours = int("".join(str(ch) for ch in value[:2]))
        minutes = int("".join(str(ch) for ch in value[2:]))

        try:
            clock = time(hours, minutes)
        except ValueError:
            continue

        valid_time.append(clock)

    print(*valid_time, sep="\n")
    return len(valid_time)


def main():
    a, b, c, d = (1, 2, 3, 4)
    print(solution(a, b, c, d))


if __name__ == "__main__":
    main()
