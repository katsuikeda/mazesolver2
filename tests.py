import unittest

from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 14
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_break_entrance_and_exit(self):
        num_cols = 14
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        entrance_cell = m1._cells[0][0]
        exit_cell = m1._cells[m1._num_cols - 1][m1._num_rows - 1]
        self.assertFalse(entrance_cell.has_top_wall)
        self.assertFalse(exit_cell.has_bottom_wall)

    def test_reset_cells_visited(self):
        num_cols = 14
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1._create_cells()
        m1._break_entrance_and_exit()
        m1._break_walls_r(0, 0)
        m1._reset_cells_visited()

        for col in m1._cells:
            for cell in col:
                self.assertFalse(cell.is_visited)


if __name__ == "__main__":
    unittest.main()
