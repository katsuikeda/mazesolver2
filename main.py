from graphics import Window, Point, Line
from cell import Cell


def main():
    win = Window(800, 600)

    cell1 = Cell(win, 50, 50, 100, 100, has_right_wall=False, has_bottom_wall=False)
    cell1.draw()
    cell2 = Cell(win, 100, 50, 150, 100, has_left_wall=False)
    cell2.draw()
    cell3 = Cell(win, 50, 100, 100, 150, has_top_wall=False, has_bottom_wall=False)
    cell3.draw()
    cell4 = Cell(win, 50, 150, 100, 200, has_top_wall=False, has_right_wall=False)
    cell4.draw()
    cell5 = Cell(win, 100, 150, 150, 200, has_left_wall=False, has_bottom_wall=False)
    cell5.draw()
    cell6 = Cell(win, 100, 200, 150, 250, has_right_wall=False, has_top_wall=False)
    cell6.draw()
    cell7 = Cell(win, 150, 200, 200, 250, has_left_wall=False, has_top_wall=False)
    cell7.draw()
    cell8 = Cell(win, 150, 150, 200, 200, has_bottom_wall=False, has_top_wall=False)
    cell8.draw()
    cell9 = Cell(
        win,
        150,
        100,
        200,
        150,
        has_left_wall=False,
        has_bottom_wall=False,
        has_top_wall=False,
    )
    cell9.draw()
    cell10 = Cell(win, 100, 100, 150, 150, has_right_wall=False)
    cell10.draw()
    cell11 = Cell(win, 150, 50, 200, 100, has_bottom_wall=False, has_right_wall=False)
    cell11.draw()
    cell12 = Cell(win, 200, 50, 250, 100, has_left_wall=False, has_bottom_wall=False)
    cell12.draw()

    cell1.draw_move(cell2)
    cell2.draw_move(cell1, undo=True)
    cell1.draw_move(cell3)
    cell3.draw_move(cell4)
    cell4.draw_move(cell5)
    cell5.draw_move(cell6)
    cell6.draw_move(cell7)
    cell7.draw_move(cell8)
    cell8.draw_move(cell9)
    cell9.draw_move(cell10)
    cell10.draw_move(cell9, True)
    cell9.draw_move(cell11)
    cell11.draw_move(cell12)

    win.wait_for_close()


main()
