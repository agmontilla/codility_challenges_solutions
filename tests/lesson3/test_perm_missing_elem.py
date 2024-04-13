import pytest

from lesson3.perm_missing_elem import solution


@pytest.mark.asyncio
async def test_solution() -> None:
    """Test perm missing element solution"""
    sample = [2, 3, 1, 5]
    assert await solution(sample) == 4
