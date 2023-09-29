import os

def sort(STUDENTS):
    os.system("cls")
    choice = input("Ascending or Descending order(low caps): ")

    print("SORTING STUDENTS BASED ON AVERAGE")
    for i in STUDENTS:
        i.setAverage()
    if choice.lower() == "descending":
        for s in range(len(STUDENTS)):
            min_idx = s
            for i in range(s + 1, len(STUDENTS)):
                if STUDENTS[i].average > STUDENTS[min_idx].average:
                    min_idx = i
            (STUDENTS[s], STUDENTS[min_idx]) = (STUDENTS[min_idx], STUDENTS[s])

        for i in STUDENTS:
            i.printInfo()
            print("--------------\n")

    elif choice.lower() == "ascending":
        for s in range(len(STUDENTS)):
            min_idx = s
            
            for i in range(s + 1, len(STUDENTS)):
                if STUDENTS[i].average < STUDENTS[min_idx].average:
                    min_idx = i
    
            (STUDENTS[s], STUDENTS[min_idx]) = (STUDENTS[min_idx], STUDENTS[s])
        for i in STUDENTS:
            i.printInfo()
            print("--------------\n")


    print("STUDENT LIST HAS BEEN SORTED OUT BASED ON AVERAGE!")

    os.system("pause")
    os.system("cls")