import tkinter as tk
from tkinter import Canvas, Frame, BOTH

class HistogramViewer(tk.Frame):
   def __init__(self, master=None):
       super().__init__(master)
       self.master = master
       self.master.title('Histogram Viewer')
       self.pack(fill=BOTH, expand=1)

       canvas = Canvas(self)
       canvas.create_rectangle(60, 120, 210, 60, outline='darkolivegreen4', fill='darkolivegreen4')
       canvas.create_rectangle(60, 800, 160, 125, outline='cyan', fill='cyan')
       canvas.create_rectangle(60, 450, 360, 190, outline='gray40', fill='gray40')

       canvas.pack(fill=BOTH, expand=1)
       self.pack()

app_frame = tk.Tk()
app_frame.geometry('1920x1080')
histogram_viewer = HistogramViewer(master=app_frame)
histogram_viewer.mainloop()
