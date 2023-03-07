# import tkinter as tk

# win = tk.Tk()
# max_amount = 0
# label1 = None #just so it is defined

# def fun():
#     global max_amount, label1
#     max_amount +=100
#     label1.configure(text='Balance :$' + str(max_amount))

# btn = tk.Button(win,text = 'Change', command = fun)
# btn.grid()
# t1 =str(max_amount)
# label1 = tk.Label(win,text = 'Balance :$' + t1)
# label1.grid()

# win.mainloop()


# import tkinter as tk

# def remove_button():
#     global label
#     # Get the grid parameters passed in button when it was created
#     button_grid_info = button.grid_info()
#     button.grid_forget()
#     label = tk.Label(button_grid_info["in"], text="This is a Label widget")
#     # Put the label exactly where the button was:
#     label.grid(**button_grid_info)

# root = tk.Tk()

# button = tk.Button(root, text="Click me", command=remove_button)
# button.grid(row=1, column=1)

# root.mainloop()


# 
# from tkinter import *
# from tkinter import ttk

# class Main():
#     def __init__(self) -> None:
#         self.window = Tk()
#         self.window.title('Testing')
        
#         self.frame = ttk.Frame(self.window, padding=10)
#         self.frame.grid()
        
#         self.label1 = ttk.Label(self.frame, text='Hello from the testing.py')
#         self.label1.grid()
#         self.label2 = ttk.Label(self.frame, text='2nd Layout without grid atributes')
#         self.label2.grid()
#         self.button = ttk.Button(self.frame, text='remove 1st line')
#         self.button['command'] =  self.label1.destroy
#         self.button.grid()
        
        
#         self.window.mainloop()
    
# Main()




# 
tuple = ((1, 2), (1, 2), (1, 2), (1, 2), (1, 2))

for t in tuple:
    print(t)
    for a in t:
        print(a)