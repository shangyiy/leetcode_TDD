import pytest
from src.solution import Solution

s = Solution()

def test_case0():
    assert s.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]) == [5, 6]