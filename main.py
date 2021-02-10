import turtle
import pandas
from states import States

# Setup
screen = turtle.Screen()
screen.setup(height=490, width=690)
screen.tracer(0)
screen.title("U.S. States Game")
IMAGE = "blank_states_img.gif"
GAME_STATE = True
SCORE = 0
screen.addshape(IMAGE)
turtle.shape(IMAGE)

# Data extraction from CSV
df = pandas.read_csv("50_states.csv")

# Global list creation
STATES_NAME = []
STATES_X = []
STATES_Y = []


# Append data from csv into list
for i in range(len(df)):
    STATES_NAME.append(df["state"][i])
    STATES_X.append(df["x"][i])
    STATES_Y.append(df["y"][i])

# State object creation
for i in range(len(df)):
    states = States(STATES_NAME[i], STATES_X[i], STATES_Y[i])

# Main loop
while GAME_STATE:
    screen.update()
    answer_state = (screen.textinput(title=f"{SCORE}/50", prompt="What's another state's name?")).title()

    # Quit Game & Save Remaining
    if answer_state == "Quit" or answer_state == "Exit" or answer_state == "Stop":
        with open("remaining_states.txt", mode="w") as file:
            file.write(states.exit())
        GAME_STATE = False

    # Increase score if true
    if states.guess(answer_state):
        SCORE += 1

    # If score reaches 50
    if SCORE == 50:
        GAME_STATE = False
