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
        """Write states text to screen"""
        self.goto(self.x_pos, self.y_pos)
        self.write(arg=f"{self.state_name}", font=("Arial", 8, "bold"))
        STATES.remove(self)

    def guess(self, answer):
        """Main guessing loop. Grabs states object in STATES list"""
        for i in STATES:
            name = i.state_name
            if name == answer:
                States.write_state(i)
                return True

    def exit(self):
        """Return a string of states remaining in game"""
        States_string = [i.state_name for i in STATES]

        listToStr = '\n'.join([str(elem) for elem in States_string])

        return listToStr
