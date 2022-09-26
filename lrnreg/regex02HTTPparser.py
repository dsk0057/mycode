#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
A script to demonstrate the power of Regular Expression (regex) and
the requests library."""

# standard library imports go above 3rd party imports (best practice)
import re

# python3 -m pip install requests
import requests

def main():
    """Search a website's content"""

    matches_count = 0

    print("Where should we search?")
    url = input("> ")  # collect user input

    while True:

        print(f"Great! So we'll try to open this URL {url} to search for the phrase:")
        searchFor = input("> ")

        resp = requests.get(url)  # Send HTTP GET
        searchMe = resp.text      # strip everything off the response as a string (text)

        # use the re.search() to determine if our website has the pattern we are looking for
        # it works by taking arguments, the first is the regex search pattern, and the second
        # is the string to search within

        if searchFor == "quit":
            break

        if re.search(searchFor, searchMe):
            matches_count += 1
            print(f"Found a match! There are {matches_count} matches for {searchFor} in the webpage.")
        else:
            print("No match!")


if __name__ == "__main__":
    main()

