class Circle:
    def __init__(self, radius: int):
        """
        by referencing the setter, we can ensure that the
        validation logic is applied when initializing the
        object
        """
        self.radius: int = radius

    # THE GETTER
    @property
    def radius(self):
        return self.radius

    # THE SETTER
    @radius.setter
    def radius(self, value: int):
        if value < 0:
            raise ValueError("Radius cannot be negative!")
        self._radius = value


if __name__ == "__main__":
    circle = Circle(-10)
    # Using the getter: circle.radius
    print(f"Initial radius: {circle.radius}")
    # Using the setter: circle.radius = new_value
    circle.radius = 15
    print(f"New radius: {circle.radius}")
