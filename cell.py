from graphics import Line, Point, Window

class Cell():
    def __init__(self, win: Window):
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
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        if self.has_left_wall:
            top_point = Point(x1, y1)
            bottom_point = Point(x1, y2)
            line = Line(top_point, bottom_point)
            self._win.draw_line(line)

        if self.has_right_wall:
            top_point = Point(x2, y1)
            bottom_point = Point(x2, y2)
            line = Line(top_point, bottom_point)
            self._win.draw_line(line)

        if self.has_top_wall:
            left_point = Point(x1, y1)
            right_point = Point(x2, y1)
            line = Line(left_point, right_point)
            self._win.draw_line(line)

        if self.has_bottom_wall:
            left_point = Point(x1, y2)
            right_point = Point(x2, y2)
            line = Line(left_point, right_point)
            self._win.draw_line(line)