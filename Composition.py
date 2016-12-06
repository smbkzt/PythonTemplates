class Head:
    def __init__(self, eye_color, hair_color):
        self.eye_color = eye_color
        self.hair_color = hair_color

class Body:
    def __init__(self, weight):
        self.weight = weight


class Person:
    def __init__(self, eye_color, hair_color, weight):
        self.head = Head(eye_color, hair_color)
        self.body = Body(weight)

    def print_eye_color(self):
        print(self.head.eye_color)


if "__main__":
    bekzat = Person("brown", "black", 180)
    bekzat.print_eye_color()