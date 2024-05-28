from turtle import Turtle, Screen
import random

def setup_turtle_race():
    screen = Screen()
    screen.setup(width=500, height=400)
    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
    
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    y_positions = [-70, -40, -10, 20, 50, 80]
    
    turtles = []
    for index in range(6):
        turtle = Turtle(shape="turtle")
        turtle.penup()
        turtle.color(colors[index])
        turtle.goto(x=-230, y=y_positions[index])
        turtles.append(turtle)
    
    return screen, user_bet, turtles

def start_race(turtles, user_bet):
    is_race_on = user_bet is not None
    while is_race_on:
        for turtle in turtles:
            if turtle.xcor() > 230:
                is_race_on = False
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    print(f"You've won! The {winning_color} turtle is the winner!")
                else:
                    print(f"You've lost! The {winning_color} turtle is the winner!")
                break
            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)

def main():
    screen, user_bet, turtles = setup_turtle_race()
    start_race(turtles, user_bet)
    screen.exitonclick()

if __name__ == "__main__":
    main()
