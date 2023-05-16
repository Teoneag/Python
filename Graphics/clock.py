from cmath import cos, pi, sin
from pydoc import text
from time import *
from graphics import *

Y = strftime("%Y")
m = strftime("%m")
d = strftime("%d")
A = strftime("%A")
h = strftime("%H")
m = strftime("%M")
s = strftime("%S")

sf = 1  # scaling factor
R = 150  # radius
C = 200  # centre

magenta = color_rgb(160, 63, 128)
darkBlue = color_rgb(0, 0, 128)
lightBlue = color_rgb(64, 64, 192)
orange = color_rgb(224, 96, 0)


# def l(x1, y1, x2, y2, color):  # poligon
# l = Polygon(Point())


def r(x1, y1, x2, y2, color):  # rectangle
    r = Rectangle(Point(x1 * sf, y1 * sf), Point(x2 * sf, y2 * sf))
    r.setOutline(color)
    r.setFill(color)
    r.draw(clock_win)


def c(x, y, r, color):  # circle
    c = Circle(Point(x * sf, y * sf), r * sf)
    c.setOutline(color)
    c.setFill(color)
    c.draw(clock_win)


def o(x1, y1, x2, y2, color):  # oval
    o = Oval(Point(x1 * sf, y1 * sf), Point(x2 * sf, y2 * sf))
    o.setOutline(color)
    o.setFill(color)
    o.draw(clock_win)


def t(x1, y1, x2, y2, x3, y3, color):  # triangle
    t = Polygon(Point(x1 * sf, y1 * sf), Point(x2 *
                sf, y2 * sf), Point(x3 * sf, y3 * sf))
    t.setOutline(color)
    t.setFill(color)
    t.draw(clock_win)


#---------------#
# MAIN FUNCTION #
#---------------#
clock_win = GraphWin("Clock", 400 * sf, 400 * sf)

c(200, 200, R + 30, "black")
c(200, 200, R + 20, "white")
# c(200, 200, 10, "black")

for i in range(0, 24):
    angle = pi * 2 / 24 * (i + 1) - 0.25 * 2 * pi
    print(C + sin(angle).real * R, C + cos(angle).real * R)
    t = Text(Point(C + cos(angle).real * R, C + sin(angle).real * R), str((i + 1)))
    t.draw(clock_win)

clock_win.getMouse()
clock_win.close()

sin
