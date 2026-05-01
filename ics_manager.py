from tkinter import filedialog
from datetime import datetime
import database


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

    tasks = database.get_tasks()

    for e in tasks:
        task_id, title, description, start_datetime, due_datetime, complete = e

        start_dt = datetime.strptime(start_datetime, "%Y-%m-%d %H:%M:%S")
        end_dt = datetime.strptime(due_datetime, "%Y-%m-%d %H:%M:%S")

        dtstart = start_dt.strftime("%Y%m%dT%H%M%S")
        dtend = end_dt.strftime("%Y%m%dT%H%M%S")

        lines.extend(
            [
                "BEGIN:VEVENT",
                f"UID:{task_id}",
                f"SUMMARY:{title}",
                f"DTSTART:{dtstart}",
                f"DTEND:{dtend}",
                f"DESCRIPTION:{description}",
                "END:VEVENT",
            ]
        )
    lines.append("END:VCALENDAR")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
