from graphics import Window, Point, Line
from cell import Cell


def main():
    win = Window(800, 600)

    cell = Cell(win, 50, 50, 100, 100)
    cell.draw()
    cell = Cell(win, 100, 50, 150, 100, has_top_wall=False)
    cell.draw()
    cell = Cell(win, 50, 100, 100, 150, has_top_wall=False, has_bottom_wall=False)
    cell.draw()
    cell = Cell(win, 50, 150, 100, 200, has_top_wall=False, has_right_wall=False)
    cell.draw()
    cell = Cell(win, 100, 150, 150, 200, has_left_wall=False, has_bottom_wall=False)
    cell.draw()

    win.wait_for_close()


main()
