import sys

from graphics import Window, Point, Line
from maze import Maze


def main():
    screen_x = 800
    screen_y = 600
    margin = 50
    num_rows = 10
    num_cols = 14
    cell_size_x = (screen_x - margin * 2) / num_cols
    cell_size_y = (screen_y - margin * 2) / num_rows

    sys.setrecursionlimit(10000)
    win = Window(screen_x, screen_y)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)
    print("maze created...")
    print("now solving...")
    is_solved = maze.solve()
    if not is_solved:
        print("maze can not be solved!")
    else:
        print("maze solved!")

    win.wait_for_close()


main()
