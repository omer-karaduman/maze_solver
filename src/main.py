from window import Window
from point import Point
from line import Line
from cell import Cell
def main():
    win = Window(800, 600)

    c = Cell(win)
    c.has_left_wall = False
    c.draw(50, 50, 100, 100)

    c = Cell(win)
    c.has_right_wall = False
    c.draw(125, 125, 200, 200)

    c = Cell(win)
    c.has_bottom_wall = False
    c.draw(225, 225, 250, 250)

    c1 = Cell(win)
    c1.has_top_wall = False
    c1.draw(300, 300, 500, 500)

    c.draw_move(c1)

    win.wait_for_close()

main()