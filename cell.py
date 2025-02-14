from graphics import Line, Point, Window

class Cell():
    def __init__(self, win: Window = None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = win

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        if self.has_left_wall:
            top_point = Point(x1, y1)
            bottom_point = Point(x1, y2)
            line = Line(top_point, bottom_point)
            self._win.draw_line(line)
        else:
            top_point = Point(x1, y1)
            bottom_point = Point(x1, y2)
            line = Line(top_point, bottom_point)
            self._win.draw_line(line, "white")

        if self.has_right_wall:
            top_point = Point(x2, y1)
            bottom_point = Point(x2, y2)
            line = Line(top_point, bottom_point)
            self._win.draw_line(line)
        else:
            top_point = Point(x2, y1)
            bottom_point = Point(x2, y2)
            line = Line(top_point, bottom_point)
            self._win.draw_line(line, "white")

        if self.has_top_wall:
            left_point = Point(x1, y1)
            right_point = Point(x2, y1)
            line = Line(left_point, right_point)
            self._win.draw_line(line)
        else:
            left_point = Point(x1, y1)
            right_point = Point(x2, y1)
            line = Line(left_point, right_point)
            self._win.draw_line(line, "white")

        if self.has_bottom_wall:
            left_point = Point(x1, y2)
            right_point = Point(x2, y2)
            line = Line(left_point, right_point)
            self._win.draw_line(line)
        else:
            left_point = Point(x1, y2)
            right_point = Point(x2, y2)
            line = Line(left_point, right_point)
            self._win.draw_line(line, "white")

    def draw_move(self, to_cell, undo = False):
        color = "red"
        if undo:
            color = "gray"
        
        line = Line(self.get_center(), to_cell.get_center())
        self._win.draw_line(line, color)

    def get_center(self):
        x = int(self._x1 + (abs(self._x2 - self._x1) // 2))
        y = int(self._y1 + (abs(self._y2 - self._y1) // 2))
        return Point(x, y)