import turtle

# import time

# turtle.speed(0)
# for i in range(60):
#     turtle.right(6 * i)
#     turtle.forward(100)
#     turtle.home()
#     turtle.clear()
#     time.sleep(1)
# turtle.done()

turtle.penup()
turtle.tracer(0, 0)

for i in range(8):
    turtle.right(45 * i)
    turtle.forward(100)
    turtle.stamp()
    turtle.home()

turtle.done()
