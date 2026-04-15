from datetime import date, time, datetime

events = []


class Event:
    def __init__(self, title, due_date, due_time, description, complete=False):
        self.title = title
        self.due_date = due_date
        self.due_time = due_time
        self.description = description
        self.complete = complete

    def status(self):
        return "Completed" if self.complete else "Pending"


# Testing events
events.append(Event("Meeting", date(2026, 4, 15), datetime.now().time(), "A meeting"))
events.append(
    Event(
        "Gym",
        date(2026, 4, 2),
        datetime.now().time(),
        "Gym visit ksajdhfl khasdkfhashdfl hasdlfasdhfklas jhkfhasdkfh",
    )
)
events.append(Event("Meeting", date(2026, 4, 2), datetime.now().time(), "A meeting"))
events.append(Event("Store", date(2026, 4, 2), datetime.now().time(), "Go to store"))


def load_events():
    pass


def save_events():
    pass
