from datetime import time

import pytest

from technical_challenge.valid_hours import solution


@pytest.mark.parametrize(
    "input_values,  expected",
    [
        (
            (1, 8, 3, 2),
            [time(12, 38), time(13, 28), time(18, 23), time(18, 32), time(21, 38), time(23, 18)],
        ),
        (
            (2, 3, 3, 2),
            [time(22, 33), time(23, 23), time(23, 32)],
        ),
        (
            (1, 2, 3, 4),
            [
                time(12, 34),
                time(12, 43),
                time(13, 24),
                time(13, 42),
                time(14, 23),
                time(14, 32),
                time(21, 34),
                time(21, 43),
                time(23, 14),
                time(23, 41),
            ],
        ),
    ],
)
@pytest.mark.asyncio
async def test_valid_hours_is_working(input_values: tuple[int, int, int, int], expected: list[time]):
    """Should return all the possible valid times"""
    response = await solution(*input_values)
    assert response == expected
