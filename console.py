#!/usr/bin/python3

"""
console.py to run console
"""

import cmd

class HBNBCommand(cmd.Cmd):
    """
    console class
    """
    prompt = "(hbnb) "

    def do_quit(self, line):
        """
        command to quit the interpreter
        """

        return True

    def do_EOF(self, line):
        """
        Command for the end of file. It quits
        """

        return True

    def emptyline(self):
        """
        Empty line command
        """
        return True

    def onecmd(self, line):
        """
        interpreter for any command we enter
        """
        if line == "quit":
            return self.do_quit(line)
        elif line == "EOF":
            return self.do_EOF(line)
        else:
            cmd.Cmd.onecmd(self, line)

if __name__ == "__main__":
    HBNBCommand().cmdloop()
