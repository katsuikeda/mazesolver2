from graphics import Window, Point, Line


def main():
    win = Window(800, 600)
    p1 = Point(50, 80)
    p2 = Point(500, 500)
    p3 = Point(50, 520)
    p4 = Point(500, 100)
    line = Line(p1, p2)
    line2 = Line(p3, p4)
    win.draw_line(line, "black")
    win.draw_line(line2, "black")

    win.wait_for_close()


main()
