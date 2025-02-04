# Class Attendance System

The **Class Attendance System** is a Python-based application designed to streamline the process of managing student attendance. It provides a user-friendly console menu for adding/removing students, taking attendance, generating weekly reports, and viewing the class roster.

## Features

- **Add/Remove Students**  
  Easily add or remove students from the class roster.

- **Take Attendance**  
  Record attendance for each student with options for:
  - Present
  - Tardy
  - Absent Excused
  - Absent Unexcused

- **Generate Weekly Reports**  
  View a summary of attendance records for the week.

- **View Class Roster**  
  Display the current list of students in the class.

- **Console Menu Interface**  
  A simple and interactive menu system for navigating the program.

## File Descriptions

- **attendance.py**  
  Contains core functions for managing attendance, including:
  - Adding and removing students.
  - Taking attendance.
  - Generating weekly reports.
  - Viewing the class roster.

- **main.py**  
  Implements the console menu interface using the `consolemenu` library. Provides options to interact with the functions defined in `attendance.py`.

## How to Use

1. Clone this repository to your local machine:
git clone https://github.com/muditm006/Class-Attendance.git
cd Class-Attendance
2. Install the required Python library:
pip install console-menu
3. Run the program:
python main.py

4. Use the interactive menu to:
- Add or remove students.
- Take attendance.
- Generate weekly reports.
- View the class roster.

5. Follow on-screen instructions to complete your tasks.

## Notes

- The program creates and manages text files (`class_attendance.txt`, `Class Report.txt`, etc.) to store data persistently.
- If this is your first time using the program, you will be prompted to initialize empty files for storing class data.

## Example Menu Options

CAP Attendance System
'Here for all your attendance taking needs!'
- Add Student
- Remove Student
- Take Attendance
- Week Report
- Class Roster

Select an option by entering its corresponding number.

## Libraries Used

- **os**: For file handling and system operations.
- **consolemenu**: For creating an interactive console menu interface.
