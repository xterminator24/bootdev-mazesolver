from graphics import Window, Line, Point
from cell import Cell

def main():
    print("opening window...")
    win = Window(800, 600)
       
    cell = Cell(win)
    cell.draw(100, 150, 150, 200)

    cell = Cell(win)
    cell.draw(150, 150, 200, 200)

    cell = Cell(win)
    cell.has_bottom_wall = False
    cell.has_left_wall = False
    cell.draw(200, 150, 250, 200)

    cell = Cell(win)
    cell.has_top_wall = False
    cell.has_right_wall = False
    cell.draw(250, 150, 300, 200)
    
    win.wait_for_close()

if __name__ == "__main__":
    main()