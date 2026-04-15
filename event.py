from datetime import date


class Event:
    def __init__(self, title, due_date, description, complete=False):
        self.title = title
        self.due_date = due_date
        self.description = description
        self.complete = complete

    def status(self):
        return "Completed" if self.complete else "Pending"
