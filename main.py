import os
from datetime import datetime
from dateoperations import contains_dashes, days_since_date
def show_help():
    print('''
    Usage: hypeban -[option]

    Accepted date formats: [YYYY-MM-DD], [MM-DD-YYYY]

        --h, -help                  Display this menu
        --a, -about                 See more program information
        --c, -clear                 Clear console
        --u, -until                 Calculate days until given date
        --s, -since                 Calculate days since given date
    ''')


show_help()

while True:
    command = input(" > ")

    if (command == "help"):
        show_help()

    elif (command == "about"):
        print('''
        NAME
            hypeban, hp

        SYNOPSIS
            Perform calender date operations using UNIX-formatted date strings.

        DESCRIPTION
        A terminal-based program that calculates days left until a given date that parses DateStrings
         in multiple UNIX-compliant formats created by Bupper
         
        USAGE
            Enter a date as follows.

            Example 1:
                > since 1969-07-20
                Date input: 1969-07-20
                Output: 19078

            Example 2:
                > since 01-31-2000
                Date input: 01-31-200
                Output: 7926


         ''')
    
    elif (command == "clear"):
        os.system("clear")

    elif command.startswith("since "):
        date_string = command.split(" ")[-1]
        includes_dashes = contains_dashes(date_string)
        if includes_dashes: date_string_elements = date_string.split("-")



        if includes_dashes and len(date_string_elements[0]) == 4: 
            result = days_since_date(date_string, "%Y-%m-%d")
            print("Days since:", result)

        elif includes_dashes and len(date_string_elements[-1]) == 4:
            result = days_since_date(date_string, "%m-%d-%Y")
            print("Days since:", result)

    elif command.startswith("until "):
        date_string = command.split(" ")[-1]
        includes_dashes = contains_dashes(date_string)
        if includes_dashes: date_string_elements = date_string.split("-")



        if includes_dashes and len(date_string_elements[0]) == 4: 
            then = datetime.strptime(date_string, "%Y-%m-%d")
            print("Date input:", then.strftime("%d %B %Y"))
            now = datetime.now()
            days_until = (then - now).days
            print("Days until: ", days_until)

        elif includes_dashes and len(date_string_elements[-1]) == 4:
            then = datetime.strptime(date_string, "%m-%d-%Y")
            print("Date input:", then.strftime("%d %B %Y"))
            now = datetime.now()
            days_until = (then - now).days
            print("Days until: ", days_until)

    elif command == "exit":
        break

    else:
        print("Command not found")