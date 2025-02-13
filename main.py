from graphics import Window, Line, Point

def main():
    print("opening window...")
    win = Window(800, 600)
    Window.draw_line(win, Line(Point(0,0), Point(25, 25)), "red")
    Window.draw_line(win, Line(Point(50,50), Point(100, 50)), "orange")
    Window.draw_line(win, Line(Point(300,20), Point(45, 400)), "blue")
    Window.draw_line(win, Line(Point(50,50), Point(400, 400)))
    win.wait_for_close()

if __name__ == "__main__":
    main()