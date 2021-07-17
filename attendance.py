import os
clear= lambda: os.system("clear")
restart = open("class_attendance.txt", "a")
restart.write("\n")
restart.close()
loop="yes"
student=0
again="yes"
sarah="yes"
repeat="yes"
week=["Monday","Tuesday","Wednesday","Thursday","Friday"]
def listToString(s):  
        str1 = ""  
        for ele in s:  
          str1 += ele   
        return str1  
print("Hello, Welcome to the Class Attendance Program!")
print("Is this your first time using the program? Print 'Yes' if it is,")
r= input("if it is not, print anything else to begin! ")
r=r.lower()
if r=="yes":
  if os.path.exists("Checky.txt"):
    os.remove("Checky.txt")
  if os.path.exists("Check.txt"):
    os.remove("Check.txt")
  open('Class Report.txt', 'w').close()
  open('class_roster.txt', 'w').close()
  open('class_attendance.txt', 'w').close()
while sarah=="yes":
  print("\n")
  print("Add Student----------------(1)")
  print("Remove Student-------------(2)")
  print("Take Attendance------------(3)")
  print("Week Report----------------(4)")
  print("View Class Roster----------(5)")
  print("Clear----------------------(6)")
  print("Close Program--------------(7)")
  print("\n")
  while True:
    try:
      a= int(input("What would you like to do? "))
      if a not in range(0,8):
        print("Integer not in range!")
      else:
        break
    except:
        print("Print Valid Input!")
  if a==1:
      checky= open("Checky.txt","w+")
      checky.write("hello")
      checky.close()
      again = "yes"
      while again == "yes":
        f = open("class_attendance.txt", "r")
        with open("class_attendance.txt", "r") as f:
          lines = f.readlines()
        with open("class_roster.txt", "w") as f:
          for line in lines:
            if line.strip("\n") != "":
              f.write(line)
        six= open("class_roster.txt", "r")
        students=six.readlines()
        q=listToString(students)
        print("Current students in class: \n" + q)
        f = open("class_attendance.txt", "a")
        f.write("\n")
        b = input("Name of student you would like to add: ")
        f.write(b+"\n")
        print("Do you want to add another student? Print 'Yes' to do so,")
        again= input("if you don't wish to do so, print anything else to go to menu! ")
        again = again.lower()
        if again != "yes":
          f.close()
  if a==2:
      repeat="yes"
      while repeat=="yes":
        if os.path.exists("Checky.txt")==False:
          print("No students in the class!")
          break
        f = open("class_attendance.txt", "r")
        print("Students in Class: \n")
        with open("class_attendance.txt", "r") as f:
          lines = f.readlines()
        with open("class_roster.txt", "w") as f:
          for line in lines:
            if line.strip("\n") != "":
              f.write(line)
        six= open("class_roster.txt", "r")
        students=six.readlines()
        q=listToString(students)
        print(q)
        c=input("What name do you want to remove? ")
        if c=="":
          print("Not Valid Input!")
          f=open("class_attendance.txt", "r")
        else:
          with open("class_attendance.txt", "r") as f:
            lines = f.readlines()
          with open("class_attendance.txt", "w") as f:
            for line in lines:
              if line.strip("\n") != c:
                f.write(line)
          if (c+"\n") not in lines:
            print("Student does not exist")
          else: 
            print(c+" removed from list")
        print("Do you want to remove another student? Print 'Yes' to do so,")
        repeat= input("if you don't wish to do so, print anything else to go to menu! ")
        repeat=repeat.lower() 
        if repeat!="yes":
          f.close()
  if a==3:
      loop="yes"
      while loop=="yes":
        if os.path.exists("Checky.txt")==False:
          print("No students in the class!")
          break
        check= open("Check.txt","w+")
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
        g.write(h+"\n")
        print("Attendance Options:")
        print("Present--------------------(1)")
        print("Tardy----------------------(2)")
        print("Absent Excused-------------(3)")
        print("Absent Unexcused-----------(4)")
        for element in i:
          l=i.readlines(student)
          m= listToString(l)
        for name in m.split():
          while True:
            try:
              k= int(input(name+" attendance status on " + h + ": "))
              if k not in range(0,5):
                print("Integer not in range!")
              else:
                break
            except:
                print("Print Valid Input!")
          if k==1:
            k="Present"
          if k==2:
            k="Tardy"
          if k==3:
            k="Absent Excused"
          if k==4:
            k="Absent Unexcused"
          n=name+": "+ k+ "\n"
          g.write(n)
          print("Attendance updated for " + name)
          student=student+1
        g.close()
        i.close()
        loop="no"
        student=0
  if a==4:
      if os.path.exists("Check.txt")==False:
        print("You have not taken attendance yet!")
      else:
        n=open("Class Report.txt","r")
        o=n.readlines()
        p=listToString(o)
        print("Here is your report for the week!")
        print(p)
  if a==5:
      if os.path.exists("Checky.txt")==False:
          print("No students in the class!")
      else:
        f = open("class_attendance.txt", "r")
        print("Students in Class: \n")
        with open("class_attendance.txt", "r") as f:
          lines = f.readlines()
        with open("class_roster.txt", "w") as f:
          for line in lines:
            if line.strip("\n") != "":
              f.write(line)
        six= open("class_roster.txt", "r")
        students=six.readlines()
        q=listToString(students)
        print(q)
  if a==6:
    clear()
    print("Cleared.")
  if a==7:
    clear()
    print("Have a nice day!")
    print("-------------------------------") 
    print(" Thank you for using our system") 
    print("-------------------------------")
    break
