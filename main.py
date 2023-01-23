from menu import main_menu, project_menu, employee_menu
import os,sys,time

op = 0
while(op != 3):
    main_menu()
    op = int(input("Choose an option:"))
    if op == 1:
        employee_menu()
    elif op == 2:
        project_menu()
    elif op == 3:
        break
    else:
        print("Enter a valid option\n")
        time.sleep(1)




