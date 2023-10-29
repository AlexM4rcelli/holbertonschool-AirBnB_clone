#!/usr/bin/python3
"""entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.place import Place



class HBNBCommand(cmd.Cmd):
    """interpreter"""
    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "Place",
        "City",
        "State",
        "Amenity",
        "Review"
    }


    def do_quit(self, args):
        """Exit the program"""
        return True

    def do_EOF(self, args):
        """Exit the program"""
        return True

    def emptyline(self):
        """empty line does nothing"""
        pass

    def do_create(self, args):
        """
        create: Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id. Ex: $ create BaseModel
            If the class name is missing, print ** class name missing ** (ex: $ create)
            If the class name doesn’t exist, print ** class doesn't exist ** (ex: $ create MyModel)
        """
        if not args:
            print("** class name missing **")
            return
        else:
            args = args.replace('  ', ' ').replace('\n', ' ').split(' ')
            for arg in args:
                if arg not in HBNBCommand().__classes:
                    print(" ** class doesn't exist ** ")
                    return
                else:
                    new_instance = eval(f"{arg}()")
                    new_instance.save()
                    print(new_instance.id)

    def do_show(self, args):

        if not args:
            print("** class name missing **")
            return
        else:
            args = args.replace('  ', ' ').replace('\n', ' ').split(' ')
            if len(args) > 2:
                print('Usage: ClassName ClassNameid')
                return
            elif args[0] not in HBNBCommand.__classes:
                print(args[0])
                print("** class doesn't exist **")
                return
            elif len(args) == 1:
                print("** instance id missing **")
                return
            elif f"{args[0]}.{args[1]}" not in storage.all():
                print("** no instance found **")
                return
            else:
                print(storage.all()[f"{args[0]}.{args[1]}"])
                return

    def do_destroy(self, args):
        if not args:
            print("** class name missing **")
            return
        else:
            args = args.replace('  ', ' ').replace('\n', ' ').split(' ')
            if len(args) > 2:
                print('Usage: ClassName ClassNameid')
                return
            elif args[0] not in HBNBCommand.__classes:
                print("** class doesn't exist **")
                return
            elif len(args) == 1:
                print("** instance id missing **")
                return
            elif f"{args[0]}.{args[1]}" not in storage.all():
                print("** no instance found **")
                return
            else:
                del storage.all()[f"{args[0]}.{args[1]}"]
                storage.save()
                return

    def do_all(self, args):
        args = args.replace('  ', ' ').replace('\n', ' ').split(' ')
        if len(args) == 1 and args[0] == '':
            print([str(ins) for ins in storage.all().values()])
        else:
            for arg in args:
                if arg not in HBNBCommand.__classes:
                    print("** class doesn't exist **")
                else:
                    ins_list = []
                    for key, val in storage.all().items():
                        if key.startswith(arg):
                            ins_list.append(val)
                    print([str(ins) for ins in ins_list])

    def do_update(self, args):
        args = args.replace('  ', ' ').replace('\n', ' ').split(' ')
        if args[0] == '':
            print("** class name missing **")
            return
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        elif f"{args[0]}.{args[1]}" not in storage.all():
            print("** no instance found **")
            return
        elif len(args) == 2:
            print("** attribute name missing **")
            return
        elif len(args) == 3:
            print("** value missing **")
            return
        else:
            instance = storage.all()[f"{args[0]}.{args[1]}"]
            setattr(instance, args[2], args[3].strip('"'))
            storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
