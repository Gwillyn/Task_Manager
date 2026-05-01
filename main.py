import ui
import database


def main():
    database.create_table()
    ui.main_display()


if __name__ == "__main__":
    main()
