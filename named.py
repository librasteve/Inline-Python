# this is used by test file t/import.t

from logging import warn
def test_named(a, b):
    return a + b
def test_kwargs(**kwargs):
    return len(kwargs)
