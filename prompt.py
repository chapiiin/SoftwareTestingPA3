from bmi import calculate_bmi
from retirement import calculate_retirement
import sys


def user_prompt(user_choice):
    choice = user_choice
    if (choice == ' '):
        choice = str(input("Choose a function below (1 or 2). Enter 'x' to exit the program at anytime.\n 1) Body Mass Index Calculator \n 2) Retirement Plan Calculator\n"))

    if (choice == "x"):
        print("Exiting program.")
        return sys.exit(0)
    elif (choice == "1"):
        print("Body Mass Index Calculator chosen.\n")
        valid_choice = True
        return [choice, valid_choice]
    elif (choice == "2"):
        print("Retirement Plan Calculator chosen.\n")
        valid_choice = True
        return [choice, valid_choice]
    else:
        print("Please, enter a valid choice from the options provided.\n")
        return [choice, False]
        
def main():
    valid_choice = False
    while (valid_choice == False):
        choice, valid_choice = user_prompt(' ')
        
    if (choice == "1"):
        calculate_bmi()
    elif (choice == "2"):
        calculate_retirement()        
    print()
    print("----------------------------------------")
    print()
    main()

if __name__ == "__main__":
    main()
