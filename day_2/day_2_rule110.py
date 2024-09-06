'''
In-Class Exercise 2: Rule 110
Date: August 28, 2024

----------------------------------------------------------
Authors:
- Isaac
- Dipesh
----------------------------------------------------------


End Product: Program with a text-based UI that turns a sequence of 0s and 1s into automaton-generated ASCII art and saves your creation. 

See https://elife-asu.github.io/wss-modules/modules/1-1d-cellular-automata/ for what we're making.

Spec:
Part I
- Open the file "art_input.txt" and turn the first line into a list of 0s and 1s. Store that in focus_list.
- Calculate a new list from focus_list based on the following rules:
    focus_list |   0 0 0    1 0 0   0 1 0    1 1 0    0 0 1    1 0 0    0 1 0    1 1 1 
    apply_list |     1        0       0        1        0        0        0        1
  We treat out-of-bounds items as 0s. For example, 
    focus_list = [1, 0, 0, 1] 
  means that
    apply_list = [1, 1, 0, 1]
  * This is called "Rule 110", and defines what is called a "1-D Cellular Automaton".
- Write stringify(apply_list) to art_output.txt.
- Write a loop that repeats the procedure of calculating the next line generated by focus_list 30 times.
- Store the result in a string. This should create a 30 x 30 grid of text.
- Write that string into art_output.txt.
~~~BONUS~~~
- Allow the user to input their own names for the input and output text files so that the program doesn't always just read from "art_input.txt" and write to "art_output.txt". 
- Allow the user to start with a random string 0s and 1s instead of "art_input.txt".
- Try out other rules in the same format as Rule 110.
- Change the output symbols. Copy/paste these if you like (or Google to find your own): 
    ♥︎ ▲ ◈ ◯ ◳
'''

# Functions
## Cell Rule
def apply_cell_rule(cells) :
    ### Hint 1: Add a zero to either side of the input first
    print(cells)
    cells = [0] + cells + [0]
    print(cells)
    ### Hint 2: Initialize output list
    apply_list = []
    for i in range(1, len(cells)-1):
        slice = cells[i-1:]
        print(slice)
        if (slice[0] == 0 and slice[1] == 0) or (slice[0] == 1 and slice[1] == 1 and slice[2] == 1):
            apply_list.append(0)
        else:
            apply_list.append(1)
      
        

    ### Hint 3: Iterate through input_list and apply Rule 110 to each triplet of items, and append the result to the output string
    
    ### Now return the resulting list
    return apply_list
    ### ~

## Stringify
def stringify(item_list) :
    ret_string = ""
    for item in item_list :
        if item == 0 :
            ret_string = ret_string + "◈"
        elif item == 1 :
            ret_string = ret_string + "◳"
    
    return ret_string
    ### ~

# The Program
if __name__ == "__main__" :
  ## Introduction
  print('''
  ----------------------------------------------
  | Welcome to the Art Generator Device          |
  | Authors: Isaac and Dipesh                    |
  | Date:                                        |
  ----------------------------------------------
  ''', end="\n")
  file = ""
  f = open("C:\\Users\\isaac\\Documents\\GitHub\\csci-204-Bucknell-Fall24\\day_2\\art_input.txt", "r")
  file = f.readline()
  f.close()
  numstr = [int(c) for c in file.split()]
  numstr = apply_cell_rule(numstr)
  f = open("C:\\Users\\isaac\\Documents\\GitHub\\csci-204-Bucknell-Fall24\\day_2\\art_output.txt", "w",  encoding="UTF-8")
  for i in range(25):
    f.write(stringify(numstr)+"\n")
    numstr = apply_cell_rule(numstr)
  f.close()
  

  ## Main ##
