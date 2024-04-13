import pytest

from lesson3.frog_jmp import solution


@pytest.mark.asyncio
async def test_solution() -> None:
    """Test frog jump solution"""
    assert await solution(10, 85, 30) == 3
