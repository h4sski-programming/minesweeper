from tkinter import *
from tkinter import ttk

from settings import Settings
settings = Settings()
print(settings.rows)

window = Tk()
window.title('Minesweeper')

frame = ttk.Frame(window, padding=10)
frame.grid()

input_value = 'a'
ttk.Label(frame, text='Hello h4sski').grid(column=0, row=0)
ttk.Button(frame, text='Quit', command=window.destroy).grid(column=0, row=1)
ttk.Label(frame, textvariable=input_value).grid(column=0, row=2)

mine_frame = ttk.Frame(window, padding=10)
mine_frame.grid()


for i in range(settings.columns):
    for j in range(settings.rows):
        ttk.Button(mine_frame, text=i*j, width=3).grid(column=i, row=j)

window.mainloop()