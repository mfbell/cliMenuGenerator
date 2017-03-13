# Python CLI menu generator.
```
    From cli-menu.py:
    This function [menu] generates a menu with given lines and then only
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
```

## sytax      
```
menu(acceptables [, lines, unknown, prompt, preclear, postclear])
```

## example use
```
import cli-menu

lines = ["HI", "Welcome to this example", "Type hi to continue"]
acceptables = ["hi"]
unknown = "You did not type hi :("
prompt = "/"
cmd = cli-menu.menu(acceptables, lines, unknown, prompt)
```

## other tools
There is clear()
This clears the screen with the os' clear screen command or if os module is not available it uses black lines.
The default amount of lines is 100. To change it, it is clear()'s first and only argument.
```
clear([lines])
```
