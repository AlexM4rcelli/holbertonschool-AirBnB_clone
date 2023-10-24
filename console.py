#!/usr/bin/python3
"""entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel
from models.__init__ import storage

class HBNBCommand(cmd.Cmd):
    """interpreter"""
    prompt = "(hbnb) "
    
    
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
            args.replace('  ', ' ').replace('\n', ' ')
            for arg in args.split(' '):
                if arg not in storage.all().keys():
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
            args.replace('  ', ' ').replace('\n', ' ')
            if len(args.split()) > 2:
                print('Usage: ClassName ClassName_id')
                return
            if args[0] not in storage.all().keys():
                print (" ** class doesn't exist ** ")
                return
            if len(args.split()) == 1:
                print(" ** instance id missing ** ")
                return
            if args[1] not in BaseModel.all():
                print("** no instance found **")

    
if __name__ == '__main__':
    HBNBCommand().cmdloop()