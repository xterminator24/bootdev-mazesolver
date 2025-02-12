from graphics import Window

def main():
    print("opening window...")
    win = Window(800, 600)
    win.wait_for_close()

if __name__ == "__main__":
    main()