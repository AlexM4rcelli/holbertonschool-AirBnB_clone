#!/usr/bin/python3
"""entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel
from models.__init__ import storage

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
                    print (" ** class doesn't exist ** ")
                    return
                else:
                    newinstance = BaseModel()
                    newinstance.save()
                    print(newinstance.id)

    def do_show(self, args):
        """
        show: Prints the string representation of an instance based on the class name and id. Ex: $ show BaseModel 1234-1234-1234.
        If the class name is missing, print ** class name missing ** (ex: $ show)
        If the class name doesn’t exist, print ** class doesn't exist ** (ex: $ show MyModel id)
        If the id is missing, print ** instance id missing ** (ex: $ show BaseModel)
        If the instance of the class name doesn’t exist for the id, print ** no instance found ** (ex: $ show BaseModel 121212)
        """
        
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
                print (" ** class doesn't exist ** ")
                return
            elif len(args) == 1:
                print(" ** instance id missing ** ")
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
                print (" ** class doesn't exist ** ")
                return
            elif len(args) == 1:
                print(" ** instance id missing ** ")
                return
            elif f"{args[0]}.{args[1]}" not in storage.all():
                print("** no instance found **")
                return
            else:
                del storage.all()[f"{args[0]}.{args[1]}"]
                storage.save()
                return

    def do_all (self, args):
        args = args.replace('  ', ' ').replace('\n', ' ').split(' ')
        if len(args) == 1 and args[0] == '':
            print(storage.all())
        else:
            for arg in args:
                if arg not in HBNBCommand.__classes:
                    print("** class doesn't exist **")
                else:
                    for key, value in storage.all().items(): 
                        if key.startswith(arg):
                            print(value)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
