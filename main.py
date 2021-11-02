import os
import argparse
from datetime import datetime
from dateoperations import contains_dashes, days_since_date, days_until_date
from config import show_help



# while True:
#     command = input(" > ")

#     if (command == "help"):
#         show_help()

#     elif (command == "about"):
#         print ("Refer to README: https://github.com/Bupper420/hypeban")

#     elif (command == "clear"):
#         os.system("clear")

#     elif command.startswith("since "):
#         date_string = command.split(" ")[-1]
#         includes_dashes = contains_dashes(date_string)
#         if includes_dashes: date_string_elements = date_string.split("-")



#         if includes_dashes and len(date_string_elements[0]) == 4: 
#             result = days_since_date(date_string, "%Y-%m-%d")
#             print("Days since:", result)

#         elif includes_dashes and len(date_string_elements[-1]) == 4:
#             result = days_since_date(date_string, "%m-%d-%Y")
#             print("Days since:", result)

#     elif command.startswith("until "):
#         date_string = command.split(" ")[-1]
#         includes_dashes = contains_dashes(date_string)
#         if includes_dashes: date_string_elements = date_string.split("-")



#         if includes_dashes and len(date_string_elements[0]) == 4: 
#             result = days_until_date(date_string, "%Y-%m-%d")
#             print("Days until:", result)

#         elif includes_dashes and len(date_string_elements[-1]) == 4:
#             result = days_until_date(date_string, "%m-%d-%Y")
#             print("Days until:", result)

#     elif command == "exit":
#         break

#     else:
#         print("Command not found")

###--------------------------------------------NEW--------------------------------------------------


parser = argparse.ArgumentParser()

parser.add_argument("--about", help="display information about program", action="store_true")
parser.add_argument("-s", "--since", help="enter a date as an argument to find days since given date")
parser.add_argument("-u", "--until", help="enter a date as an argument to find days until given date")

args = parser.parse_args()
if args.about:
    print("A terminal-based program that calculates days left until a given date that parses DateStrings in multiple UNIX-compliant formats created by Bupper")

if args.since:
    date_string = args.since
    includes_dashes = contains_dashes(date_string)
    if includes_dashes: date_string_elements = date_string.split("-")

    if includes_dashes and len(date_string_elements[0]) == 4: 
        result = days_since_date(date_string, "%Y-%m-%d")
        print("Days since:", result)

    elif includes_dashes and len(date_string_elements[-1]) == 4:
        result = days_since_date(date_string, "%m-%d-%Y")
        print("Days since:", result)
        print("User entered:", args.since)

if args.until:
    date_string = args.until
    print("User entered:", args.until)