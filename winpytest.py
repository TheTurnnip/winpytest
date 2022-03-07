
#    winpytest, a python script to test and atempt to fix corrupted windows installs.
#    Copyright (C) 2022  Ryan Steffan
# 
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
# 
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
# 
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

#-----------------------------------------------------------------------------

import os

#Import the required OS library 

def license():
    print("\n" + """    winpytest  Copyright (C) 2022  Ryan Steffan
    This program comes with ABSOLUTELY NO WARRANTY.
    This is free software, and you are welcome to redistribute it
    under certain conditions; type `L, when prompted for letter' for details.""" + "\n")
    ops()

def ops():
    a="A) Run all commands"
    b="B) sfc"
    c="C) dism" 
    d="D) chkdsk"
    l="L) License details"
    print(a + "\n" + b + "\n" + c + "\n" + d + "\n" + l)
    choice()

#List the options for the user

def choice():
    op = input("Please Select a letter:")
    selections = ["A", "a", "B", "b", "C", "c", "D", "d", "L"]
    if op == selections[0] or op == selections[1]:
        op_a()
    elif op == selections[2] or op == selections[3]:
        op_b()
    elif op == selections[4] or op == selections[5]:
        op_c()
    elif op == selections[6] or op == selections[7]:
        op_d()
    elif op == selections[8]:
        show_license()
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

def show_license():
    print("Please visit for more details: https://github.com/TheTurnnip/winpytest/blob/master/LICENSE")
    exit_sig=input("Press any key to exit...")

#Provides the user with the details of GPL V3.0

license()
