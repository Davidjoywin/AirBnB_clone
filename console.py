#!/usr/bin/python3
"""Entry point of the command interpreter"""

import cmd
import sys
import json

from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel


model_apps = [
        "BaseModel",
        "User",
        "Place",
        "State",
        "City",
        "Amenity",
        "Review",
        ]


def get_class(name):
    """get the class from the class name"""
    return getattr(sys.modules[__name__], name)


def get_all(model):
    """retrieve all the instances of a class"""
    store = storage.all()
    cls_from_name = get_class(model)
    list_models = [cls_from_name(value) for key, value in store.items() if key.startswith(model)]
    return list_models


def get_count(model):
    """retrieve the number of instances of a class"""
    return len(get_all())


def show_with_id(id):
    """retrives an instance based on its ID"""
    store = storage.all()
    for key, value in store.items():
        if key.endswith(id):
            return value
    return None


def destroy_with_id(id):
    """destroy an instance based on his ID"""
    store = storage.all()
    res = None
    for key, value in store.items():
        if key.endswith(id):
            del store.__objects[key]
    store.save()


def update(id, class_name, attr_name, attr_value):
    """update an instance based on his ID"""
    obj = show_with_id(id)
    obj = class_name(**obj)
    obj.__dict__[attr_name] = attr_value
    obj.save()


def update_with_dic(id, class_name, dict_obj):
    """update an instance based on his ID with a dictionary"""
    obj = show_with_id(id)
    obj = class_name(**obj)
    for key, value in obj.__dict__.keys():
        dict_obj[key] = value
    obj.save()


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
        """commands not defined"""
        model_fun = line.split(".")
        model_name = model_fun[0]
        function_called = model_fun[1]
        if model_name in model_apps:
            if function_called == "all()":
                get_all(model_name)
            elif function_called == "count()":
                pass

    def emptyline(self):
        """When nothing is entered"""
        return False

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
                except Exception:
                    print("** no instance found **")
                    return
            else:
                print("** class doesn't exist **")
                return

        if line not in model_apps:
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
                except Exception:
                    print("** no instance found **")
                    return
            else:
                print("** class don't exist")
                return

        if line not in model_apps:
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
                    stripped = line_param[3].strip("\"")
                    setattr(new_model, line_param[2], stripped)
                    new_model.save()
                    return
                except Exception:
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
