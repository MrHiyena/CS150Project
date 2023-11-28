# https://www.geeksforgeeks.org/python-gui-tkinter/
# Outline of the GUI is by OpenAI
import tkinter as tk
from tkinter import filedialog

# Function to prompt the Ready status and control delay
def set_playing_status():
    status_label.config(text="Ready...")


# Function to handle the Play button click
def play_button_click():
    status_label.config(text="Playing...")


    # Delays after 2 seconds
    root.after(4000, set_playing_status)

# Function to handle the Record button click
def record_button_click():
    status_label.config(text="Recording...")

# Function to handle the Browse button click
def browse_button_click():
    file_path = filedialog.askopenfilename()
    if file_path:
        status_label.config(text=f"Selected file: {file_path}")

# Create the main window
root = tk.Tk()
root.title("Audio Recorder and Player")

# Create labels
status_label = tk.Label(root, text="Status: Ready")
status_label.pack()

# Create buttons
play_button = tk.Button(root, text="Play", command=play_button_click)
record_button = tk.Button(root, text="Record", command=record_button_click)
browse_button = tk.Button(root, text="Browse", command=browse_button_click)

play_button.pack()
record_button.pack()
browse_button.pack()

# Start the main event loop
root.mainloop()

