class Event:
    def __init__(
        self,
        uuid,
        title,
        start_date,
        start_time,
        due_date,
        due_time,
        description,
        complete=False,
    ):
        self.uuid = uuid
        self.title = title
        self.start_date = start_date
        self.start_time = start_time
        self.due_date = due_date
        self.due_time = due_time
        self.description = description
        self.complete = complete

    def status(self):
        return "Completed" if self.complete else "Pending"
