#!/usr/bin/python3

import sys
import cmd
from base_model import BaseModel
from file_storage import FileStorage

class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb)"
    our_classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
        }

    def emptyline(self):
       """Do nothing upon receiving an empty line."""
       pass

    def do_quit(self, arg):
        """quit command to exit the program"""
        return True
    
    def do_EOF(self, arg):
        """EOF to exit the program."""
        print("")
        return True

    def do_create(self, arg):
        """Usage: create <class>
        Create a new class instance and print its id.
        """

        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        
        # class_name = sys.argv[1]
        elif args[0] not in HBNBCommand.our_classes:
                print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, *args):
        """Usage: show <class> <id> or <class>.show(<id>)
        Display the string representation of a class instance of a given id.
        """
        arg = args.split()
        info = storage.all()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
        elif arg[1] == None:
            print("** instance id missing **")
        elif pass

    def do_destroy(self, arg):
        """Usage: destroy <class> <id> or <class>.destroy(<id>)
        Delete a class instance of a given id.
        """
        args = arg.split()
        dicts = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.__our_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in dicts.keys():
            print("** no instance found **")
        else:
            del dicts["{}.{}".format(args[0], args[1])]
            storage.save()

    def do_all(self, arg):
        """Usage: all or all <class> or <class>.all()
        Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects.
        """
        
        args = arg.split()
        if len(args) == 0:
            print("** class doesn't exist **")
        else:
            obj1 = []
            for obj in storage.all().values():
                if len(args) > 0 and args[0] == obj.__class__.__name__:
                    obj1.append(obj.__str__())
                elif len(args) == 0:
                    obj1.append(obj.__str__())
            print(obj1)

    def do_update(self, arg):
        """Usage: update <class> <id> <attribute_name> <attribute_value> or
       <class>.update(<id>, <attribute_name>, <attribute_value>) or
       <class>.update(<id>, <dictionary>)
        Update a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary.
        """
        
        args = arg.split()
        obj_dict = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        if arg[0] not in HBNBCommand.our_classes:
            print("** class doesn't exist **")
            return False
        if len(args) == 1:
            print("** instance id missing **")
        if "{}.{}".format(args[0], args[1]) not in obj_dict.keys():
            print("** no instance found **")
            return False
        if len(args) == 2:
            print("** attribute name missing **")
            return False
        if len(args) == 3:
            try:
                 type(eval(args[2])) != dict
            except NameError:
                print("** value missing **")
                return False
        
        if len(args) == 4:
            obj = obj_dict["{}.{}".format(args[0], args[1])]
            if args[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[args[2]])
                obj.__dict__[args[2]] = valtype(args[3])
            else:
                obj.__dict__[args[2]] = args[3]
        elif type(eval(args[2])) == dict:
            obj = obj_dict["{}.{}".format(args[0], args[1])]
            for k, v in eval(args[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()

    def do_count(self, arg):
        """count <class> or <class>.count()
        Retrieve the number of instances of a given class.
        """
        
        args = arg.split()
        count = 0
        for obj in storage.all().values():
            if args[0] == obj.__class__.__name__:
                count += 1
        print(count)
          


if __name__ == "__main__":
    HBNBCommand().cmdloop()
