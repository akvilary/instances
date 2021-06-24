import turtle
import pandas

#Setup
screen = turtle.Screen()
screen.title("U.S. States Game")
image = './blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
FONT = "Arial", 9, "bold"
GAME_OVER_FONT = "Arial", 24, "bold"

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
#

#Data
game_is_on = True
score: int = 0
bd_states = pandas.read_csv("50_states.csv")
guessed_states = []
all_states = bd_states.state.to_list()
states_to_learn = []

#Running
while game_is_on:
    if score == 50:
        print("You win!")
        game_over_text = turtle.Turtle()
        game_over_text.penup()
        game_over_text.hideturtle()
        game_over_text.goto(-150,0)
        game_over_text.write("Game over. You win!", font=GAME_OVER_FONT)
        game_is_on = False
    else:
        answer_state = screen.textinput(title=f"{score}/50 States Correct",
                                        prompt="What's another state's name?").title()

        if answer_state == "Exit":
            states_to_learn = [lstate for lstate in all_states if lstate not in guessed_states]
            learnsheet = pandas.DataFrame(states_to_learn)
            learnsheet.to_csv("./states_to_learn.csv")
            break
        elif answer_state in all_states and answer_state not in guessed_states:
            overtext = turtle.Turtle()
            overtext.penup()
            overtext.hideturtle()
            state_info = bd_states[bd_states.state == answer_state]
            overtext.goto(int(state_info.x), int(state_info.y))
            overtext.write(state_info.state.item(), font=FONT)
            guessed_states.append(state_info.state.item())
            score += 1

