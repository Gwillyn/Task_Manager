import tkinter as tk
from tkinter import ttk
import main
from datetime import date


def display():
    text_font = "JetBrainsMono Nerd Font"

    root = tk.Tk()
    root.title("Task Manager")
    root.geometry("600x600")

    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    style = ttk.Style()
    style.configure("TButton", font=(text_font, 12))

    # Main Frame
    mainframe = ttk.Frame(root)
    mainframe.grid(column=0, row=0, sticky=("nwes"))

    mainframe.columnconfigure(0, weight=1)

    # Header Frame
    headerframe = ttk.Frame(mainframe)
    headerframe.grid(column=0, row=1, sticky="ew", pady=(50, 80))
    headerframe.columnconfigure(0, weight=1)

    ttk.Label(
        headerframe, text="Task Manager", font=(text_font, 30, "bold"), anchor="center"
    ).grid(column=0, row=0)

    # Task Area
    taskframe = ttk.Frame(mainframe)
    taskframe.grid(column=0, row=0, sticky="ew")
    taskframe.columnconfigure(0, weight=1)
    taskframe.rowconfigure(0, weight=1)

    buttonframe = ttk.Frame(taskframe)
    buttonframe.grid(column=0, row=0, sticky="w")

    settings_button = ttk.Button(buttonframe, text="Settings")
    settings_button.grid(column=0, row=0, padx=(0, 1))

    make_task_button = ttk.Button(buttonframe, text="Make Task")
    make_task_button.grid(column=1, row=0, padx=(0, 1))

    calendar_button = ttk.Button(buttonframe, text="Calendar View")
    calendar_button.grid(column=2, row=0, padx=(0, 1))

    # List Area
    listframe = ttk.Frame(mainframe)
    listframe.grid(column=0, row=2, sticky="ew", padx=20)
    listframe.columnconfigure(0, weight=1)

    ttk.Label(listframe, text="Tasks: ", font=(text_font, 16, "bold")).grid(
        column=0, row=0, pady=10
    )

    eventsframe = ttk.Frame(listframe, borderwidth=20, relief="ridge")
    eventsframe.grid(column=0, row=0, sticky="ew")
    eventsframe.columnconfigure(0, weight=1)

    tasktree = ttk.Treeview(
        eventsframe, columns=("title", "due date", "description"), show="headings"
    )
    tasktree.heading("title", text="Title: ")
    tasktree.heading("due date", text="Due Date: ")
    tasktree.heading("description", text="Description: ")

    tasktree.column("title", width=120)
    tasktree.column("due date", width=120)
    tasktree.column("description", width=120)

    tasktree.grid(column=0, row=0, sticky="nwes", padx=20)

    for event in main.events:
        # Display time and date in a readable format
        event_time = event.due_time.strftime("%I:%M %p")
        event_date = event.due_date.strftime("%Y-%m-%d")

        if event.due_date == date.today():
            date_set = event_time + "  " + "Today"
        else:
            date_set = event_time + "  " + event_date

        # Insert the event details into the tree
        tasktree.insert("", "end", values=(event.title, date_set, event.description))

    root.mainloop()
