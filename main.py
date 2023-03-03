from tkinter import *
from tkinter import ttk
from map import Map

from settings import Settings
settings = Settings()

window = Tk()
window.title('Minesweeper')

frame = ttk.Frame(window, padding=10)
frame.grid()

input_value = StringVar()
ttk.Label(frame, text='Hello h4sski').grid(column=0, row=0)
ttk.Button(frame, text='Quit', command=window.destroy).grid(column=0, row=1)
ttk.Entry(frame, textvariable=input_value).grid(column=0, row=2)

mine_frame = ttk.Frame(window, padding=10)
mine_frame.grid()

map = Map()
map.generate_new_map()
for i in range(settings.rows):
    for j in range(settings.columns):
        ttk.Button(mine_frame, text=map.mines[i][j], width=3).grid(row=i, column=j)

window.mainloop()