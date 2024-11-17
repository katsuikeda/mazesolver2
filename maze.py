from cell import Cell


class Maze:
    def __init__(
        self,
        win,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
    ):
        self._win = win
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y

        self._create_cells()

    def _create_cells(self):
        for col in range(self._num_cols):
            self._cells.append([])
            for row in range(self._num_rows):
                x1 = self._x1 + (self._cell_size_x * col)
                y1 = self._y1 + (self._cell_size_y * row)
                x2 = x1 + self._cell_size_x
                y2 = y1 + self._cell_size_y
                cell = Cell(self._win, x1, y1, x2, y2)
                self._cells[col].append(cell)

        for col in range(self._num_cols):
            for row in range(self._num_rows):
                self._draw_cell(col, row)

    def _draw_cell(self, col, row):
        cell = self._cells[col][row]
        cell.draw()
        self._animate()

    def _animate(self):
        self._win.redraw()
        # Sleep for 50 ms
        self._win.sleep(50)
