#!/usr/bin/python3
"""Entry point of the command interpreter"""

import cmd
import json
from models.base_model import BaseModel
from models import storage


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
            if line == "BaseModel":
                base = BaseModel()
                base.save()
                print(base.id)
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
            if cls_name_id[0] == "BaseModel":
                name_id_key = ".".join(cls_name_id)
                try:
                    store = storage.all()
                    obj = store[name_id_key]
                    new_model = BaseModel(**obj)
                    print(new_model)
                    return
                except:
                    print("** no instance found **")
                    return
            else:
                print("** class doesn't exist **")
                return

        if line != "BaseModel":
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
            if cls_name_id[0] == "BaseModel":
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

        if line != "BaseModel":
            print("** class does't exit **")
            return

        if len(cls_name_id) == 1:
            print("** instance id missing **")
            return

    def do_all(self, line):
        """Prints all string representation of all instances based of not
        on the class name"""
        if line == "BaseModel" or not line:
            obj_list = [value for _, value in storage.all().items()]
            print(obj_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding
        or updating attribute"""
        non_updateables = ["id", "created_id", "updated_at"]

        if not line:
            print("** class name is missing **")
            return

        line_param = line.split(" ")
        if len(line_param) == 4:
            if line_param[0] == "BaseModel":
                name_id_key = ".".join(line_param[:2])
                try:
                    store = storage.all()
                    obj = store[name_id_key]
                    new_model = BaseModel(**obj)
                    setattr(new_model, line_param[2], line_param[3].strip("\""))
                    new_model.save()
                    return
                except:
                    print("** no instance found **")
                    return

        elif len(line_param) == 1 and line_param[0] == "BaseModel":
            print("** instance id missing **")
            return

        elif len(line_param) == 2:
            print("** attribute name missing **")
            return

        else:
            print("** value missing **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
