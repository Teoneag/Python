from graphics import *

sf = 2  # scaling factor

magenta = color_rgb(160, 63, 128)
darkBlue = color_rgb(0, 0, 128)
lightBlue = color_rgb(64, 64, 192)
orange = color_rgb(224, 96, 0)

# rectangle background: magenta
r_bg = Rectangle(Point(0, 0), Point(300 * sf, 170 * sf))
r_bg.setOutline(magenta)
r_bg.setFill(magenta)

# "hole" background: white
h_bg = Oval(Point(-96 * sf, 60 * sf), Point(128 * sf, 281 * sf))
h_bg.setOutline("white")
h_bg.setFill("white")

# "oval" background: magenta
o_bg = Oval(Point(-10 * sf, 125 * sf), Point(70 * sf, 215 * sf))
o_bg.setOutline(magenta)
o_bg.setFill(magenta)

# rectange cut background: for the down left corner
r_c_bg = Rectangle(Point(-10 * sf, 170 * sf), Point(70 * sf, 215 * sf))
r_c_bg.setOutline("white")
r_c_bg.setFill("white")


# oval exterior body penguin
o_e_b_p = Oval(Point(135 * sf, 110 * sf), Point(290 * sf, 270 * sf))
o_e_b_p.setOutline(darkBlue)
o_e_b_p.setFill(darkBlue)

# oval interior body penguin
o_i_b_p = Oval(Point(148 * sf, 110 * sf), Point(275 * sf, 270 * sf))
o_i_b_p.setOutline(lightBlue)
o_i_b_p.setFill(lightBlue)

# oval head penguin
o_h_p = Oval(Point(161 * sf, 66 * sf), Point(262 * sf, 150 * sf))
o_h_p.setOutline(lightBlue)
o_h_p.setFill(lightBlue)

# hole interrior body penguin
h_i_b_p = Oval(Point(160 * sf, 110 * sf), Point(263 * sf, 270 * sf))
h_i_b_p.setOutline("white")
h_i_b_p.setFill("white")

# hole left eye head penguin
h_l_e_h_p = Circle(Point(192 * sf, 110 * sf), (110 - 90) * sf)
h_l_e_h_p.setOutline("white")
h_l_e_h_p.setFill("white")

# hole right eye head penguin
h_r_e_h_p = Circle(Point(232 * sf, 110 * sf), (110 - 90) * sf)
h_r_e_h_p.setOutline("white")
h_r_e_h_p.setFill("white")

# circle left eye penguin
c_l_e_p = Circle(Point(192 * sf, 110 * sf), (110 - 105) * sf)
c_l_e_p.setOutline("black")
c_l_e_p.setFill("black")

# circle right eye penguin
c_r_e_p = Circle(Point(232 * sf, 110 * sf), (110 - 105) * sf)
c_r_e_p.setOutline("black")
c_r_e_p.setFill("black")


# triangle nose penguin
t_n_p = Polygon(Point(192 * sf, 125 * sf), Point(232 *
                sf, 125 * sf), Point(212 * sf, 150 * sf))
t_n_p.setOutline(orange)
t_n_p.setFill(orange)

# triangle left foot penguin
t_l_f_p = Polygon(Point(13 * sf, 270 * sf), Point(180 *
                  sf, 270 * sf), Point(180 * sf, 250 * sf))
t_l_f_p.setOutline(orange)
t_l_f_p.setFill(orange)
6
# triangle right foot penguin
t_r_f_p = Polygon(Point(243 * sf, 270 * sf), Point(289 *
                  sf, 270 * sf), Point(253 * sf, 250 * sf))
t_r_f_p.setOutline(orange)
t_r_f_p.setFill(orange)


#---------------#
# MAIN FUNCTION #
#---------------#
penguin_win = GraphWin("Penguin", 300 * sf, 281 * sf)

# background with magneta rectangle with the left right cut
penguin_win.setBackground("white")
r_bg.draw(penguin_win)
h_bg.draw(penguin_win)
o_bg.draw(penguin_win)
r_c_bg.draw(penguin_win)

# penguin
o_e_b_p.draw(penguin_win)
o_i_b_p.draw(penguin_win)
o_h_p.draw(penguin_win)
h_i_b_p.draw(penguin_win)
h_l_e_h_p.draw(penguin_win)
h_r_e_h_p.draw(penguin_win)
c_l_e_p.draw(penguin_win)
c_r_e_p.draw(penguin_win)
t_n_p.draw(penguin_win)
t_l_f_p.draw(penguin_win)
t_r_f_p.draw(penguin_win)

penguin_win.getMouse()
penguin_win.close()
