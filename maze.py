import random

from cell import Cell


class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None,
    ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        if seed:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        for col in range(self._num_cols):
            self._cells.append([])
            for row in range(self._num_rows):
                x1 = self._x1 + (self._cell_size_x * col)
                y1 = self._y1 + (self._cell_size_y * row)
                x2 = x1 + self._cell_size_x
                y2 = y1 + self._cell_size_y
                cell = Cell(x1, y1, x2, y2, win=self._win)
                self._cells[col].append(cell)

        for col in range(self._num_cols):
            for row in range(self._num_rows):
                self._draw_cell(col, row)

    def _draw_cell(self, col, row):
        if self._win is None:
            return
        cell = self._cells[col][row]
        cell.draw()
        self._animate()

    def _animate(self):
        self._win.redraw()
        # Sleep for 50 ms
        self._win.sleep(50)

    def _break_entrance_and_exit(self):
        entrance_cell = self._cells[0][0]
        exit_cell = self._cells[self._num_cols - 1][self._num_rows - 1]

        entrance_cell.has_top_wall = False
        self._draw_cell(0, 0)
        exit_cell.has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, col, row):
        directions = [
            ("left", -1, 0, "has_left_wall", "has_right_wall"),
            ("right", 1, 0, "has_right_wall", "has_left_wall"),
            ("up", 0, -1, "has_top_wall", "has_bottom_wall"),
            ("down", 0, 1, "has_bottom_wall", "has_top_wall"),
        ]
        current_cell = self._cells[col][row]
        current_cell.is_visited = True

        while True:
            unvisited_neighbors = []
            for direction, dx, dy, current_wall, opposite_wall in directions:
                new_col, new_row = col + dx, row + dy
                if 0 <= new_col < self._num_cols and 0 <= new_row < self._num_rows:
                    neighbor = self._cells[new_col][new_row]
                    if not neighbor.is_visited:
                        unvisited_neighbors.append(
                            (neighbor, new_col, new_row, current_wall, opposite_wall)
                        )

            if not unvisited_neighbors:
                self._draw_cell(col, row)
                return

            neighbor, new_col, new_row, current_wall, opposite_wall = random.choice(
                unvisited_neighbors
            )
            setattr(current_cell, current_wall, False)
            setattr(neighbor, opposite_wall, False)
            self._break_walls_r(new_col, new_row)

    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.is_visited = False
