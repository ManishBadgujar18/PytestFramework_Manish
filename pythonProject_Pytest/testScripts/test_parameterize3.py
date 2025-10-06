import pytest
import math

data = [
    ([2,3,4], 'sum', 9),
    ([4,5,6], 'prod', 120),
    ([1,2,3], 'sum', 5)
]

@pytest.mark.parametrize('input, algorithm, output', data)
def test_param03(input, algorithm, output):
    print('Test 3')
    if algorithm == 'sum':
        assert sum(input) == output
    elif algorithm == 'prod':
        assert math.prod(input) == output