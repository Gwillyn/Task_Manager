from tkinter import filedialog
import event
from datetime import datetime


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
