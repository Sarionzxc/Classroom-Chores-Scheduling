import tkinter as tk
from build.login_page.gui import  LoginPage 


root = tk.Tk()  # Make temporary window for app to start
root.withdraw()  


if __name__ == "__main__":

    LoginPage()
    #mainWindow()

    root.mainloop()


#This main.py 