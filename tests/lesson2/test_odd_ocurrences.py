import pytest

from lesson2.odd_ocurrences import solution


@pytest.mark.asyncio
async def test_solution():
    """Test odd ocurrences solution"""
    sample = [9, 3, 9, 3, 9, 7, 9]
    assert await solution(sample) == 7
