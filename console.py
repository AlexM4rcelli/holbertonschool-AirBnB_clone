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
        else:
            args.replace('  ', ' ').replace('\n', ' ')
            for arg in args.split(' '):
                if arg not in storage.all().keys():
                    print (" ** class doesn't exist ** ")
                else:
                    newinstance = BaseModel()
                    newinstance.save()
                    print(newinstance.id)

    
if __name__ == '__main__':
    HBNBCommand().cmdloop()