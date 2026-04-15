import ui
from datetime import date
from datetime import datetime
from event import Event

# Testing event
e1 = Event("Meeting", date(2026, 4, 15), datetime.now(), "A meeting")
e2 = Event("Gym", date(2026, 4, 2), datetime.now(), "Gym visit")
e3 = Event("Meeting", date(2026, 4, 2), datetime.now(), "A meeting")
e4 = Event("Store", date(2026, 4, 2), datetime.now(), "Go to store")

events = []
events.append(e1)
events.append(e2)
events.append(e3)
events.append(e4)


def main():
    ui.display()


if __name__ == "__main__":
    main()
