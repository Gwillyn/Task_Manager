import event
import tkinter as tk
from tkinter import ttk
from datetime import date, datetime
import ics_manager as ics
from tkcalendar import Calendar


text_font = "JetBrainsMono Nerd Font"
dark_mode = False


def main_display():

    root = tk.Tk()
    root.title("Task Manager")
    root.geometry("900x800")

    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    style = ttk.Style()
    style.configure("TButton", font=(text_font, 12))
    style.configure("TNotebook.Tab", font=(text_font, 12, "bold"))

    # Main Frame
    mainframe = ttk.Frame(root)
    mainframe.grid(column=0, row=0, sticky=("nwes"))

    mainframe.columnconfigure(0, weight=1)
    mainframe.columnconfigure(1, weight=1)
    mainframe.columnconfigure(2, weight=1)
    mainframe.rowconfigure(1, weight=1)

    # Header Frame
    headerframe = ttk.Frame(mainframe)
    headerframe.grid(column=1, row=0, sticky="ew", pady=(80, 70))
    headerframe.columnconfigure(0, weight=1)

    ttk.Label(
        headerframe,
        text="Task Manager",
        font=(text_font, 30, "bold"),
        anchor="center",
    ).grid(column=0, row=0)

    # Task Area
    taskframe = ttk.Frame(mainframe)
    taskframe.grid(column=1, row=1, sticky="new")
    taskframe.columnconfigure(0, weight=1)
    taskframe.rowconfigure(0, weight=1)

    buttonframe = ttk.Frame(taskframe)
    buttonframe.grid(column=1, row=0, sticky="ne", padx=(0, 30), pady=(50, 0))

    settings_button = ttk.Button(
        buttonframe, text="Settings", command=lambda: settings_display(root)
    )
    settings_button.grid(column=0, row=1, pady=30, ipadx=10)

    create_task_button = ttk.Button(
        buttonframe, text="Create Task", command=lambda: create_display(root, tasktree)
    )
    create_task_button.grid(column=0, row=0, ipadx=1)

    # Notebook for list and calendar view
    notebook = ttk.Notebook(taskframe)
    notebook.grid(column=0, row=0, sticky="nsew", padx=30)

    # List Area
    listframe = ttk.Frame(notebook)
    listframe.columnconfigure(0, weight=1)
    listframe.rowconfigure(1, weight=1)

    notebook.add(listframe, text="List: ")

    ttk.Label(listframe, text="Tasks: ", font=(text_font, 16, "bold")).grid(
        column=0, row=0, pady=10
    )

    eventsframe = ttk.Frame(listframe, borderwidth=20, relief="ridge")
    eventsframe.grid(column=0, row=0, sticky="ew")
    eventsframe.columnconfigure(0, weight=1)
    eventsframe.rowconfigure(0, weight=1)

    tasktree = ttk.Treeview(
        eventsframe, columns=("title", "due date", "description"), show="headings"
    )
    tasktree.heading("title", text="Title: ")
    tasktree.heading("due date", text="Due Date: ")
    tasktree.heading("description", text="Description: ")

    tasktree.column("title", width=60)
    tasktree.column("due date", width=120)
    tasktree.column("description", width=120)

    tasktree.grid(column=0, row=0, sticky="nwes", padx=20, pady=(0, 20))

    refresh_tasks(tasktree)

    calendarframe = ttk.Frame(notebook)
    calendarframe.columnconfigure(0, weight=1)

    notebook.add(calendarframe, text="Calendar: ")

    root.mainloop()


def settings_display(root, width=600, height=400):
    settings_pop = popup_window(root, "Settings", width, height)

    ttk.Label(settings_pop, text="> SETTINGS", font=(text_font, 25, "bold")).grid(
        column=0, row=0, padx=(10, 0)
    )

    import_button = ttk.Button(
        settings_pop,
        text="Import ICS",
        command=ics.import_ics,
    )
    import_button.grid(column=0, row=1)

    export_button = ttk.Button(
        settings_pop, text="Export ICS", command=lambda: ics.export_ics()
    )
    export_button.grid(column=0, row=2)

    theme_button = ttk.Button(settings_pop, text="Theme")
    theme_button.grid(column=1, row=1)


def create_display(root, tasktree, width=600, height=600):
    create_pop = popup_window(root, "Create Task", width, height)

    ttk.Label(create_pop, text="> Create Task", font=(text_font, 25, "bold")).grid(
        column=0, row=0, pady=(0, 20), padx=(10, 0)
    )
    # Title entry
    ttk.Label(create_pop, text="Title: ", font=(text_font, 16)).grid(
        column=0, row=1, sticky="w", padx=(10, 0)
    )
    title_entry = ttk.Entry(create_pop, width=30)
    title_entry.grid(column=0, row=2)

    # Description Entry
    ttk.Label(create_pop, text="Description: ", font=(text_font, 16)).grid(
        column=0, row=3, sticky="w", pady=(40, 0), padx=(10, 0)
    )
    desc_entry = ttk.Entry(create_pop, width=30)
    desc_entry.grid(column=0, row=4)

    # Due date and time entry
    ttk.Label(create_pop, text="Time: ", font=(text_font, 16)).grid(
        column=1, row=1, sticky="w", padx=(10, 0)
    )

    hour = tk.StringVar(value="12")
    minute = tk.StringVar(value="00")
    ampm = tk.StringVar(value="AM")

    hour_box = ttk.Spinbox(create_pop, from_=1, to=12, textvariable=hour, width=10)
    minute_box = ttk.Spinbox(create_pop, from_=0, to=59, textvariable=minute, width=10)
    ampm_box = ttk.Combobox(
        create_pop,
        values=["AM", "PM"],
        textvariable=ampm,
        width=5,
        state="readonly",
        height=10,
    )

    hour_box.grid(column=1, row=2, sticky="w", padx=(25, 0))
    colon_box = ttk.Label(create_pop, text=":", font=(text_font, 16)).grid(
        column=2, row=2, sticky="w"
    )
    minute_box.grid(column=3, row=2, sticky="w")
    ampm_box.grid(column=4, row=2, sticky="w")

    date_entry = Calendar(create_pop, selectmode="day")
    date_entry.grid(column=1, row=4, padx=(20, 0), columnspan=3, rowspan=3)

    def submit_handler():
        print("Submitted")
        hours = int(hour.get())
        minutes = int(minute.get())
        ampms = ampm.get()

        if ampms == "PM" and hours != 12:
            hours += 12
        elif ampms == "AM" and hours == 12:
            hours = 0

        full_time = datetime.strptime(f"{hours}:{minutes}", "%H:%M").time()
        stripped_date = datetime.strptime(date_entry.get_date(), "%m/%d/%y")

        event.save_event(
            title_entry.get(),
            desc_entry.get(),
            datetime.combine(stripped_date.date(), full_time),
        )
        refresh_tasks(tasktree)
        create_pop.destroy()

    # Submit
    submit = ttk.Button(create_pop, text="Submit", command=submit_handler)
    submit.grid(column=0, row=8)


def popup_window(root, title, width, height):
    name = tk.Toplevel(root)
    name.title(title)

    # This grabs the new window and opens it in the middle of the screen.
    # also, it lets any window managers know to keep the window floating
    name.transient(root)
    name.grab_set()
    name.wm_attributes(
        "-type", "utility"
    )  # lets WM know to float window since it is read as a utility
    screen_w = name.winfo_screenwidth()
    screen_h = name.winfo_screenheight()
    x = (screen_w // 2) - (width // 2)
    y = (screen_h // 2) - (height // 2)
    name.geometry(f"{width}x{height}+{x}+{y}")
    return name


def refresh_tasks(tasktree):
    for item in tasktree.get_children():
        tasktree.delete(item)

    for e in event.events:
        # Display time and date in a readable format
        event_time = e.due_time.strftime("%I:%M %p")
        event_date = e.due_date.strftime("%Y-%m-%d")

        if e.due_date == date.today():
            date_set = event_time + "  " + "Today"
        else:
            date_set = event_time + "  " + event_date

        # Insert the event details into the tree
        tasktree.insert("", "end", values=(e.title, date_set, e.description))
