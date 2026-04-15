class Event:
    def __init__(self, title, due_date, due_time, description, complete=False):
        self.title = title
        self.due_date = due_date
        self.due_time = due_time
        self.description = description
        self.complete = complete

    def status(self):
        return "Completed" if self.complete else "Pending"
