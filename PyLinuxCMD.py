#PyLinuxCMD
import os
def ls():
    PATH = input("Где:")
    os.system("dir" + PATH)
def notpad():
    os.system("notepad")
def calculatlor():
    os.system("calc")
def dbg():
    print("Works!")
def cd():
    cdw = input("Куда?:")
    os.system("cd " + cdw )
while True:
    answer = input("Что сделать:")
    if answer == "ls":
        ls()
        break
    elif answer == "Калькоулятор":
        calculatlor()
        break
    elif answer == "Блокнот":
        notpad()
        break
    elif answer == "debug":
        dbg()
        break
    elif answer == "Выйти":
        exit()
    elif answer == "cd":
        cd()
        break
    else:
        print("Такого нет")
