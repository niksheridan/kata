import pytest

from kata.getter_setter import Circle


def test_getter_setter():
    obj = Circle(10)
    assert obj.radius == 10

    obj.radius = 20
    assert obj.radius == 20

    with pytest.raises(ValueError, match="Radius cannot be negative!"):
        obj.radius = -5
