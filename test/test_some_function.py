import pytest
from pytest_demo.some_functions import compose_hello_to

testdata_compose_hello_to = [
    ('Kresna', 'Hello Kresna!'),
    ('World', 'Hello World!'),
    ('Anonymous', 'Hello Anonymous!')
]


@pytest.mark.parametrize("name,expected", testdata_compose_hello_to)
def test_compose_is_as_expected(name, expected):
    result = compose_hello_to(name)
    assert result == expected
