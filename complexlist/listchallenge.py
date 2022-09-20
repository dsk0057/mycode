#!/usr/bin/env python3

import random

def main():

    wordbank= ["indentation", "spaces"] 

    tlgstudents= ["Aaron", "Andy", "Asif", "Brent", "Cedric", "Chris", "Cory", "Ebrima", "Franco", "Greg", "Hoon", "Joey", "Jordan", "JC", "LB", "Mabel", "Shon", "Pat", "Zach"]

    wordbank.append(4)

    num = input("Enter a number between 0 and 18: ")

    if num in tlgstudents:
        print(f"{num} always uses {wordbank[2]} {wordbank[1]} to indent.")
    elif num not in tlgstudents and num != num:
        print("Please enter either a number between 0 and 18, or one of the names from the provided list.")
    else:

        random_num = random.randint(0, 19)

        student_name = tlgstudents[int(num)]

        random_student_name = tlgstudents[random_num]

        print(f"{student_name} always uses {wordbank[2]} {wordbank[1]} to indent.")

        print(f"{random_student_name} always uses {wordbank[2]} {wordbank[1]} to indent.")

if __name__ == "__main__":
    main()
