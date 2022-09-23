#!/usr/bin/env python3

def main():

    category=0 

    wind_speed = int(input("Enter the wind speed in mph: "))

    if wind_speed >= 157:
        category = 5
        print(f"This is a Category {category} hurricane. Please take immediate action and keep on monitioring latest updates from the National Hurricane Center.")

    elif wind_speed >= 130:
        category = 4
        print(f"This is a Category {category} hurricane. Please take caution per the National Hurricane Center message.")

    elif wind_speed >= 111:
        category = 3
        print(f"This is a Category {category} hurricane. Please take caution per the National Hurricane Center message.")

    elif wind_speed >= 96:
        category = 2
        print(f"This is a Category {category} hurricane. Please take caution per the National Hurricane Center message.")

    elif wind_speed >= 74:
        category = 1
        print(f"This is a Category {category} hurricane. Please take caution per the National Hurricane Center message.")

    else:
        print("Don't worry! It is a routine wind.")

if __name__ == "__main__":
    main()

