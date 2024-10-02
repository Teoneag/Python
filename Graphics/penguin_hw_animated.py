# Penguin minigame using graphics hw: efficient solution, with my own functions
from graphics import *
import random

sf = 2.5  # scaling factor
xm, ym = 0, 0  # change in coordonates

messages_intro = ["Click me and u'll get free ...", "I'm joking, but at least I see I got ur atention :))", "So 'morning, what u doing?", "Actually I don't care, lmao", "So as you can see, where u touch the screen, there I move",
                  "So pls stop toughing the screen, kinda anoying", "Come on!", "Stoooooooooooooooop!", "Bro, seriousely"]
messages_eggs = ["Ou, and those are my eggs", "Please don't make me sit on them", "So DON'T CLICK THE EGGS!!!", "pls :))"]
messages_teaca = ["Ha!", "Lmao", "Teaca!", "I't just me or u weak?",
                  "Haha, no chance!", "ou, somebody is getting angry :)", "try more, u noob", "..."]

magenta = color_rgb(160, 63, 128)
darkBlue = color_rgb(0, 0, 128)
lightBlue = color_rgb(64, 64, 192)
orange = color_rgb(224, 96, 0)
eggColor = color_rgb(210, 184, 161)


def clearWin():
    for x in penguin_win.items[4:]:  # the first 4 el are the bg
        x.undraw()
    penguin_win.update()


def r(x1, y1, x2, y2, color, okM):  # rectangle
    r = Rectangle(Point(x1 * sf + xm, y1 * sf + ym), Point(x2 * sf + xm, y2 * sf + ym)
                  ) if okM == 1 else Rectangle(Point(x1 * sf, y1 * sf), Point(x2 * sf, y2 * sf))
    r.setOutline(color)
    r.setFill(color)
    r.draw(penguin_win)


def c(x, y, r, color, okM):  # circle
    c = Circle(Point(x * sf + xm, y * sf + ym), r *
               sf) if okM == 1 else Circle(Point(x * sf, y * sf), r * sf)
    c.setOutline(color)
    c.setFill(color)
    c.draw(penguin_win)


def o(x1, y1, x2, y2, color, okM):  # oval
    o = Oval(Point(x1 * sf + xm, y1 * sf + ym), Point(x2 * sf + xm, y2 * sf + ym)
             ) if okM else Oval(Point(x1 * sf, y1 * sf), Point(x2 * sf, y2 * sf))
    o.setOutline(color)
    o.setFill(color)
    o.draw(penguin_win)


def t(x1, y1, x2, y2, x3, y3, color, okM):  # triangle
    t = Polygon(Point(x1 * sf + xm, y1 * sf + ym), Point(x2 * sf + xm, y2 * sf + ym), Point(x3 * sf + xm, y3 * sf + ym)
                ) if okM else Polygon(Point(x1 * sf, y1 * sf), Point(x2 * sf, y2 * sf), Point(x3 * sf, y3 * sf))
    t.setOutline(color)
    t.setFill(color)
    t.draw(penguin_win)


def drawEgg():
    x1, y1 = (xm + 212 * sf - 200) / sf, (ym + 100 * sf - 170) / sf
    x2, y2 = (xm + 212 * sf + 200) / sf, (ym + 100 * sf + 430) / sf
    while 1:
        x, y = random.randint(10, 260), random.randint(10, 250)
        if x < x1 or x > x2 or y < y1 or y > y2:
            break
    o(x - 1, y - 1, x + 1 + 14, y + 1 + 20, "white", 0)
    o(x, y, x + 14, y + 20, eggColor, 0)
    o(x - 1 + 11, y - 1 + 10, x + 1 + 11 + 20, y + 1 + 10 + 14, "white", 0)
    o(x + 11, y + 10, x + 11 + 20, y + 10 + 14, eggColor, 0)


def drawMessage(x, y, text):
    o(x - len(text) * 1.4 - 5 - 2, y - 15 - 2, x +
      len(text) * 1.4 + 5 + 2, y + 15 + 2, "black", 1)
    t(x - 5, y + 15, x + 5, y + 15, x - 10, y + 30, "black", 1)
    o(x - len(text) * 1.4 - 5, y - 15, x +
      len(text) * 1.4 + 5, y + 15, "white", 1)
    s = Text(Point(x * sf + xm, y * sf + ym), text)
    s.draw(penguin_win)


def drawBg():  # bg = background with magneta rectangle with the left right cut
    r(0, 0, 300, 170, magenta, 0)  # magenta r bg
    o(-96, 60, 128, 281, "white", 0)  # white o in magenta r bg
    o(-10, 125, 70, 215, magenta, 0)  # magenta o SV bg
    r(-10, 170, 70, 215, "white", 0)  # white r to cover magenta c bg


def drawPeng():  # p = peng = penguin
    o(135, 110, 290, 270, darkBlue, 1)  # dark blue o: exterior body p
    o(148, 110, 275, 270, lightBlue, 1)  # light blue o: interior body p
    o(161, 66, 262, 150, lightBlue, 1)  # light blue o: head p
    o(160, 110, 263, 270, "white", 1)  # white c: whole body p
    c(192, 110, (110 - 90), "white", 1)  # white c: left eye whole p
    c(232, 110, (110 - 90), "white", 1)  # white c: right eye whole p
    c(192, 110, (110 - 105), "black", 1)  # black c: left eye p
    c(232, 110, (110 - 105), "black", 1)  # black c: right eye p
    t(192, 125, 232, 125, 212, 150, orange, 1)  # orange t: nose p
    t(136, 270, 180, 270, 180, 250, orange, 1)  # orange t: left foot p
    t(243, 270, 289, 270, 253, 250, orange, 1)  # orange t: right foot p


#---------------#
# MAIN FUNCTION #
#---------------#

penguin_win = GraphWin("Penguin", 300 * sf, 281 * sf, autoflush=0)
penguin_win.setBackground("white")  # white bg

for message in messages_intro:
    drawBg()
    drawPeng()
    drawMessage(250, 50, message)
    p = penguin_win.getMouse()
    xm = p.getX() - 212 * sf
    ym = p.getY() - 100 * sf
    clearWin()

for message in messages_eggs:
    drawBg()
    drawEgg()
    drawPeng()
    drawMessage(250, 50, message)
    p = penguin_win.getMouse()
    xm = p.getX() - 212 * sf
    ym = p.getY() - 100 * sf
    clearWin()

while 1:
    drawBg()
    drawEgg()
    drawPeng()
    drawMessage(250, 50, random.choice(messages_teaca))
    p = penguin_win.getMouse()
    xm = p.getX() - 212 * sf
    ym = p.getY() - 100 * sf
    clearWin()
    
penguin_win.close()
