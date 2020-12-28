
import Tkinter as tk
import os

# TODO: Setting the size of the windows
# TODO: add this to the start up script
class Demo1:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.label = tk.Label(text = "Welcome to Your Camera")
        self.label.pack()
        self.ChooseLabel = tk.Label(text = "Please choose an option:")
        self.ChooseLabel.pack()
        self.button1 = tk.Button(self.frame, text = 'Choose a mode', width = 25, command = self.new_window)
        self.button1.pack()
        self.button2 = tk.Button(self.frame, text = 'Transferring Photos', width = 25 , command = self.File_Transfer)
        self.button2.pack()

        # TODO: button to sharefiles
        self.frame.pack()

    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Demo2(self.newWindow)
        self.master.withdraw()

    # TODO: Method open file manager and bluetooth
    def File_Transfer(self):
        os.system('systemctl start bluetooth')
        print("bluetooth on")


class Demo2:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)

        self.QuestionLabel = tk.Label(self.frame, text = "What would you like to do")
        self.QuestionLabel.pack()

        # TODO: link the camera to the camera software and exeacute a linux command
        self.CameraButton = tk.Button(self.frame, text= 'Camera mode', width = 25,command = self.test)
        self.CameraButton.pack()

        # TODO: Force the windows to close and boot to the normal window
        self.WorkingButton = tk.Button(self.frame, text= 'Desktop mode', width = 25)
        self.WorkingButton.pack()

        self.TvButton = tk.Button(self.frame,text= 'Media Mode', width = 25)
        self.TvButton.pack()

        # TODO: Command force the code to confugure the retropie .sh file
        self.GamingButton = tk.Button(self.frame, text= 'Gaming Mode', width = 25)
        self.GamingButton.pack()

        #self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows).pack()
        self.frame.pack()

    def close_windows(self):
        self.master.destroy()

    # TODO: execute the Raspberry pi retropie configuration
    # TODO: Destory the main root
    def test(self):
        changePath = os.chdir('Po')
        cmd = 'ls'
        os.system(cmd)


# TODO: window for camera interface
# TODO: button to scanner
# TODO: button to take a photo
# TODO: button to record videos


def main():
    root = tk.Tk()
    app = Demo1(root)
    root.mainloop()



if __name__ == '__main__':
    main()
