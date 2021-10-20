import os
from datetime import datetime
from dateoperations import contains_dashes, days_since_date, days_until_date
from config import show_help

show_help()

while True:
    command = input(" > ")

    if (command == "help"):
        show_help()

    elif (command == "about"):
        print ("Refer to README: https://github.com/Bupper420/hypeban")

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
            result = days_until_date(date_string, "%Y-%m-%d")
            print("Days until:", result)

        elif includes_dashes and len(date_string_elements[-1]) == 4:
            result = days_until_date(date_string, "%m-%d-%Y")
            print("Days until:", result)

    elif command == "exit":
        break

    else:
        print("Command not found")