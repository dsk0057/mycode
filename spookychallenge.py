#!/usr/bin/python3
"""spooky challenge that counts the word 'vampire' in dracula.txt """

# main function
def main():

    # counter for the word 'vampire'
    vampcount = 0

    # open the file for reading and assign a variable
    with open("/home/student/dracula.txt", "r") as spookyfile:
        with open("/home/student/vampytimex.txt", "w") as vampyfile:

            # loop over the file and read the content
            for line in spookyfile:

                # check if 'vampire' is present in the file/also check for case sensitiveness
                if "vampire" in line.lower():
                    print(line)

                    # increase the count of 'vampire' by 1 every time it is encountered
                    vampcount += 1
                    
                    # write the lines with 'vampire' words into vampytimes.txt
                    vampyfile.write(line)
    
    # display the count
    print(f"\nThe word vampire appears {vampcount} times.") 

# run the main() function
if __name__ == "__main__":
    main()
