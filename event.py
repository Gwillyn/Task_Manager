from datetime import date, datetime
from uuid import uuid4

events = []


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


# Testing events
events.append(
    Event(
        str(uuid4()),
        "Meeting",
        date(2026, 4, 15),
        datetime.now().time(),
        date(2026, 4, 15),
        datetime.now().time(),
        "A meeting",
    )
)
events.append(
    Event(
        str(uuid4()),
        "Gym",
        date(2026, 4, 15),
        datetime.now().time(),
        date(2026, 4, 2),
        datetime.now().time(),
        "Gym visit ksajdhfl khasdkfhashdfl hasdlfasdhfklas jhkfhasdkfh",
    )
)
events.append(
    Event(
        str(uuid4()),
        "Meeting",
        date(2026, 4, 15),
        datetime.now().time(),
        date(2026, 4, 2),
        datetime.now().time(),
        "A meeting",
    )
)
events.append(
    Event(
        str(uuid4()),
        "Store",
        date(2026, 4, 15),
        datetime.now().time(),
        date(2026, 4, 2),
        datetime.now().time(),
        "Go to store",
    )
)


def load_events():
    pass


def save_events():
    pass
