import datetime
import os
from time import sleep
from typing import Optional
import webbrowser

pwd = os.path.abspath(os.path.dirname(__file__))
PATH_LAST_EXECUTION_TIME = os.path.join(pwd, 'last_opened.txt')
PATH_LINKS_TO_OPEN = os.path.join(pwd, 'links.txt')


def open_web_links_in_file(path_link_file: str, heading_links_to_open: Optional[str] = None):
    def open_if_is_link(row: str):
        if row.startswith('http'):
            webbrowser.open_new_tab(row)
            sleep(0.05)

    current_heading = ''
    with open(path_link_file) as f:
        for row in f:
            row = row.strip()

            if row.startswith('#'):
                current_heading = row

            if heading_links_to_open is None or current_heading == heading_links_to_open:
                open_if_is_link(row)


def update_last_execution_date(new_date: str):
    with open(PATH_LAST_EXECUTION_TIME, 'w') as f:
        f.write(new_date)


def is_not_opened_today(today):
    def get_last_execution_date() -> str:
        if os.path.exists(PATH_LAST_EXECUTION_TIME):
            with open(PATH_LAST_EXECUTION_TIME) as f:
                last_execution_date = f.readline()
        else:
            last_execution_date = None

        return last_execution_date

    last_execution_date = get_last_execution_date()
    return today != last_execution_date


def main():
    open_web_links_in_file(PATH_LINKS_TO_OPEN, heading_links_to_open='# Always')

    today = datetime.datetime.now().strftime('%Y-%m-%d')
    if is_not_opened_today(today):
        open_web_links_in_file(PATH_LINKS_TO_OPEN, heading_links_to_open='# Daily')

    update_last_execution_date(today)


if __name__ == '__main__':
    main()
