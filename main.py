import tkinter as tk
from tkinter import ttk


def main():
    root = tk.Tk()
    root.title("Task Manager")
    root.geometry("600x600")

    frame = ttk.Frame(root, padding=(3, 3, 12, 12))
    frame.grid(column=0, row=0, sticky=("nwes"))

    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    frame.columnconfigure(2, weight=1)

    root.mainloop()


if __name__ == "__main__":
    main()
