from turtle import Turtle, Screen
import random

is_race = False
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet",prompt="Which Turtle will win?\n(RED/GREEN/BLUE/YELLOW/BLACK)")
all_turtles = []
position = [-100,-50,0,50,100]
colours = ['green','red','black','blue','yellow']

#------5 Players-------
for turtle_index in range(0,5):
    new_turtle = Turtle('turtle')
    new_turtle.color(colours[turtle_index])
    all_turtles.append(new_turtle)
    new_turtle.penup()
    new_turtle.goto(x=-240,y=-position[turtle_index])
    
if user_bet:
    is_race =True

while is_race:

    for turtle in all_turtles:
        if turtle.xcor()>=230:
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print(f"You've won! The {winning_color} turtle is the Winner!")
                is_race = False
            else:
                print(f"You've lost! The {winning_color} turtle is the Winner!")
                is_race = False
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)
        
    
screen.exitonclick()