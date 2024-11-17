from graphics import Window, Point, Line


class Cell:
    # (x1, y1): top-left, (x2, y2): bottom-right
    def __init__(
        self,
        x1,
        y1,
        x2,
        y2,
        has_left_wall=True,
        has_right_wall=True,
        has_top_wall=True,
        has_bottom_wall=True,
        win=None,
    ):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self._win = win

    def draw(self):
        if self._win is None:
            return

        left_wall = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
        right_wall = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
        top_wall = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
        bottom_wall = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))

        self.draw_wall(left_wall, self.has_left_wall)
        self.draw_wall(right_wall, self.has_right_wall)
        self.draw_wall(top_wall, self.has_top_wall)
        self.draw_wall(bottom_wall, self.has_bottom_wall)

    def draw_wall(self, wall, has_wall):
        fill_color = "black" if has_wall else "white"
        self._win.draw_line(wall, fill_color)

    def draw_move(self, to_cell, undo=False):
        line = Line(
            Point((self._x1 + self._x2) / 2, (self._y1 + self._y2) / 2),
            Point((to_cell._x1 + to_cell._x2) / 2, (to_cell._y1 + to_cell._y2) / 2),
        )
        fill_color = "red"
        if undo:
            fill_color = "grey"
            self._win.draw_line(line, fill_color)
            return
        self._win.draw_line(line, fill_color)
