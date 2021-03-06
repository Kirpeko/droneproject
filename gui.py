
# Use "pip install python-tk" if tkinter is not installed

# Import tkinter module for creating gui
import tkinter as tk

# Import Roy's Tello abridged module
import tello_abridged as ta

# Import Tello module
import tello as tell

# Create handles for the Tello class in both tello.py and tello_abridged.py files
t = ta.Tello()
tel = tell.Tello()


# Import tkinter module for creating gui
import tkinter as tk


# creating the actual window
window = tk.Tk()

# Create grid for everything

window.columnconfigure([0, 1, 2, 3, 4, 5], minsize=150)
window.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7], minsize=50)

"""CM and Degree/Updates to each"""

# creating entry widgets and headers for cm and degrees
cm_label = tk.Label(text="Centimetres (20 - 500)")
cm_entry = tk.Entry()

cm = 20
cm_entry.insert(0, 20)  # Set default entry for cm

degree_label = tk.Label(text="Degrees (1 - 360)")
degree_entry = tk.Entry()
degree = 45
degree_entry.insert(0, 45)  # Set default entry for degree
degree_label = tk.Label(text="Degrees (1 - 360)")
degree_entry = tk.Entry()

cm_label.grid(row=0, column=0, sticky="w")
cm_entry.grid(row=1, column=0, sticky="n")
degree_label.grid(row=0, column=2)
degree_entry.grid(row=1, column=2, sticky="n")

# Create update buttons for the entry values of cm and degree (2 separate ones to look cleaner next to entries)
update_cm = tk.Button(
    text="✓",
    width=1,
    height=1
    height=1,
)

update_degree = tk.Button(
    text="✓",
    width=1,
    height=1
    height=1,
)
update_cm.grid(row=0, column=0, sticky="e")
update_degree.grid(row=0, column=2, sticky="e")


# Define the function to get the entry values when clicking the update button
# if cm is out of range, if statements are setup to push it back into the range
def entry_cm(event):
    global cm  # Set it to actually interact with our created "cm" variable
    cm = cm_entry.get()
    if not cm.isnumeric():
        cm = 20
        cm_entry.delete(0, tk.END)
        cm_entry.insert(0, cm)
    cm = float(cm)
    if cm < 20:
        cm = 20
        cm_entry.delete(0, tk.END)
        cm_entry.insert(0, cm)
    elif cm > 500:
        cm = 500
        cm_entry.delete(0, tk.END)
        cm_entry.insert(0, cm)
    print(cm)


def entry_degree(event):
    global degree  # Set it to actually interact with our created "degree" variable
    degree = degree_entry.get()
    if not degree.isnumeric():
        degree = 90
        degree_entry.delete(0, tk.END)
        degree_entry.insert(0, degree)
    degree = float(degree)
    if degree < 1:
        degree = 1
        degree_entry.delete(0, tk.END)
        degree_entry.insert(0, degree)
    elif degree > 360:
        degree = 360
        degree_entry.delete(0, tk.END)
        degree_entry.insert(0, degree)
    print(degree)


# set button Presses for both entries
update_cm.bind("<Button-1>", entry_cm)
update_degree.bind("<Button-1>", entry_degree)

""" Start of Engine related """
# Create a take off button
takeoff = tk.Button(
    text="Take Off",
    width=10,
    height=2,
    bg="cyan",
)
takeoff.grid(row=3, column=0, sticky="nsew", padx=2, pady=2)

# Create a land button
land = tk.Button(
    text="Land",
    width=10,
    height=2,
    bg="#D2691E",
)
land.grid(row=4, column=0, sticky="nsew", padx=2, pady=2)

# Create a Cut Engine button button
cut_engine = tk.Button(
    text="PANIC",
    width=10,
    height=2,
    bg="red",
    fg="white"
)
cut_engine.grid(row=5, column=0, sticky="nsew", padx=2, pady=2)


# Define event handling for each button when clicked (Temporary Print to console for testing)
def button_takeoff(event):
    print("Take Off initiated")
    tel.takeoff()




takeoff.bind("<Button-1>", button_takeoff)


def button_land(event):
    print("Landing Initiated")
    t.land()



land.bind("<Button-1>", button_land)


def button_cut_engine(event):
    print("EMERGENCY! ENGINE HAS BEEN CUT")
    t.emergency()




cut_engine.bind("<Button-1>", button_cut_engine)

"""Start of Directional"""

# Create rotational buttons

button_rotate_cw = tk.Button(
    text="⟳",
    width=3,
    height=2
)
button_rotate_cw.grid(row=3, column=4, sticky="nesw", padx=2, pady=2)


def rotate_cw(event):
    print("Rotate clockwise {} degrees".format(degree))
    tel.rotate_clockwise(degree)
    print("Rotate clockwise")



button_rotate_cw.bind("<Button-1>", rotate_cw)

button_rotate_ccw = tk.Button(
    text="⟲",
    width=3,
    height=2
)
button_rotate_ccw.grid(row=3, column=2, sticky="nesw", padx=2, pady=2)


def rotate_ccw(event):
    print("Rotate counter-clockwise {} degrees".format(degree))
    tel.rotate_counterclockwise(degree)
    print("Rotate counter-clockwise")



button_rotate_ccw.bind("<Button-1>", rotate_ccw)

# Create directional buttons
button_forward = tk.Button(
    text="⮉",
    width=3,
    height=2,
)
button_forward.grid(row=4, column=3, sticky="nesw", padx=2, pady=2)


def forward(event):
    print("move forward {}cm".format(cm))
    tel.fly_forward(cm)
    print("move forward")



button_forward.bind("<Button-1>", forward)

button_back = tk.Button(
    text="⮋",
    width=3,
    height=2,
)
button_back.grid(row=5, column=3, sticky="nesw", padx=2, pady=2)


def back(event):
    print("move backward {}cm".format(cm))
    tel.fly_backward(cm)
    print("move backward")



button_back.bind("<Button-1>", back)

button_up = tk.Button(
    text="🢁",
    width=3,
    height=2,
)
button_up.grid(row=3, column=3, sticky="nesw", padx=2, pady=2)


def up(event):
    print("move up {}cm".format(cm))
    tel.fly_up(cm)
    print("move up")



button_up.bind("<Button-1>", up)

button_left = tk.Button(
    text="🢀",
    width=3,
    height=2,
)
button_left.grid(row=4, column=2, sticky="nesw", padx=2, pady=2)


def left(event):
    print("move left {}cm".format(cm))
    tel.fly_left(cm)
    print("move left")



button_left.bind("<Button-1>", left)

button_right = tk.Button(
    text="🢂",
    width=3,
    height=2,
)
button_right.grid(row=4, column=4, sticky="nesw", padx=2, pady=2)


def right(event):
    print("move right {}cm".format(cm))
    tel.fly_right(cm)
    print("move right")



button_right.bind("<Button-1>", right)

button_down = tk.Button(
    text="🢃",
    width=3,
    height=2,
)
button_down.grid(row=6, column=3, sticky="nesw", padx=2, pady=2)


def down(event):

    print("move down {}cm".format(cm))
    tel.fly_down(cm)
    print("move down")



button_down.bind("<Button-1>", down)

# Running a loop of our window which will continuously look for inputs to execute until window is exited
window.mainloop()
