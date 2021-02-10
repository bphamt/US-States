from turtle import Turtle
STATES = []


class States(Turtle):
    def __init__(self, name, x, y):
        super().__init__()
        self.speed("fastest")
        self.state_name = name
        self.color("red")
        self.x_pos = x
        self.y_pos = y
        self.hideturtle()
        self.penup()
        STATES.append(self)

    def write_state(self):
        self.goto(self.x_pos, self.y_pos)
        self.write(arg=f"{self.state_name}", font=("Arial", 8, "bold"))
        STATES.remove(self)

    def guess(self, answer):
        for i in STATES:
            name = i.state_name
            if name == answer:
                States.write_state(i)
                return True

    def exit(self):
        States_string = []

        for i in STATES:
            States_string.append(i.state_name)

        listToStr = '\n'.join([str(elem) for elem in States_string])

        return listToStr
