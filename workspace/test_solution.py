import pytest
from solution import trap, InvalidHeightError


def test_trap_happy_path():
    assert trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    assert trap([4, 2, 0, 3, 2, 5]) == 9


def test_trap_edge_cases():
    assert trap([]) == 0  # Empty list
    assert trap([1]) == 0  # Single element
    assert trap([1, 2]) == 0  # Two elements
    assert trap([3, 0, 3]) == 3  # Simple trap
    assert trap([3, 3, 3]) == 0  # Flat surface
    assert trap([0, 0, 0]) == 0  # All zeros


def test_trap_invalid_inputs():
    with pytest.raises(InvalidHeightError):
        trap([-1, 0, 1])  # Negative number
    with pytest.raises(InvalidHeightError):
        trap([1.5, 0, 2])  # Non-integer
    with pytest.raises(InvalidHeightError):
        trap(['a', 0, 1])  # Non-numeric
    with pytest.raises(InvalidHeightError):
        trap([None, 0, 1])  # NoneType


def test_trap_large_input():
    assert trap([0] * 1000 + [1] + [0] * 1000) == 0  # Large input with no trap
    assert trap([1] * 1000 + [0] * 1000 + [1] * 1000) == 1000  # Large input with trap


def test_trap_single_trap():
    assert trap([2, 0, 2]) == 2  # Single trap
    assert trap([5, 0, 5]) == 5  # Larger single trap
