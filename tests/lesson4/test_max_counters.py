import pytest

from lesson4.max_counters import solution


@pytest.mark.parametrize(
    "counters_dim, operations, expected",
    [
        (5, [3, 4, 4, 6, 1, 4, 4], [3, 2, 2, 4, 2]),
    ],
)
@pytest.mark.asyncio
async def test_max_counters_is_working(
    counters_dim: int,
    operations: list[int],
    expected: list[int],
):
    """Should return the final state of the counters after applying the operations"""
    assert await solution(counters_dim, operations) == expected
