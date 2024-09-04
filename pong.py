#Pong spēle, jo kāpēc gan nē :D


import turtle

win = turtle.Screen()
win.title("Pong")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# Lāpsta A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350, 0)

# Lāpsta B

# Bumba


# Spēles atkārtošanās
while True:
    win.update()

