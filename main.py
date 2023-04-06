import turtle
import pandas

screen = turtle.Screen()
screen.title("The Us State Game")
img = "blank_states_img.gif"
timmy = turtle.Turtle()
screen.addshape(img)
timmy.shape(img)
data = pandas.read_csv("50_states.csv")
x = 0
score = 0
states_column = data.state
l = states_column.to_list()


def modifying_ans(ans):
    new_ans = ""
    li = ans.split()
    for w in li:
        new_ans += w[0].upper() + w[1::]
        new_ans += ' '
    return new_ans.strip()


def writing_with_turtle(state, xc, yc):
    obj = turtle.Turtle()
    obj.penup()
    obj.hideturtle()
    obj.goto(xc, yc)
    obj.write(state, align="left", font=("Arial", 8, "normal"))


guessed_states = []
while x != 50:
    answer = modifying_ans(screen.textinput(f"Enter your guess{score}/50", "What's the state name"))
    if answer == "Exit":
        break
    elif answer in l:
        guessed_states.append(answer)
        row = data[data.state == answer]
        xcor = int(row.x)
        ycor = int(row.y)
        writing_with_turtle(answer, xcor, ycor)
        x += 1
        score += 1


# Generating the csv file to learn the states


li = [w for w in l if w not in guessed_states]
new_data = pandas.DataFrame(li)
new_data.to_csv("states_to_learn.csv")









screen.exitonclick()
