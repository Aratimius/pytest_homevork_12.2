import pytest
from utils import arrs




@pytest.mark.parametrize('array, index, default, expected', [
    ([1, 2, 3], 1, "test", 2),
    ([], 0, "test", "test"),
    ([1, 2, 3], -1, "test", "test")
])
def test_get(array, index, default, expected):
    assert arrs.get(array, index, default) == expected


@pytest.mark.parametrize('array, start, stop, expected', [
    ([1, 2, 3, 4], 1, 3, [2, 3]),
    ([1, 2, 3], 1,  None, [2, 3]),
    ([], None, None, []),
    ([1, 2, 3, 4], None, None, [1, 2, 3, 4])
])
def test_slice(array, start, stop, expected):
    assert arrs.my_slice(array, start, stop) == expected

