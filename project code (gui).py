import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("1200x800")

#photo = tk.PhotoImage(file="strava.png")

def make_label(parent, img):
    label = tk.Label(parent, image=img)


menuframe = tk.Frame(root, bg="forest green")
map_frame = tk.Frame(root, bg="wheat3")
weather_frame = tk.Frame(root, bg="cornsilk3")
reviews_frame = tk.Frame(root, bg="green")
info_frame = tk.Frame(root, bg="beige")

presaved_routes_frame = tk.Frame(root, bg="red")

newroutes_frame = tk.Frame(root, bg="blue")

#logo_label = make_label(menuframe, photo)

logo_label = tk.Label(menuframe, bg="gray60", font=("aquagrotesque", 10))
newroute_button = tk.Button(menuframe, bg="lawn green", text="FIND NEW ROUTE", font=("aquagrotesque", 10, "bold"))
savedroute_button = tk.Button(menuframe, bg="lawn green", text="SAVED ROUTEs", font=("aquagrotesque", 10, "bold"))
create_button = tk.Button(menuframe, bg="lawn green", text="CREATE NEW ROUTE", font=("aquagrotesque", 10, "bold"))
back_button = tk.Button(menuframe, bg="lawn green", text="<--")
forwward_button = tk.Button(menuframe, bg="lawn green", text="-->")

def savedroutes_pressed():
    presaved_routes_frame.grid(row=0, column=0, sticky="nesw", columnspan=6, rowspan=2)

def find_new_routes_pressed():
    newroutes_frame.grid(row=0, column=0, sticky="nesw", columnspan=6, rowspan=2)

def createroute_pressed():
    menuframe.grid(row=0, column=0, sticky="nesw", rowspan=2)
    map_frame.grid(row=0, column=1, sticky="nesw", columnspan=4)
    weather_frame.grid(row=0, column=5, sticky="nesw", columnspan=4)
    reviews_frame.grid(row=1, column=1, sticky="nesw", columnspan=4)
    info_frame.grid(row=1, column=5, sticky="nesw", columnspan=4)





logo_label.grid(row=0, column=0, sticky="nesw", columnspan=2)
newroute_button.grid(row=1, column=0, sticky="nesw", columnspan=2)
savedroute_button.grid(row=2, column=0, sticky="nesw", columnspan=2)
create_button.grid(row=3, column=0, sticky="nesw", columnspan=2)
back_button.grid(row=4, column=0, sticky="nesw")
forwward_button.grid(row=4, column=1, sticky="nesw")



root.columnconfigure(0, weight=8)
root.columnconfigure(1, weight=8)
root.columnconfigure(2, weight=8)
root.columnconfigure(3, weight=8)
root.columnconfigure(4, weight=8)
root.columnconfigure(5, weight=8)
root.columnconfigure(6, weight=8)
root.columnconfigure(7, weight=8)
root.rowconfigure(0, weight=2)
root.rowconfigure(1, weight=2)

menuframe.columnconfigure(0, weight=2)
menuframe.columnconfigure(1, weight=2)

menuframe.rowconfigure(0, weight=5)
menuframe.rowconfigure(1, weight=5)
menuframe.rowconfigure(2, weight=5)
menuframe.rowconfigure(3, weight=5)
menuframe.rowconfigure(4, weight=5)



root.mainloop()