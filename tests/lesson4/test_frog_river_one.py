import pytest

from lesson4.frog_river_one import solution


@pytest.mark.parametrize(
    "x, data_input, expected",
    [
        (6, [1, 1, 2, 3, 5, 6, 4], 6),
        (5, [1, 3, 1, 4, 2, 3, 5, 4], 6),
        (4, [1, 2, 4, 5], -1),
    ],
)
@pytest.mark.asyncio
async def test_case_frog_river_one_is_working(data_input: list[int], x: int, expected: int) -> None:
    """Should return the earliest time when the frog can jump to the other side of the river."""
    assert await solution(x, data_input) == expected
