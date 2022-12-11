from turtle import Screen, Turtle, done, bgcolor
from vector import Vector2
from bezier import getFunction

size = 1200
increment = 50

doDots = False
doText = False
showPoints = True

backgroundColor = 'black'
lineColor = 'white'
pointColor = 'red'
textColor = 'white'

Screen().setup(size, size)
bgcolor(backgroundColor)

t = Turtle()
t.hideturtle()
t.speed(0)
t.pensize(2)
    
half = (size / 2) - 50

totalDiagrams = 0
def draw(points):
    global totalDiagrams
    totalDiagrams = totalDiagrams + 1

    t.color(lineColor)
    t.penup()
    t.setpos(points[0].x, points[0].y)
    
    if not doDots:
        t.pendown()

    f = getFunction(points)

    for i in range(increment + 1):
        target = f(points, i / increment, change=0)

        t.goto(target.x, target.y)

        if doDots:
            t.dot(3, lineColor)

    t.color(textColor)

    if showPoints:
        for idx, point in enumerate(points):
            t.penup()
            t.setpos(point.x, point.y)
            t.dot(5, pointColor)
        
            if doText:
                t.write(f'{totalDiagrams}:{idx+1}', align='center', font=('Arial', 14, 'bold'))

def main():
    draw([
        Vector2(0, half),
        Vector2(-half, 0),
        Vector2(-half, -half)
    ])

    draw([
        Vector2(half, half),
        Vector2(-(half / 2), 0),
        Vector2(0, -half),
        Vector2(half, -half)
    ])

    done()

if __name__ == '__main__':
    main()
