import pytest

from src.getCount import get_count

@pytest.mark.parametrize(
    "text, expected_count",
    (
        ("1234", 3),
        ("10101", 1),
        ("54321", 2),
    )
)
def test_get_count(text, expected_count):
    assert get_count(text) == expected_count, f"Test text: '{text}' expected count: '{expected_count}'"
