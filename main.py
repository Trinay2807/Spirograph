import turtle as tt

tt.bgcolor("black")
tt.pensize(2)
tt.speed(10)
for i in range(6):
    for color in ("red", "yellow", "blue","cyan", "green", "white"):
        tt.color(color)
        tt.circle(100)
        tt.left(10)
    tt.hideturtle()
