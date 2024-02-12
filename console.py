#!/usr/bin/python3
""" The console program"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    CLI cass
    """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """ Exits the program."""
        return True

    def help_quit(self):
        """ Assistance when quitting"""
        print("Quit command to exit the program")

    def do_EOF(self, arg):
        """ Exits using EOF"""
        return True
    
    def help_EOF(self):
        """ Assistance when using EOF"""
        print("exit program using EOF")

    def empty(self):
        """ Assumes an empty line"""
        pass

if __name__ == '__main__':
        HBNBCommand().cmdloop()