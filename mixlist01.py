#!/#usr/bin/env python3

# create a list my_list containing three items
#my_list = [ "192.168.0.5", 5060, "UP" ]

# print the first item in the list
#print(f"The first item in the list: {my_list[0]}")

# print the second item in the list
#print(f"The second item in the list: {my_list[1]}")

# print the last item in the list
#print(f"The last item in the list: {my_list[2]}")

"""
def main():

# create a list iplist with given items
    iplist = [5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh"]

    for items in iplist:
        if "." in iplist:
            print(f"The IP addresses are: {iplist}")
        else:
            print("There are no IP address in the given list.")

main()
"""

# display only the IP addresses to the screen.
iplist = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]

# example 1 - add up the strings
print("IP addresses: " + iplist[3] + ", and " + iplist[4])

# example 2 - use the comma separator
print("IP addresses:", iplist[3], ", and", iplist[4])

# example 3 - use an 'f-string'
print(f"IP addresses: {iplist[3]}, and {iplist[4]}")

