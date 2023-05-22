from turtle import Turtle, Screen

# comment here

minna = Turtle()
screen = Screen()

screen.listen()
screen.setup(600,400)
screen.bgpic("back_image.gif")
screen.update()
#screen.bgcolor('cyan')



def move_forwards():
    minna.forward(5)

def turn_right():
    #minna.right(5)
    new_heading = minna.heading() + 5
    minna.setheading(new_heading)

def turn_left():
    #minna.left(5)
    new_heading = minna.heading() - 5
    minna.setheading(new_heading)

def move_backwards():
    minna.backward(5)

def clear_screen():
    screen.resetscreen()

def move_circle_right():
    minna.circle(50, 2)

def move_circle_left():
    minna.circle(-50, 2)


screen.onkey(fun=move_forwards, key='w')
screen.onkey(fun=move_backwards, key='s')

screen.onkey(fun=turn_left, key='a')
screen.onkey(fun=turn_right, key='d')

screen.onkey(fun=move_circle_right, key='e')
screen.onkey(fun=move_circle_left, key='q')

screen.onkey(fun=clear_screen, key='c')


screen.exitonclick()
