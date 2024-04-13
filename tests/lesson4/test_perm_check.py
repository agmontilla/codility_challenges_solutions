import pytest

from lesson4.perm_check import solution


@pytest.mark.parametrize(
    "data_input, expected",
    [
        ([4, 1, 3, 2], 1),
        ([4, 1, 3], 0),
        ([1, 1], 0),
    ],
)
@pytest.mark.asyncio
async def test_perm_check(data_input: list[int], expected: int):
    """Should return 1 if the array is a permutation and 0 if it is not."""
    assert await solution(data_input) == expected
