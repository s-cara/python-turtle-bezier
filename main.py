from turtle import Screen, Turtle, done, bgcolor
from vector import Vector2, Vector3
from bezier import getPoint

Screen().setup(1000, 1000)
bgcolor('black')

t = Turtle()
t.hideturtle()
t.speed(0)
t.color('white')

def main():
    v1 = Vector2(-450, -450)
    v2 = Vector2(-450, 450)
    v3 = Vector2(450, -450)
    v4 = Vector2(450, 0)

    points = [v1, v2, v3, v4]

    for idx, point in enumerate(points):
        t.penup()
        t.setpos(point.x, point.y)
        t.dot(5)
        #t.write(idx + 1)

    t.penup()
    t.setpos(v1.x, v1.y)
    t.pendown()

    for i in range(101):
        target = getPoint(points, i / 100)

        t.goto(target.x, target.y)

    done()

if __name__ == '__main__':
    main()
