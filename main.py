import tkinter as tk
from tkinter import ttk
from datetime import date
from event import Event

# Testing event
e1 = Event("Meeting", date(2026, 4, 2), "A meeting")
e2 = Event("Gym", date(2026, 4, 2), "Gym visit")
e3 = Event("Meeting", date(2026, 4, 2), "A meeting")
e4 = Event("Store", date(2026, 4, 2), "Go to store")
events = []
events.append(e1)
events.append(e2)
events.append(e3)
events.append(e4)


def main():
    text_font = "JetBrainsMono Nerd Font"

    root = tk.Tk()
    root.title("Task Manager")
    root.geometry("600x600")

    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    style = ttk.Style()
    style.configure("TButton", font=(text_font, 12))

    # Main Frame
    mainframe = ttk.Frame(root, padding=(12, 12, 12, 12))
    mainframe.grid(column=0, row=0, sticky=("nwes"))

    mainframe.columnconfigure(0, weight=1)

    # Header Frame
    headerframe = ttk.Frame(mainframe)
    headerframe.grid(column=0, row=1, sticky="ew", pady=(50, 50))
    headerframe.columnconfigure(0, weight=1)

    ttk.Label(
        headerframe, text="Task Manager", font=(text_font, 20, "bold"), anchor="center"
    ).grid(column=0, row=0)

    # Task Area
    taskframe = ttk.Frame(mainframe)
    taskframe.grid(column=0, row=0, sticky="ew")
    taskframe.columnconfigure(0, weight=1)
    taskframe.rowconfigure(0, weight=1)

    buttonframe = ttk.Frame(taskframe)
    buttonframe.grid(column=0, row=0, sticky="ew")

    settings_button = ttk.Button(buttonframe, text="Settings")
    settings_button.grid(column=0, row=0, padx=15)

    make_task_button = ttk.Button(buttonframe, text="Make Task")
    make_task_button.grid(column=1, row=0, padx=15)

    calendar_button = ttk.Button(buttonframe, text="Calendar View")
    calendar_button.grid(column=2, row=0, padx=15)

    # List Area
    listframe = ttk.Frame(mainframe)
    listframe.grid(column=0, row=2, sticky="ew")
    listframe.columnconfigure(0, weight=1)

    ttk.Label(listframe, text="Tasks: ", font=(text_font, 16, "bold")).grid(
        column=0, row=0, pady=10
    )

    eventsframe = ttk.Frame(listframe)
    eventsframe.grid(column=0, row=0, sticky="ew", pady=20)
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

    tasktree.grid(column=0, row=0, sticky="nwes", padx=50)

    for event in events:
        tasktree.insert("", "end", values=(event.title, "2026", event.description))

    root.mainloop()


if __name__ == "__main__":
    main()
