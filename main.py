# main.py
import sys

def main():
    if len(sys.argv) > 1 :
        from cli import app
        app.run()
    else:
        from gui import app
        app.run()

if __name__ == "__main__":
    main()
