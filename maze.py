from cell import Cell
import time
import random

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
            seed = None
        ):
            self._x1 = x1
            self._y1 = y1
            self._num_rows = num_rows
            self._num_cols = num_cols
            self._cell_size_x = cell_size_x
            self._cell_size_y = cell_size_y
            self._win = win
            self._cells = []
            
            if seed:
                random.seed(seed)

            self._create_cells()
            self._break_entrance_and_exit()
            self._break_walls_r(0, 0)
            self._reset_cells_visited()
            self.solve()

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

    def _break_entrance_and_exit(self):
        print("breaking entrance and exit")
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)

        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            next_index_list = []

            # determine which cells to visit next
            # left
            if i > 0 and not self._cells[i - 1][j].visited:
                next_index_list.append((i - 1, j))
            # right
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                next_index_list.append((i + 1, j))
            # up
            if j > 0 and not self._cells[i][j - 1].visited:
                next_index_list.append((i, j - 1))
            # down
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                next_index_list.append((i, j + 1))

            # if there is nowhere to go from here
            # just break out
            if len(next_index_list) == 0:
                self._draw_cell(i, j)
                return
            
            # randomly choose the next direction to go
            direction_index = random.randrange(len(next_index_list))
            next_index = next_index_list[direction_index]

            # knock out walls between this cell and the next cell(s)
            # right
            if next_index[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
            # left
            if next_index[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
            # down
            if next_index[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
            # up
            if next_index[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False

            # recursively visit the next cell
            self._break_walls_r(next_index[0], next_index[1])
    
    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True

        # left
        if i > 0 and not self._cells[i][j].has_left_wall and not self._cells[i - 1][j].visited:
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            result = self._solve_r(i - 1, j)
            if result:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i - 1][j], True)
        # right
        if i < self._num_cols - 1 and not self._cells[i][j].has_right_wall and not self._cells[i + 1][j].visited:
            self._cells[i][j].draw_move(self._cells[i + 1][j])
            result = self._solve_r(i + 1, j)
            if result:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i + 1][j], True)
        # up
        if j > 0 and not self._cells[i][j].has_top_wall and not self._cells[i][j - 1].visited:
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            result = self._solve_r(i, j - 1)
            if result:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j - 1], True)
        # down
        if j < self._num_rows and not self._cells[i][j].has_bottom_wall and not self._cells[i][j + 1].visited:
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            result = self._solve_r(i, j + 1)
            if result:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j + 1], True)

        return False
            

    def solve(self):
        solved = self._solve_r(0, 0)
        return solved
            
    def _animate(self):
         self._win.redraw()
         time.sleep(0.05)

    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False
        
        