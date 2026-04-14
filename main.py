import tkinter as tk
from tkinter import ttk


def main():
    text_font = "JetBrainsMono Nerd Font"

    root = tk.Tk()
    root.title("Task Manager")
    root.geometry("600x600")

    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # Main Frame
    mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))
    mainframe.grid(column=0, row=0, sticky=("nwes"))

    mainframe.columnconfigure(0, weight=1)

    # Header Frame
    headerframe = ttk.Frame(mainframe)
    headerframe.grid(column=0, row=0, sticky="ew")
    headerframe.columnconfigure(0, weight=1)

    ttk.Label(
        headerframe, text="Task Manager", font=(text_font, 20, "bold"), anchor="center"
    ).grid(column=0, row=0, pady=10)

    # Task Area

    taskframe = ttk.Frame(mainframe)
    taskframe.grid(column=0, row=1, sticky="ew")
    taskframe.columnconfigure(0, weight=1)
    taskframe.rowconfigure(0, weight=1)

    buttonframe = ttk.Frame(taskframe)
    buttonframe.grid(column=0, row=0, sticky="ew")

    settings_button = ttk.Button(buttonframe, text="Settings")
    settings_button.grid(column=0, row=0, padx=15)

    make_task_button = ttk.Button(buttonframe, text="Make Task")
    make_task_button.grid(column=1, row=0, padx=15)

    # List Area
    listframe = ttk.Frame(mainframe)
    listframe.grid(column=0, row=2, sticky="ew")
    listframe.columnconfigure(0, weight=1)

    ttk.Label(listframe, text="Tasks: ", font=(text_font, 16, "bold")).grid(
        column=0, row=0, pady=10
    )
    root.mainloop()


if __name__ == "__main__":
    main()
