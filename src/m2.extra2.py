import tkinter
from tkinter import ttk

def get_my_drive_frame(window, mqtt_sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()
    frame_label = ttk.Label(frame, text="A Robot-deliveryman")
    Speed_label = ttk.Label(frame,text="How fast do you want me to drive?")

    Speed_entry= ttk.Entry(frame,width=8)
    Speed_entry.insert(0,"100")

    Drive_button=ttk.Button(frame, text="I want to drink some water")
    Stop_button = ttk.Button(frame, text="I'm not thirsty now")

    frame_label.grid(row=0,column=1)
    Speed_label.grid(row=3,column=0)
    Speed_entry.grid(row=4,column=0)
    Drive_button.grid(row=2,column=2)
    Stop_button.grid(row=4,column=2)

    return frame



