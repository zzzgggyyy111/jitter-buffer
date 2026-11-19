import pytest

from net import jitter as mod

CASES = [
    ('reorder', [[[2, 'b'], [1, 'a']]], [[1, 'a'], [2, 'b']], False),
    ('reorder', [[]], [], False),
    ('target_delay', [0.02, 0.02], 0.06, True),
    ('playout', [[[1, 'a'], [3, 'c']], 2], [[1, 'a']], False),
    ('conceal', ['a', 2], ['a', 'a'], False),
    ('conceal', ['a', 0], [], False),
    ('buffer_size', [0.02, 0.02], 3, False),
    ('buffer_size', [0.02, 0], 0, False),
    ('reorder', [[[1, 'a']]], [[1, 'a']], False),
    ('target_delay', [0, 0.02], 0.02, True),
    ('playout', [[], 1], [], False),
    ('conceal', ['x', 1], ['x'], False),
    ('buffer_size', [0, 0.02], 1, False),
    ('playout', [[[1, 'a'], [2, 'b']], 5], [[1, 'a'], [2, 'b']], False),
    ('reorder', [[[3, 'c'], [1, 'a'], [2, 'b']]], [[1, 'a'], [2, 'b'], [3, 'c']], False),
]


@pytest.mark.parametrize("func_name,args,expected,approx", CASES)
def test_jitter_contract(func_name, args, expected, approx):
    func = getattr(mod, func_name)
    result = func(*args)
    if approx:
        assert result == pytest.approx(expected)
    else:
        assert result == expected
