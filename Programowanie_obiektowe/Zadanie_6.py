class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        if isinstance(other, int):
            return Vector(self.x * other, self.y * other)
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, Vector):
            return self.x / other.x + self.y / other.y
        if isinstance(other, int):
            return Vector(self.x / other, self.y / other)
        return NotImplemented

    def length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __lt__(self, other):
        return


def test_vector_init():
    vector1 = Vector(x=1, y=2)
    assert vector1.x == 1
    assert vector1.y == 2


def test_vector_add():
    vector1 = Vector(x=1, y=2)
    vector2 = Vector(x=1, y=2)
    vector3 = vector1 + vector2
    assert vector3.x == 2
    assert vector3.y == 4


def test_vector_sub():
    vector1 = Vector(x=1, y=2)
    vector2 = Vector(x=1, y=2)
    vector3 = vector1 - vector2
    assert vector3.x == 0
    assert vector3.y == 0


def test_vector_mul():
    vector1 = Vector(x=1, y=2)
    vector2 = Vector(x=1, y=2)
    assert vector1 * vector2 == 1 * 1 + 2 * 2


def test_vector_truediv():
    vector1 = Vector(x=1, y=2)
    vector2 = vector1 / 1
    assert vector2.x == 1
    assert vector2.y == 2

def test_vector_length():
    assert Vector(3,4).length() == 5

def test_vector_lt():
    assert Vector(1,1) < Vector(1,2)
    assert Vector(6,5) < Vector(5,5) == False
