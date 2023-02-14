import tkinter as tk

class Application(tk.Frame):
   def __init__(self, master=None):
       super().__init__(master)
       self.master = master

       # Set the frame's title
       self.master.title('My first framwork(:')
       self.pack()

app_frame = tk.Tk()

# Set the frame's width (400) and height (250) in pixels
app_frame.geometry('720x720')

# Make the frame visible to the user
app = Application(master=app_frame)
app.mainloop()
