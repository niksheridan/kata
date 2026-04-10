from getter_setter import Circle


def test_getter_setter():
    obj = Circle(10)
    assert obj.radius == 10

    obj.radius = 20
    assert obj.radius == 20

    try:
        obj.radius = -5
    except ValueError as exc:
        assert str(exc) == "Radius cannot be negative!"
