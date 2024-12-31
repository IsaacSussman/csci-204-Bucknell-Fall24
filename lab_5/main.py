from GroceryBuddy import GroceryApp
from DataStructure import ArrayList, LinkedList
from sys import argv

"""
  Note: here are a list of grocery you can buy:

  avocados
  bagel
  bananas
  beans
  candy
  celery
  danish
  eggs
  garlic
  grapes
  lemons
  lettuce
  limes
  onions
  pears
  peppers
  pizza
  scallions
  strawberries
  tomatos
  yams
"""

if __name__ == "__main__": # this line is to avoid running main() in case main.py is imported.
    args = argv[1:]
    if len(args) != 1:
        print("Usage: python main.py [0|1]\n\n\t0: use array list; 1: use linked list")
    else:
        l = ArrayList() if args[0] == "0" else LinkedList()
        g = GroceryApp(l)
        g.run()
