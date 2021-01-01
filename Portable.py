import Tkinter as tk
import os


# TODO: change the size of the windows to 320x 480
class window1:
    def __init__(self,master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.label = tk.Label(text = "Welcome to the hand me down pi").pack()
        self.ChooseLabel = tk.Label(text = "Please choose an option:").pack()
        self.button1 = tk.Button(self.frame, text = 'TV Mode', width = 25, command = self.Open_TVmode).pack()
        self.button2 = tk.Button(self.frame, text = 'Portable Mode', width = 25, command = self.new_window).pack()
        self.frame.pack()

    def new_window(self):
        self.newwindow = tk.Toplevel(self.master)
        self.app = PortableWindow(self.newwindow)
        self.master.withdraw()

    def Open_TVmode(self):
        self.new_window = tk.Toplevel(self.master)
        self.app = TVMode(self.new_window)
        self.master.destory()



class PortableWindow:
    def __init__(self,master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.button3 = tk.Button(self.frame, text = 'Camera Mode', width = 25).pack()
        # Watching on a small screen
        self.button4 = tk.Button(self.frame, text = 'Portable mode', width = 25).pack()
        self.button5 = tk.Button(self.frame, text = 'Share Files', width = 25).pack()
        self.frame.pack()

    def close_windows(self):
        self.master.destroy()



    # TODO: method to turn on bluetooth and add a file manager

class TVMode:
    def __init__(self,master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.button6 = tk.Button(self.frame, text = 'Media', width = 25).pack()
        self.button7 = tk.Button(self.frame, text = 'Desktop watching video', width = 25).pack()
        self.frame.pack()



def main():
    root = tk.Tk()
    app = window1(root)
    root.mainloop()

if __name__ == '__main__':
    main()
