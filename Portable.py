import Tkinter as tk
import os

def Open_Retro():
    global piGaming
    def Gaming():
        # change paths so I am able to boot into retropie
        # changePath = os.chdir('cd/RetroPie-Setup')
        # TODO: running retro pi configuration file
        #os.system(changePath)
        #execute the command to enter the setup so you are able to boot into Retropie
        #Changeboot="sudo ./retropie_setup.sh"
        #os.system.(Changeboot)

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
        self.master.withdraw()

class PortableWindow:
    def __init__(self,master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.button3 = tk.Button(self.frame, text = 'Camera Mode', width = 25, command = self.Open_Camera).pack()
        # Watching on a small screen
        self.button4 = tk.Button(self.frame, text = 'Portable mode', width = 25,command = self.close_window).pack()
        self.button5 = tk.Button(self.frame, text = 'Share Files', width = 25).pack()
        self.button6 = tk.Button(self.frame, text = 'Portable gaming', width = 25).pack()
        self.frame.pack()

    def close_window(self):
        self.master.destroy()

    # TODO: method to open the camera window
    def Open_Camera(self):
        self.cam_window = tk.Toplevel(self.master)
        self.app = CameraWindow(self.cam_window)
        self.master.withdraw()
    # TODO: method to turn on bluetooth and add a file manager




class TVMode:
    def __init__(self,master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.button7 = tk.Button(self.frame, text = 'Media', width = 25).pack()
        self.button8 = tk.Button(self.frame, text = 'Desktop watching video', width = 25).pack()
        self.button9 = tk.Button(self.frame, text = 'Retro Gaming', width = 25).pack()
        self.frame.pack()
    

#CameraWindow class
class CameraWindow:
    def __init__(self,master):
        self.master = master
        self.frame = tk.Frame(self.master)
        #TODO: set the size of make a frame for the image to display
        #TODO: set a button to take photos
        self.button10 = tk.Button(self.frame, text = 'Photo', width = 10).pack()
        #TODO: set a button to take videos
        self.frame.pack()
    
    #TODO: Method to execute the command to take a photo
    


def main():
    root = tk.Tk()
    app = window1(root)
    root.mainloop()

if __name__ == '__main__':
    main()
