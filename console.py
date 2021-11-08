#!/usr/bin/python3
"""This is a program named console.py that contains the entry point
of the command interpreter:."""
import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
    """Contains the entry point of the command interpreter."""
    prompt = "(hbnb) "
    class_list = ("BaseModel", "User", "Amenity", "City",
                  "Place", "Review", "State")

    def emptyline(self):
        """When there is an empty line + ENTER shouldn’t execute anything."""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """Exits the program."""
        return True

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id.
        """
        if not arg:
            print("** class name missing **")
            return
        if arg not in HBNBCommand.class_list:
            print("** class doesn't exist **")
            return
        obj = eval(arg + "()")
        obj.save()
        print(obj.id)

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id."""
        arg_list = arg.split(" ") if type(arg) == str else arg
        if not arg:
            print("** class name missing **")
            return
        if arg_list[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
            return
        if len(arg_list) < 2:
            print("** instance id missing **")
            return
        key = arg_list[0] + "." + arg_list[1]
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file)."""
        arg_list = arg.split(" ") if type(arg) == str else arg
        if not arg:
            print("** class name missing **")
            return
        if arg_list[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
            return
        if len(arg_list) < 2:
            print("** instance id missing **")
            return
        key = arg_list[0] + "." + arg_list[1]
        if key in storage.all():
            del storage.all()[key]
            storage.save()
            return
        print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances
        based or not on the class name."""
        arg_list = arg.split(" ") if type(arg) == str else arg
        if arg:
            if arg_list[0] not in HBNBCommand.class_list:
                print("** class doesn't exist **")
                return
            obj_list = []
            for key, val in storage.all().items():
                if key.split(".")[0] == arg_list[0]:
                    obj_list.append(str(val))
            print(obj_list)
            return
        obj_list = [str(val) for val in storage.all().values()]
        print(obj_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id
        by adding or updating attribute
        (save the change into the JSON file)."""
        if type(arg) == str:
            arg_list = shlex.shlex(arg)
            arg_list.wordchars += "-"
            arg_list = list(arg_list)
            try:
                index_start = arg_list.index("[")
                index_end = arg_list.index("]")
                list_str = "".join(arg_list[index_start:index_end + 1])
                list_str = eval(list_str)
                list_start = arg_list[:index_start]
                list_end = arg_list[index_end + 1:]
                arg_list = list_start
                arg_list.append(list_str)
                arg_list.extend(list_end)
            except ValueError:
                pass
        else:
            arg_list = arg
        if not arg:
            print("** class name missing **")
            return
        if arg_list[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
            return
        if len(arg_list) < 2:
            print("** instance id missing **")
            return
        key = arg_list[0] + "." + arg_list[1]
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(arg_list) == 3 and type(arg_list[2]) == dict:
            obj = storage.all()[key]
            for key, val in arg_list[2].items():
                setattr(obj, key, val)
                obj.save()
            return
        if len(arg_list) < 3:
            print("** attribute name missing **")
            return
        if len(arg_list) < 4:
            print("** value missing **")
            return
        obj = storage.all()[key]
        if type(arg_list[3]) != list:
            arg_list[3].replace('"', "").replace("'", "")
        setattr(obj, arg_list[2].replace('"', "").replace("'", ""),
                arg_list[3])
        obj.save()

    def do_count(self, arg):
        """Retrieve all instances of a class"""
        arg_list = arg.split(" ") if type(arg) == str else arg
        if not arg:
            print("** class name missing **")
            return
        if arg_list[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
            return
        objs = [key for key in map(lambda x: x.split(".")[0],
                                   storage.all().keys())]
        print(objs.count(arg_list[0]))

if __name__ == '__main__':
    HBNBCommand().cmdloop()
