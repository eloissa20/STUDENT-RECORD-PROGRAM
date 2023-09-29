#DONE BY PAIR
#ANDAL, MARIA ELOISSA M.
#ENRIQUEZ, SIGNET B.

import os
from Andal_MariaEloissa_Student_Record import *
from Andal_MariaEloissa_sorting import sort


STUDENTS = []


def menu():
    print("----MENU----\n1. Add Student\n2. Add Subject\n3. Add grade\n4. View/Display Student Record\n5. Search Student Record\n6. Update Student Record\n7. Delete Student Record\n8. Save Student Record in csv File\n9. Read Student Record from a csv File\n10. Sort Student Record by Average(Ascending or Descending order)\n11. Quit")


def main():
    choice = ' '

    while (choice != '11'):
        menu()
        print("\n--------------------")
        choice = input("Choice: ")

        if choice == '1':
            addStudent(STUDENTS)
        elif choice == '2':
            addSubject(STUDENTS)
        elif choice == '3':
            addGrade(STUDENTS)
        elif choice == '4':
            display(STUDENTS)
        elif choice == '5':
            search(STUDENTS)
        elif choice == '6':
            update(STUDENTS)
        elif choice == '7':
            delete(STUDENTS)
        elif choice == '8':
            write(STUDENTS)
        elif choice == '9':
            read(STUDENTS)
        elif choice == '10':
            sort(STUDENTS)
        elif choice == '11':
            os.system("cls")
            print("Thank you Goodbye!")
            os.system("pause")
            os.system("cls")


if __name__ == "__main__":
    main()
