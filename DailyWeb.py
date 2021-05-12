import datetime
import os
from time import sleep
import webbrowser

pwd = os.path.abspath(os.path.dirname(__file__))
PATH_LAST_EXECUTION_TIME = os.path.join(pwd, 'last_opened.txt')
PATH_LINKS_TO_OPEN = os.path.join(pwd, 'links.txt')


def open_web_links_in_file(path_link_file, heading_links_to_open=None):
    def open_link_with_validation(row):
        if row[0:4] == 'http':
            webbrowser.open_new_tab(row)
            sleep(0.03)

    current_heading = ''
    with open(path_link_file) as f:
        for row in f:
            row = row.strip()

            if row and row[0] == '#':
                current_heading = row

            if heading_links_to_open is None:
                open_link_with_validation(row)

            elif current_heading == heading_links_to_open:
                open_link_with_validation(row)


def get_last_execution_date():
    if os.path.exists(PATH_LAST_EXECUTION_TIME):
        with open(PATH_LAST_EXECUTION_TIME) as f:
            last_execution_date = f.readline()
    else:
        last_execution_date = None

    return last_execution_date


def update_last_execution_date(new_date):
    with open(PATH_LAST_EXECUTION_TIME, 'w') as f:
        f.write(new_date)


def main():
    open_web_links_in_file(PATH_LINKS_TO_OPEN, heading_links_to_open='# Always')

    last_execution_date = get_last_execution_date()
    today = datetime.datetime.now().strftime('%Y-%m-%d')

    if today != last_execution_date:
        open_web_links_in_file(PATH_LINKS_TO_OPEN, heading_links_to_open='# Daily')

    update_last_execution_date(today)


if __name__ == '__main__':
    main()
