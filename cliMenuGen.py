"""A CLI Menu Generator.

Generator command line menus and only except given inputs.
And more. See README.md
"""

AUTHOR = "mtech0 https://github.com/mtech0"
LICENSE = "GNU-GPLv3 https://www.gnu.org/licenses/gpl.txt"
VERSION = "1.1.3"
STATUS = "Dev"
SKU = "Main"
URL = "https://github.com/mtech0/cli-menu-generator/"

_errors = {}
try:
    from os import system
    _errors["os-module"] = True
except:
    _errors["os-module"] = False
from platform import system as os_name

# Menu Generator
def menu(acceptables, lines=None, unknown=None, prompt=None, preclear=True, postclear=False):
    """A CLI menu generator.
    
    This function generates a menu with given lines and then only
    accepts inputs that are in acceptables, when it get ones of these it
    returns it.
     
    acceptables: A list of commands to accept must be provided.
        - The whole system is non case-sensitive.
        - include "*" to accept anything.
    lines: The list of lines to print before asking for an input.
        - Defaults to nothing.
    prompt: The prompt when asking for an input.
        - Defaults to nothing.
    unknown: The text to print when an invalid command is given.
        - Defaults to "Error: Unknown [{input}]"
    preclear: Clear the screen before printing the menu.
        - Defaults to true.
    postclear: Clear the screen after a succesful command is given.
        - Defaults to false.
    """
  
    # Defaults
    if not lines:
        lines = []
    if not prompt:
        prompt = ""
    if not unknown:
        unknown = "Error: Unknown [{0}]"
    acceptables = [str(item).lower() for item in acceptables]
    # Menu generator
    if preclear:
        clear()
    for line in lines:
        print(line)
    while True:
        cmd = input(prompt).lower()
        if cmd in acceptables or "*" in acceptables:
            break
        else:
            print(unknown.format(cmd))
    if postclear:
        clear()
    return cmd
    
# Tools
def clear(lines=100):
    """Clears the screen.
     
    Lines is used if system is not available.
    lines: The amound of lines to clear by.
        - Defaults to 100
    """
    
    global _errors
    os = os_name()
    if not _errors["os-module"]:
        print("\n"*lines)
        print("Could not import os module - Using fall-back method") 
    elif os == "Windows":
        system("cls")
    elif os == "Linux":
        system("clear")
    return None
    
def ranAsMain():
    lines = ["CLI Menu Generator v{0}".format(VERSION),
             "See {0} for more info.".format(URL),
             "Writen by {0}".format(AUTHOR),
             "Licensed under {0}".format(LICENCE),
             "SKU: {0} [Status: {1}]".format(SKU, STATUS)]
    for line in lines:
        print(line)
    return None
        
if __name__ == "__main__":
    ranAsMain()
