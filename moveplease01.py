#!/usr/bin/env python3

# import libraries
import shutil
import os

# main function
def main():

    # force the Python program to start in the home user directory for us
    os.chdir("/home/student/mycode/")

    # move the file/folder at the path source to the path destination
    shutil.move("raynor.obj", "ceph_storage/")

    # prompt the user for a new name for the kerrigan.obj file
    xname = input("What is the new name for kerrigan.obj?")

    # Rename the current kerrigan.obj file
    shutil.move("ceph_storage/kerrigan.obj", "ceph_storage/" + xname)

if __name__ == "__main()__":
    main()
