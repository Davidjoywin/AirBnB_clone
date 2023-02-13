#!/usr/bin/python3
"""Entry point of the command interpreter"""

import cmd
import sys
import json

from models import storage
from models.user import User
from models.base_model import BaseModel


model_apps = [
        "BaseModel",
        "User"
        ]

def get_class(name):
    return getattr(sys.modules[__name__], name)

class HBNBCommand(cmd.Cmd):
    """Command prompt

    Attributes:
        prompts - Prompt for each execution
        Intro - Intro to the prompts
    """
    intro = "HBNBCommand prompt. Type help or ? to list command\n"
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Exit the program"""
        return True

    def do_EOF(self, line):
        """Exit the program"""
        return True

    def default(self, line):
        """Commands which are not defined"""
        pass

    def do_help(self, *args):
        """list all the command available"""
        cmd.Cmd.do_help(self, *args)
        print("Use Ctrl+l to clear screen, Ctrl+a...)")

    def do_create(self, line=None):
        """create a new instance of BaseModel, save if to JSON file"""
        if line:
            if line in model_apps:
                cls_from_name = get_class(line)
                cls_model = cls_from_name()
                cls_model.save()
                print(cls_model.id)
            else:
                print("** class doesn't exit **")

        else:
            print("** class name is missing **")

    def do_show(self, line=None):
        """
            prints the string representation of an instance based on the class
            name and id
        """
        if not line:
            print("** class name missing **")
            return

        cls_name_id = line.split(" ")
        if len(cls_name_id) == 2:
            if cls_name_id[0] in model_apps:
                name_id_key = ".".join(cls_name_id)
                print(name_id_key)
                try:
                    store = storage.all()
                    obj = store[name_id_key]
                    cls_from_name = get_class(cls_name_id[0])
                    new_model = cls_from_name(**obj)
                    print(new_model)
                    return
                except Exception as e:
                    print("** no instance found **")
                    return
            else:
                print("** class doesn't exist **")
                return

        if not line in model_apps:
            print("** class doesn't exist **")
            return

        if len(cls_name_id) == 1:
            print("** instance id missing **")
            return

    def do_destroy(self, line=None):
        """Deletes an instance based on the class name and id"""
        if not line:
            print("** class name missing **")
            return

        cls_name_id = line.split(" ")
        if len(cls_name_id) == 2:
            if cls_name_id[0] in model_apps:
                name_id_key = ".".join(cls_name_id)
                try:
                    store = storage.all()
                    del store[name_id_key]
                    storage.__objects = store
                    storage.save()
                    return
                except:
                    print("** no instance found **")
                    return
            else:
                print("** class don't exist")
                return

        if not line in model_apps:
            print("** class does't exit **")
            return

        if len(cls_name_id) == 1:
            print("** instance id missing **")
            return

    def do_all(self, line):
        """Prints all string representation of all instances based of not
        on the class name"""
        if not line:
            obj_list = [value for _, value in storage.all().items()]
            print(obj_list)
        elif line in model_apps:
            obj_list = [
                    value for key, value in storage.all().items()
                    if key.startswith(line)
            ]
            print(obj_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding
        or updating attribute"""

        if not line:
            print("** class name is missing **")
            return

        line_param = line.split(" ")
        if len(line_param) == 4:
            if line_param[0] in model_apps:
                name_id_key = ".".join(line_param[:2])
                try:
                    store = storage.all()
                    obj = store[name_id_key]
                    cls_from_name = get_class(line_param[0])
                    new_model = cls_from_name(**obj)
                    setattr(new_model, line_param[2], line_param[3].strip("\""))
                    new_model.save()
                    return
                except:
                    print("** no instance found **")
                    return

        elif len(line_param) == 1 and line_param[0] in model_apps:
            print("** instance id missing **")
            return

        elif len(line_param) == 2:
            print("** attribute name missing **")
            return

        else:
            print("** value missing **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
