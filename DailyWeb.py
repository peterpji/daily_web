import webbrowser
import time
import datetime


def OpenLinks(path, lineMin=0, lineMax=-1, openHeading='#Null', wait=0):
    # Wait for the browser to update
    if wait == 1:
        time.sleep(0.1)

    with open(path, 'r') as file:
        line = 0
        heading = ''
        for row in file:
            row = row.strip()
            row = row + ' '  # Empty row causes an error
            line += 1

            # Open link based on row number
            if line >= lineMin and line <= lineMax:
                if row[0:4] == 'http':
                    webbrowser.open_new_tab(row)

            # Open link based on the heading. Headings are marked by a leading '#' character.
            if row[0] == '#':
                heading = row
                heading = heading.strip()
            if heading == openHeading and row[0:4] == 'http':
                webbrowser.open_new_tab(row)

            time.sleep(0.075)


def Main():
    # State file has one variable: last execution time
    pathState = 'DailyWeb_state.txt'
    with open(pathState, 'r') as file:
        lastExec = file.readline()

    now = datetime.datetime.now()
    now = now.strftime('%Y-%m-%d')

    # Open links that are opened every time the program is executed
    pathLinks = 'DailyWeb_links.txt'
    OpenLinks(pathLinks, lineMax=25)

    # Open links that are opened only once per day
    # if now != lastExec:
    #     pathTitles = 'C:/Users/peter/Dropbox/Muistiinpanoja/Titles.txt'
    #     OpenLinks(pathTitles, openHeading='#Comics', wait=1)

    # Update state
    with open(pathState, 'w') as file:
        file.write(now)

    exit()


Main()
