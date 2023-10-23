#!/usr/bin/python3
"""entry point of the command interpreter"""
import cmd

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
    
if __name__ == '__main__':
    HBNBCommand().cmdloop()