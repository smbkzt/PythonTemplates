class Person:
    def move_lef(self):
        print("I'm moving left")

    def move_right(self):
        print("I'm moving right")


class Teacher(Person):
    def teach(self):
        print("I can teach pupils")

if "__main__":
    teacher = Teacher()
    teacher.move_lef()
    teacher.move_right()
    teacher.teach()