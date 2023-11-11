# Penguin using graphics hw: efficient solution, with my own functions
from graphics import *

sf = 2  # scaling factor

magenta = color_rgb(160, 63, 128)
darkBlue = color_rgb(0, 0, 128)
lightBlue = color_rgb(64, 64, 192)
orange = color_rgb(224, 96, 0)


def r(x1, y1, x2, y2, color):  # rectangle
    r = Rectangle(Point(x1 * sf, y1 * sf), Point(x2 * sf, y2 * sf))
    r.setOutline(color)
    r.setFill(color)
    r.draw(penguin_win)


def c(x, y, r, color):  # circle
    c = Circle(Point(x * sf, y * sf), r * sf)
    c.setOutline(color)
    c.setFill(color)
    c.draw(penguin_win)


def o(x1, y1, x2, y2, color):  # oval
    o = Oval(Point(x1 * sf, y1 * sf), Point(x2 * sf, y2 * sf))
    o.setOutline(color)
    o.setFill(color)
    o.draw(penguin_win)


def t(x1, y1, x2, y2, x3, y3, color):  # triangle
    t = Polygon(Point(x1 * sf, y1 * sf), Point(x2 *
                sf, y2 * sf), Point(x3 * sf, y3 * sf))
    t.setOutline(color)
    t.setFill(color)
    t.draw(penguin_win)


#---------------#
# MAIN FUNCTION #
#---------------#

penguin_win = GraphWin("Penguin", 300 * sf, 281 * sf)

# bg = background with magneta rectangle with the left right cut
penguin_win.setBackground("white")  # white bg
r(0, 0, 300, 170, magenta)  # magenta r bg
o(-96, 60, 128, 281, "white")  # white o in magenta r bg
o(-10, 125, 70, 215, magenta)  # magenta o SV bg
r(-10, 170, 70, 215, "white")  # white r to cover magenta c bg

# p = penguin
o(135, 110, 290, 270, darkBlue)  # dark blue o: exterior body p
o(148, 110, 275, 270, lightBlue)  # light blue o: interior body p
o(161, 66, 262, 150, lightBlue)  # light blue o: head p
o(160, 110, 263, 270, "white")  # white c: whole body p
c(192, 110, (110 - 90), "white")  # white c: left eye whole p
c(232, 110, (110 - 90), "white")  # white c: right eye whole p
c(192, 110, (110 - 105), "black")  # black c: left eye p
c(232, 110, (110 - 105), "black")  # black c: right eye p
t(192, 125, 232, 125, 212, 150, orange)  # orange t: nose p
t(136, 270, 180, 270, 180, 250, orange)  # orange t: left foot p
t(243, 270, 289, 270, 253, 250, orange)  # orange t: right foot p

penguin_win.getMouse()
penguin_win.close()
