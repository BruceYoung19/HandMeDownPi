import Tkinter as tk
import os

def Open_Retro():
    global piGaming
    def Gaming():
        # change paths so I am able to boot into retropie
        changePath = os.chdir('Retropi')
        # TODO: running retro pi configuration file
        os.system(changePath)



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
        self.button4 = tk.Button(self.frame, text = 'Portable mode', width = 25,command = self.close_window).pack()
        self.button5 = tk.Button(self.frame, text = 'Share Files', width = 25).pack()
        self.button6 = tk.Button(self.frame, text = 'Portable gaming', width = 25).pack()
        self.frame.pack()

    def close_window(self):
        self.master.destroy()

    # TODO: method to open the camera window
    # TODO: method to turn on bluetooth and add a file manager

#CameraWindow class

class TVMode:
    def __init__(self,master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.button7 = tk.Button(self.frame, text = 'Media', width = 25).pack()
        self.button8 = tk.Button(self.frame, text = 'Desktop watching video', width = 25).pack()
        self.button9 = tk.Button(self.frame, text = 'Retro Gaming', width = 25).pack()
        self.frame.pack()



def main():
    root = tk.Tk()
    app = window1(root)
    root.mainloop()

if __name__ == '__main__':
    main()
