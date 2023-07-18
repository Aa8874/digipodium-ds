from turtle import *

speed ('slowest')

def polygon(sides , length , color , width):
    pencolor(color)
    pensize(width)
    for i in range(sides):
        forward(length)
        right(360/sides)

# calling
polygon( 4 , 100 , "blue" , 5) # square
goto(200 , 0)
polygon(6 , 50 , 'green' , 2)
goto(200 , 200)
polygon(3 , 100 , 'red', 10)

hideturtle()
mainloop()
