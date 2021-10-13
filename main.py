import os

def show_help():
    print('''
    Usage: hypeban -[option]

    Accepted date formats: [YYYY-MM-DD], [DD-MM-YYYY], [MM-DD]

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
            Perform calander date operations using UNIX-formatted date strings.

        DESCRIPTION
        A terminal-based program that calculates days left until a given date that parses DateStrings
         in multiple UNIX-compliant formats created by Bupper
         
        USAGE
            Enter a date as it follows.

            Example 1:
                > since 1969-07-20

                Output: 19,077 days since 1969-07-20

            Example 2:
                > since 01-01-2000

                Output: 7,955 days since 01-01-2000


         ''')
    
    elif (command == "clear"):
        os.system("clear")

    else:
        print("Command not found")