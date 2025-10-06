import time
import os
from colorama import Fore, init
from pyfiglet import Figlet
import msvcrt
import subprocess
init()

# Probably need this at some point:
# key = msvcrt.getch().decode().lower()
#    if key == "key here":

# name = subprocess.run(["command", "add to command"], capture_output=True, text=True)
# print(name.stdout)
ascii = Figlet(font="slant")
user = os.getlogin()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


#Checker with some example code

def feature1():
    clear()
    print(ascii.renderText("Feature 1"))
    print("Press" + Fore.RED + " Q " + Fore.WHITE + "to go back to the menu")
    print("<----------------------->")
    print("1. Check Google.com")
    print("2. Check Wikipedia.com")
    print("3. Check YouTube.com")
    print("<----------------------->" + "\n" + Fore.RED + f"<{user}>" + Fore.WHITE + " : ", end="")
    key = msvcrt.getch().decode().lower()
    if key.lower() == "q":
        clear()
        menu()
    elif key == "1":
        clear()
        time.sleep(0.5)
        print("Pinging google.com")
        google = subprocess.run(["ping", "google.com"], capture_output=True, text=True)
        print(google.stdout)
        while True:
            print("<----------------------->")
            print("Press" + Fore.RED + " Q " + Fore.WHITE + "to go back to Feature 1")
            print("<----------------------->")
            back_key = msvcrt.getch().decode().lower()
            if back_key.lower() == "q":
                clear()
                feature1()
                break
    elif key == "2":
        clear()
        time.sleep(0.5)
        print("Pinging wikipedia.com")
        wikipedia = subprocess.run(["ping", "wikipedia.com"], capture_output=True, text=True)
        print(wikipedia.stdout)
        while True:
            print("<----------------------->")
            print("Press" + Fore.RED + " Q " + Fore.WHITE + "to go back to Feature 1")
            print("<----------------------->")
            back_key = msvcrt.getch().decode().lower()
            if back_key == "q":
                clear()
                feature1()
                break
    elif key == "3":
        clear()
        time.sleep(0.5)
        print("Coming soon")
        while True:
            print("<----------------------->")
            print("Press" + Fore.RED + " Q " + Fore.WHITE + "to go back to Feature 1")
            print("<----------------------->")
            key = msvcrt.getch().decode().lower()
            if key == "q":
                clear()
                feature1()



def feature2():
    clear()
    print(ascii.renderText("Feature 2"))
    print("Press" + Fore.RED + " Q " + Fore.WHITE + "to go back to the menu")
    print("<----------------------->")
    print("1. Option 1")
    print("2. Option 2")
    print("3. Option 3")
    print("<----------------------->" + "\n" + Fore.RED + f"<{user}>" + Fore.WHITE + " : ", end="")
    key = msvcrt.getch().decode().lower()
    if key.lower() == "q":
        clear()
        menu()
    elif key == "1":
        clear()
        time.sleep(0.5)
        print("Coming soon...")
        while True:
            print("<----------------------->")
            print("Press" + Fore.RED + " Q " + Fore.WHITE + "to go back to Feature 2")
            print("<----------------------->")
            key = msvcrt.getch().decode().lower()
            if key.lower() == "q":
                feature2()
                break
    elif key == "2":
        clear()
        time.sleep(0.5)
        print("Coming soon...")
        while True:
            print("<----------------------->")
            print("Press" + Fore.RED + " Q " + Fore.WHITE + "to go back to Feature 2")
            print("<----------------------->")
            key = msvcrt.getch().decode().lower()
            if key.lower() == "q":
                feature2()
                break
    elif key == "3":
        clear()
        time.sleep(0.5)
        print("Coming soon...")
        while True:
            print("<----------------------->")
            print("Press" + Fore.RED + " Q " + Fore.WHITE + "to go back to Feature 2")
            print("<----------------------->")
            key = msvcrt.getch().decode().lower()
            if key.lower() == "q":
                feature2()
                break






def feature3():
    clear()
    print(ascii.renderText("Feature 3"))
    print("Press" + Fore.RED + " Q " + Fore.WHITE + "to go back to the menu")
    print("<----------------------->")
    print("1. Option 1")
    print("2. Option 2")
    print("3. Option 3")
    print("<----------------------->" + "\n" + Fore.RED + f"<{user}>" + Fore.WHITE + " : ", end="")
    key = msvcrt.getch().decode().lower()
    if key.lower() == "q":
        clear()
        menu()
    elif key == "1":
        clear()
        time.sleep(0.5)
        print("Coming soon...")
        while True:
            print("<----------------------->")
            print("Press" + Fore.RED + " Q " + Fore.WHITE + "to go back to Feature 3")
            print("<----------------------->")
            key = msvcrt.getch().decode().lower()
            if key.lower() == "q":
                feature3()()
                break
    elif key == "2":
        clear()
        time.sleep(0.5)
        print("Coming soon...")
        while True:
            print("<----------------------->")
            print("Press" + Fore.RED + " Q " + Fore.WHITE + "to go back to Feature 3")
            print("<----------------------->")
            key = msvcrt.getch().decode().lower()
            if key.lower() == "q":
                feature3()()
                break
    elif key == "3":
        clear()
        time.sleep(0.5)
        print("Coming soon...")
        while True:
            print("<----------------------->")
            print("Press" + Fore.RED + " Q " + Fore.WHITE + "to go back to Feature 3")
            print("<----------------------->")
            key = msvcrt.getch().decode().lower()
            if key.lower() == "q":
                feature3()
                break

def menu():
    print(ascii.renderText("Menu"))
    print("Version:" + Fore.GREEN + "Newest" + Fore.WHITE)
    print("<----------------------->")
    print("1. Feature 1")
    print("2. Feature 2")
    print("3. Feature 3")
    print("<----------------------->" + "\n" + Fore.RED + f"<{user}>" + Fore.WHITE + " : ", end="")
    key = msvcrt.getch().decode().lower()
    if key == "1":
        print("Feature 1 loading...")
        time.sleep(0.5)
        clear()
        time.sleep(0.5)
        feature1()
    elif key == "2":
        print("Feature 2 loading...")
        time.sleep(0.5)
        clear()
        time.sleep(0.5)
        feature2()
    elif key == "3":
        print("Feature 3 loading...")
        time.sleep(0.5)
        clear()
        time.sleep(0.5)
        feature3()
    elif key.lower() == "q":
        print("Quiting..")
        time.sleep(1)
        exit()
        

#where the actual program runs

print(ascii.renderText("checker"))
print(f"Welcome to my program" + Fore.RED + f" {user}" + Fore.WHITE + ". Would you like to continue? (Y/N)" + "\n" + Fore.RED + f"<{user}>" + Fore.WHITE + " : ", end="")
while True:
    key = msvcrt.getch().decode().lower()
    if key.lower() == "y":
        clear()
        time.sleep(0.5)
        menu()
        break
    elif key.lower() == "n":
        time.sleep(0.5)
        print("Ayt")
        time.sleep(1)
        exit()
        break