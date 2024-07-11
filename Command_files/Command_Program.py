import cmd
import os
import subprocess
from subprocess import run
import sys
from sys import exit
from datetime import datetime
import datetime

def TimeBased():
    current_time = datetime.datetime.now()
    if current_time.hour < 12:
        print("\nGood morning!\n")
    elif 12 <= current_time.hour < 18:
        print("\nGood afternoon!\n")
    else:
        print("\nGood evening!\n")
class MyCmdPrompt(cmd.Cmd):
    TimeBased()    
    intro = 'Welcome to my command prompt. Type help or ? to list commands.\nThe application provides an interactive command prompt where users can \ntype commands and receive responses.\n'
    prompt = '(cmd)$'

    def do_greet(self, line):
        print("Hello,", line)

    def do_exit(self, line):
        return True

    def do_cls(self,line):
        # Check if the operating system is Windows
        if os.name == 'nt':
            os.system('cls')

    def do_add(self, line):
        numbers = line.split()
        if len(numbers) == 2:
            try:
                result = float(numbers[0]) + float(numbers[1])
                print(f"The sum is: {result}")
            except ValueError:
                print("Please enter two valid numbers separated by a space.")
        else:
            
            print("Please enter two numbers separated by a space.")
            
    def do_date(self,line):
        print(f"Current Date : {datetime.datetime.today().date()}")

    def do_time():
        hr=datetime.datetime.today().hour
        mins=datetime.datetime.today().minute
        print(f"Current Time : {hr}:{mins} {datetime.datetime.today().strftime("%pcls")}")

    def do_dir():
        all_entries = os.listdir('.')
        # Filter out the entries that are directories
        directories = [entry for entry in all_entries if os.path.isdir(entry)]
        # Print the list of directories
        for directory in directories:
            print(directory)            

    def do_start(self,program_path):
        try:
            # Attempt to open the program
            subprocess.Popen([program_path])
            print(f"Program {program_path} opened successfully.")
        except Exception as e:
            print(f"An error occurred while trying to open the program: {e}")

    def do_shutdownS(self,line):
        os.system('shutdown /s')

    def do_shutdownf(self,line):
        os.system('shutdown /f')

    def do_restart(self,line):
        os.system('shutdown /r')

    def do_open(self,line):
        try:
            print("\nSelct a Programs to open")
            print("1 : Momo Program")
            print("2 : Calculator")
            print("3 : Rock paper Scissors")
            sel=int(input(">"))
            if(sel==1):
                from util_files import MobileMoney_Program2
                MobileMoney_Program2.Main()
            elif(sel==2):
                from util_files import Calcualtor
                Calcualtor.Calcu()
            elif(sel==3):
                from util_files import RPS1
                RPS1.rock_paper_scissors()
            else:
                print("invalid Syntax.")
        except Exception:
            print("invalid Syntax.")
            sys.exit()
    

if __name__ == '__main__':
    MyCmdPrompt().cmdloop()
    

