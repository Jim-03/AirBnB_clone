#!/usr/bin/python3
""" The console program"""
import cmd
from models.base_model import BaseModel
from models import storage


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

    def do_create(self, arg):
        """ Creates an instance of BaseModel."""
        if not arg:
            print("** class name missing **")
            return
        argumentList = arg.split()
        className = argumentList[0]
        if className not in ["BaseModel"]:
            print("** class doesn't exist **")
            return
        New = BaseModel()
        New.save()
        print(New.id)

    def do_show(self, arg):
        """Prints the string representation of an instance
          based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return
        argumentList = arg.split()
        className = argumentList[0]
        if className not in ["BaseModel"]:
            print("** class doesn't exist **")
            return
        if len(argumentList) <= 1:
            print("** instance id missing **")
            return

        objId = argumentList[1]
        objs = storage.all()
        objKey = "{}.{}".format(className, objId)
        if objKey not in objs:
            print("** no instance found **")
            return
        print(objs[objKey])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        if not arg:
            print("** class name missing **")
            return
        argumentList = arg.split()
        className = argumentList[0]
        if className not in ["BaseModel"]:
            print("** class doesn't exist **")
            return
        if len(argumentList) < 2:
            print("** instance id missing **")
            return
        objId = argumentList[1]
        objs = storage.all()
        objKey = "{}.{}".format(className, objId)
        if objKey not in objs:
            print("** no instance found **")
            return
        del objs[objKey]
        storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances
        based or not on the class name."""
        if not arg:
            objs = storage.all()
        else:
            argumentList = arg.split()
            className = argumentList[0]
            if className not in ["BaseModel"]:
                print("** class doesn't exist **")
                return
            objs = {
                key: obj
                for key, obj in storage.all().items()
                if className in key
                }
        print([str(obj) for obj in objs.values()])

    def do_update(self, arg):
        """Updates an instance based on the class name and id
        by adding or updating attribute."""
        if not arg:
            print("** class name missing **")
            return
        argumentList = arg.split()
        className = argumentList[0]
        if className not in ["BaseModel"]:
            print("** class doesn't exist **")
            return
        if len(argumentList) < 2:
            print("** instance id missing **")
            return
        objId = argumentList[1]
        objs = storage.all()
        objKey = "{}.{}".format(className, objId)
        if objKey not in objs:
            print("** no instance found **")
            return
        if len(argumentList) <= 2:
            print("** attribute name missing **")
            return
        attr = argumentList[2]
        if len(argumentList) < 4:
            print("** value missing **")
            return
        attr_str = argumentList[3]
        attr_val = attr_str
        try:
            attr_val = eval(attr_str)
        except (NameError, SyntaxError):
            pass
        setattr(objs[objKey], attr, attr_val)
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
