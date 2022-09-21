#!/usr/bin/env python3

# take user input
hostname = input("What value should we set for hostname?")

# test the input based on desired response
if hostname.lower() == "mtg":
    print("The hostname was found to be mtg")
    print("The hostname matches expected config")

print("Exiting the script")
