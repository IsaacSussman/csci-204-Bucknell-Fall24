"""
This is the main file of the starter code for the Maps week activities.
Run this file to test your implementation.
You do not need to edit this file (probably, unless it's broken somehow).

You don't need to change the following:
- Record
- read_record
- BinaryNode
- Node
- The hash function in the OpenMap class
- all of the create functions

You should complete the orderedmaps, openmaps, and closedmaps files by the end of the week.
"""

from given_classes import *
from orderedmaps import OrderedMap, create_ordered_map
from openmaps import OpenMap, create_open_map
from closedmaps import ClosedMap, create_closed_map
import time

# Run the software!
# You don't need to touch anything below
if __name__ == "__main__" :
    print("\n" * 1000 + 
"""
Welcome to the very secure and very professional license plate lookup system.          
""")
    # Obtain the file you want to load the database from
    filename = ""
    usr_in = input("Would you like the test database (0) or the real McCoy (1)?\n")
    if usr_in == "0" :
        filename = "test_license_records.txt"
    else : 
        filename = "license_records.txt"
    
    # Database loading message
    print("Database loading...")

    # Open the file and determine the format of the database
    file = open(filename, "r")
    usr_in = input("Would you like to run in \n(0) Ordered Map Mode, \n(1) Open Map Mode, or \n(2) Closed Map Mode?\n")

    start = time.time()

    if usr_in == "0" :
        database = create_ordered_map(file)
    elif usr_in == "1" :
        database = create_open_map(file) 
    else :
        database = create_closed_map(file) 
    
    dur = time.time() - start

    # Close the file
    file.close()

    # Database loaded message 
    print("\n"*1000 + 
    """
Welcome to the very secure and very professional license plate lookup system.          
""")
    print(f"Database of {database.size} records loaded in {dur:.4f} seconds.")

    # User interaction
    while True :
        inp_key = input("\nWhat license plate are you interested in?\n")

        start = time.time()
        retrieved = database.get(inp_key)
        dur = time.time() - start
        print(f"\nSearch took {dur:.4f} seconds.\n")

        if type(retrieved) in [Node, BinaryNode, Record] :
            print("There is a person on file with that plate.")
            print(retrieved)

            if usr_in in ["1", "2"]:
                inp = input("\nWould you like to delete this record?\n")
                if inp.strip().lower() == "yes" :
                    database.delete(inp_key)
        else :
            print("There is nobody on file with that license plate.")

        inp = input("\nWould you like to look up another plate (yes/no)?\n")

        if "no" == inp.strip().lower() :
            break
        else : 
            print()