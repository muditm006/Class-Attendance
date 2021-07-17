import os
student = 0
week=["Monday","Tuesday","Wednesday","Thursday","Friday"]
def listToString(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1
def add():
    checky = open("Checky.txt", "w+")
    checky.write("hello")
    checky.close()
    f = open("class_attendance.txt", "r")
    with open("class_attendance.txt", "r") as f:
        lines = f.readlines()
    with open("class_roster.txt", "w") as f:
        for line in lines:
            if line.strip("\n") != "":
                f.write(line)
    six = open("class_roster.txt", "r")
    students = six.readlines()
    q = listToString(students)
    print("Current students in class: \n" + q)
    f = open("class_attendance.txt", "a")
    f.write("\n")
    b = input("Name of student you would like to add: ")
    f.write(b + "\n")
def remove():
    if os.path.exists("Checky.txt") == False:
        print("No students in the class!")
        input("Print anything to go back to menu. ")
    f = open("class_attendance.txt", "r")
    print("Students in Class: \n")
    with open("class_attendance.txt", "r") as f:
        lines = f.readlines()
    with open("class_roster.txt", "w") as f:
        for line in lines:
            if line.strip("\n") != "":
                f.write(line)
    six = open("class_roster.txt", "r")
    students = six.readlines()
    q = listToString(students)
    print(q)
    c = input("What name do you want to remove? ")
    if c == "":
        print("Not Valid Input!")
        f = open("class_attendance.txt", "r")
    else:
        with open("class_attendance.txt", "r") as f:
            lines = f.readlines()
        with open("class_attendance.txt", "w") as f:
            for line in lines:
                if line.strip("\n") != c:
                    f.write(line)
        if (c + "\n") not in lines:
            print("Student does not exist")
            input("Print anything to go back to menu. ")
        else:
            print(c + " removed from list")
            input("Print anything to go back to menu. ")
def attendance():
    global student
    if os.path.exists("Checky.txt") == False:
        print("No students in the class!")
    check = open("Check.txt", "w+")
    check.write("hello")
    check.close()
    g = open("Class Report.txt", "a")
    i = open("class_attendance.txt", "r")
    while True:
        try:
            h = input("What day of the week is it? ")
            if h not in week:
                print("That is not a valid day of the week!")
            else:
                break
        except:
            print("Print Valid Input!")
    g.write(h + "\n")
    print("Attendance Options:")
    print("Present--------------------(1)")
    print("Tardy----------------------(2)")
    print("Absent Excused-------------(3)")
    print("Absent Unexcused-----------(4)")
    for element in i:
        l = i.readlines(student)
        m = listToString(l)
    for name in m.rsplit("\n"):
        if name == "":
            pass
        else:
            while True:
                try:
                    k = int(input(name + " attendance status on " + h + ": "))
                    if k not in range(0, 5):
                        print("Integer not in range!")
                    else:
                        break
                except:
                    print("Print Valid Input!")
            if k == 1:
                k = "Present"
            if k == 2:
                k = "Tardy"
            if k == 3:
                k = "Absent Excused"
            if k == 4:
                k = "Absent Unexcused"
            n = name + ": " + k + "\n"
            g.write(n)
            print("Attendance updated for " + name)
            student = student + 1
    g.close()
    i.close()
    loop = "no"
    student = 0
def report():
    if os.path.exists("Check.txt") == False:
        print("You have not taken attendance yet!")
        input("Print anything to continue ")
    else:
        n = open("Class Report.txt", "r")
        o = n.readlines()
        p = listToString(o)
        print("Here is your report for the week!")
        print(p)
        input("Print anything to continue ")
def roster():
    if os.path.exists("Checky.txt") == False:
        print("No students in the class!")
        input("Print anything to go back to menu! ")
    else:
        f = open("class_attendance.txt", "r")
        print("Students in Class: \n")
        with open("class_attendance.txt", "r") as f:
            lines = f.readlines()
        with open("class_roster.txt", "w") as f:
            for line in lines:
                if line.strip("\n") != "":
                    f.write(line)
        six = open("class_roster.txt", "r")
        students = six.readlines()
        q = listToString(students)
        print(q)
        input("Print anything to go back to menu! ")
# Import the necessary packages
from consolemenu import *
from consolemenu.items import *

# Create the menu
menu = ConsoleMenu("CAP Attendance System", "'Here for all your attendance taking needs!'")
# A FunctionItem runs a Python function when selected
addstudent = FunctionItem("Add Student", add)
removestudent = FunctionItem("Remove Student", remove)
takeattendance = FunctionItem("Take Attendance", attendance)
weekreport= FunctionItem("Week Report", report)
classroster= FunctionItem("Class Roster", roster)

menu.append_item(addstudent)
menu.append_item(removestudent)
menu.append_item(takeattendance)
menu.append_item(weekreport)
menu.append_item(classroster)


# Finally, we call show to show the menu and allow the user to interact
menu.show()
