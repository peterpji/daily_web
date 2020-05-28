
# Purpose
This small tool opens websites that the user opens often. Links are under two headings: those to be opened every execution and those opened daily.

# Files
## links.txt
This file contains links under two headings:
- Always
- Daily

Headings are marked with a "#" character at the start of the file. Example:

```
# Always
https://calendar.google.com/

# Daily
http://explosm.net/
```

## last_opened.txt
This file contains the date the program was last run. Example:
```
2020-05-28
```

# Dependencies
The program uses only Python in-built libraries. However, webbrowser library by default sends the open requests to the default system browser.
