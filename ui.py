from io import text_encoding
import event
import calendar
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from datetime import date
from datetime import datetime


text_font = "JetBrainsMono Nerd Font"
dark_mode = False


def main_display():

    root = tk.Tk()
    root.title("Task Manager")
    root.geometry("800x600")

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
        buttonframe, text="Create Task", command=lambda: create_display(root)
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

    calendarframe = ttk.Frame(notebook)
    calendarframe.columnconfigure(0, weight=1)

    notebook.add(calendarframe, text="Calendar: ")

    root.mainloop()


def settings_display(root, width=600, height=400):
    settings_pop = tk.Toplevel(root)
    settings_pop.title("Settings")

    # This grabs the new window and opens it in the middle of the screen.
    # also, it lets any window managers know to keep the window floating
    settings_pop.transient(root)
    settings_pop.grab_set()
    settings_pop.wm_attributes(
        "-type", "utility"
    )  # lets WM know to float window since it is read as a utility
    screen_w = settings_pop.winfo_screenwidth()
    screen_h = settings_pop.winfo_screenheight()
    x = (screen_w // 2) - (width // 2)
    y = (screen_h // 2) - (height // 2)
    settings_pop.geometry(f"{width}x{height}+{x}+{y}")

    ttk.Label(settings_pop, text="> SETTINGS", font=(text_font, 25, "bold")).grid(
        column=0, row=0, padx=(10, 0)
    )

    import_button = ttk.Button(
        settings_pop,
        text="Import ICS",
        command=import_ics,
    )
    import_button.grid(column=0, row=1)

    export_button = ttk.Button(
        settings_pop, text="Export ICS", command=lambda: export_ics()
    )
    export_button.grid(column=0, row=2)

    theme_button = ttk.Button(settings_pop, text="Theme")
    theme_button.grid(column=1, row=1)


def import_ics():
    file_path = filedialog.askopenfilename(
        filetypes=[("ICS files", "*.ics"), ("All files", "*.*")]
    )
    if file_path:
        # Process file
        print(file_path)


def export_ics():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".ics",
        filetypes=[("ICS files", "*.ics"), ("All files", "*.*")],
        title="Save calendar as ICS",
    )

    if not file_path:
        return

    lines = ["BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//Task Manager//EN"]

    for e in event.events:
        start_dt = datetime.combine(e.start_date, e.start_time)
        end_dt = datetime.combine(e.due_date, e.due_time)

        dtstart = start_dt.strftime("%Y%m%dT%H%M%S")
        dtend = end_dt.strftime("%Y%m%dT%H%M%S")

        lines.extend(
            [
                "BEGIN:VEVENT",
                f"UID:{e.uuid}",
                f"SUMMARY:{e.title}",
                f"DTSTART:{dtstart}",
                f"DTEND:{dtend}",
                f"DESCRIPTION:{e.description}",
                "END:VEVENT",
            ]
        )
    lines.append("END:VCALENDAR")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def create_display(root):
    print("Create")
