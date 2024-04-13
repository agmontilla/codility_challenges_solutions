"""
lesson learned: The operation to update all values in the array when a max counter operation is performed is time consuming
So this solution it's really slow when the number of elements in the array is big

def solution(self, N: int, A: List[int]) -> List[int]:

    counters = N * [0]

    for posi, elem in enumerate(A):
        if elem == N + 1:
            counters[:] = len(counters) * [max(counters)]
            continue
        counters[elem - 1] += 1

    return counters

Another solution is to keep track of the min value and the max value,
and only apply the max operation over the counters at the end of the loop
This way we can avoid the time consuming operation of updating all the values in the array

First iteration:
[0 0 0 0 0] init max=0 min=0
[0 0 1 0 0] 3 - max=0 min=0; get_max(min, p[3]) = 0 + 1 = 1 ; max = 1
[0 0 1 1 0] 4 - max=1 min=0; get_max(min, p[4]) = 0 + 1 = 1 ; max = 1
[0 0 1 2 0] 4 - max=1 min=0; get_max(min, p[4]) = 1 + 1 = 2 ; max = 2
[0 0 1 2 0] 6 - max=2 min=2 not apply the max operation over the counters, just update the min value with the max value
[3 0 1 2 0] 1 - max=2 min=2; get_max(min, p[1]) = 2 + 1 = 3 ; max = 3
[3 0 1 3 2] 4 - max=2 min=2; get_max(min, p[4]) = 2 + 1 = 3 ; max = 3
[3 0 1 4 0] 4 - max=3 min=2; get_max(min, p[4]) = 3 + 1 = 4 ; max = 4

Last iteration:
min = 2
[3 0 1 4 0] 1 - max=4 min=2; p[1] = get_max(min, p[1]) = 3
[3 2 1 4 0] 2 - max=4 min=2; p[2] = get_max(min, p[2]) = 2
[3 2 2 4 0] 3 - max=4 min=2; p[3] = get_max(min, p[3]) = 2
[3 2 2 4 0] 4 - max=4 min=2; p[4] = get_max(min, p[4]) = 4
[3 2 2 4 0] 5 - max=4 min=2; p[5] = get_max(min, p[5]) = 2

"""


async def solution(counters_dim: int, operations: list[int]) -> list[int]:
    """Returns the final state of the counters after applying the operations"""
    min_value, max_value = 0, 0
    counters = counters_dim * [0]

    for elem in operations:
        if elem == counters_dim + 1:
            min_value = max_value
            continue
        counters[elem - 1] = max(min_value, counters[elem - 1]) + 1
        max_value = max(max_value, counters[elem - 1])

    for index in range(counters_dim):
        counters[index] = max(min_value, counters[index])

    return counters
