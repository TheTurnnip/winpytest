import os
#Import the required OS library 


def ops():
    a="A) Run all commands"
    b="B) sfc"
    c="C) dism" 
    d="D) chkdsk"
    print(a + "\n" + b + "\n" + c + "\n" + d)
    choice()

#List the options for the user

def choice():
    op = input("Please Select a letter:")
    selections = ["A", "a", "B", "b", "C", "c", "D", "d"]
    if op == selections[0] or op == selections[1]:
        op_a()
    elif op == selections[2] or op == selections[3]:
        op_b()
    elif op == selections[4] or op == selections[5]:
        op_c()
    elif op == selections[5] or op == selections[6]:
        op_d()
    elif op != selections:
        print("ERROR CODE: 100, not proper selection")
        ops()

#Evaluates the users selction against a list of valid options and then run the corosponding function.

sysfilecheck='sfc /scannow >> /winpytest.txt'
deployimg='DISM /Online /Cleanup-Image /RestoreHealth >> /winpytest.txt'
checkdisk='echo y | chkdsk /r >> /winpytest.txt'
reboot_command='shutdown /r'

#Defines the commands that will be run.

def op_a():
    os.system(sysfilecheck)
    os.system(deployimg)
    os.system(checkdisk)
    reboot()

def op_b():
    os.system(sysfilecheck)
    reboot()

def op_c():
    os.system(deployimg)
    reboot()

def op_d():
    os.system(checkdisk)
    reboot()

#the op_ functions run the commands that are provided in the variables

def reboot():
    selection = input("Do you wish to reboot now?(y/N):")
    if selection == "y" or selection == "Y":
        os.system(reboot_command)
    else:
        print("Reboot PC later for commands to complete")

#Gives the user an option to reboot after they have made the selection


ops()
