import Tkinter as tk
import os

# TODO: change the size of the windows to 320x 480
class window1:
    def __init__(self,master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.label = tk.Label(text = "Welcome to the hand me down pi").pack()
        self.ChooseLabel = tk.Label(text = "Please choose an option:").pack()
        self.button1 = tk.Button(self.frame, text = 'TV Mode', width = 25).pack()
        self.button2 = tk.Button(self.frame, text = 'Portable Mode', width = 25, command = self.new_window).pack()
        self.frame.pack()

    def new_window(self):
        self.newwindow = tk.Toplevel(self.master)
        self.app = PortableWindow(self.newwindow)
        self.master.withdraw()


class PortableWindow:
    def __init__(self,master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.button1 = tk.Button(self.frame, text = 'Calculator', width = 25, command = self.open_Cal).pack()
        self.button2 = tk.Button(self.frame, text = 'Timer', width = 25).pack()
        self.button3 = tk.Button(self.frame, text = 'Share Files', width = 25).pack()
        self.frame.pack()

    def close_windows(self):
        self.master.destroy()

    def open_Cal(self):
        # linux commands to destory this window and open the calculator
        self.master.destroy()
        cal = 'python Calculator.py'
        os.system(cal)


    # TODO: method to turn on bluetooth and add a file manager

# TODO: add a window for the Timer
    # TODO: add a goto back button
    # TODO: okay button for that window


def main():
    root = tk.Tk()
    app = window1(root)
    root.mainloop()

if __name__ == '__main__':
    main()
