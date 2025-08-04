import sys

def main():
    if len(sys.argv) > 1 :
        splash.destroy()
        from cli import app
        app.run()
    else:
        import tkinter as tk

        splash = tk.Tk()
        splash.geometry("300x100")
        splash.title("Loading...")
        tk.Label(splash, text="Starting application...").pack(expand=True)
        splash.update()

        from gui import app
        app.run(splash)

if __name__ == "__main__":
    main()
