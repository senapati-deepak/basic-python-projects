import turtle

def draw_square():
    w=turtle.Screen()
    w.bgcolor("red")
    s=turtle.Turtle()
    s.shape("arrow")
    s.color("blue")
    s.speed(2)
    for i in range (1,73):
        for x in range(1,5):
            s.forward(200)
            s.right(90)
        s.right(5)
    w.exitonclick()


draw_square()
