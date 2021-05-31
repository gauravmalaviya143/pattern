from turtle import *
speed(10)
bgcolor('yellow')
color('red')
pensize(3)

for i in range(4):
    left(90)
    for j in range(4):
        forward(100)
        right(90)
end_fill()

for i in range(5):
    left(72)
    for j in range(5):
        forward(100)
        right(72)
end_fill()

for i in range(6):
    left(60)
    for j in range(6):
        forward(100)
        right(60)
end_fill()

for i in range(8):
    left(45)
    for j in range(8):
        forward(100)
        right(45)
end_fill()
done()