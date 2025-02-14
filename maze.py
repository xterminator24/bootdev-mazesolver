from cell import Cell
import time

class Maze():
    def __init__(
            self,
            x1, 
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win = None,
        ):
            self._x1 = x1
            self._y1 = y1
            self._num_rows = num_rows
            self._num_cols = num_cols
            self._cell_size_x = cell_size_x
            self._cell_size_y = cell_size_y
            self._win = win
            self._cells = []
            self._create_cells()

    def _create_cells(self):
        for c in range(0, self._num_cols):
            self._cells.append([])
            for r in range(0, self._num_rows):
                cell = Cell(self._win)
                self._cells[c].append(cell)

        for c in range(0, len(self._cells)):
            for r in range(0, len(self._cells[c])):
                self._draw_cell(c, r) 

    def _draw_cell(self, col_num, row_num):
        if self._win is None:
            return
        x1 = self._x1 + (col_num * self._cell_size_x)
        y1 = self._y1 + (row_num * self._cell_size_y)
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[col_num][row_num].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
         self._win.redraw()
         time.sleep(0.03)
        
        