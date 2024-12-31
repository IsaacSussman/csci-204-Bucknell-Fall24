'''

Project 1: Cave Cartographer


Legend for the Text file: 

-----------------------------------------------------------------------------------------------

Symbol    Meaning     Can you walk through it?     Console

-----------------------------------------------------------------------------------------------

R         Rock        No                           N/A                                           

_         Empty       Yes                          None                                          

S         Start       Yes                          "Entrance to the cave."                          

E         End           Yes                          End the game if the cave has been explored.

-----------------------------------------------------------------------------------------------


What you have to do:

    Any comment of the form 

    TODO: Here is a task for you to do 

    indicates that there is something you have to do there. Use Ctrl/Cmd+F to find all the tasks you have to do.

'''


import os


# Classes

class Cave :

    """

    Cave Class

    This contains information about the entirety of the cave. Needs to be passed a text file.

    """

    def __init__(self, file) :

        self.cave_file = file           # (string) file name containing 

        self.layout = [["S"], ["E"]]    # (2D list of str) default cave

        self.width  = 1                 # (int) default width

        self.height = 2                 # (int) default height

        self.starting_spot = [0, 0]     # (list of int) default starting position


    def create_cave(self) :

        """

        Creates a cave from the input text file. 

        """

        with open(self.cave_file) as file:

            c = file.readlines()

        for i in range(len(c)):

            c[i] = c[i].strip("\n").split(" ")


        check_rect_num = len(c[0])

        self.width = check_rect_num

        self.height = len(c)

        self.layout = c.copy()

        start_flag = False

        end_flag = False

        for i in range(len(c)):

            if len(c[i]) != check_rect_num:

                raise Exception("Cave is not rectangular")

            if (c[i][0] != "R") or (c[i][-1] != "R"):

               raise Exception("Cave is not surrounded by R")

            for j in range(check_rect_num):

                if c[i][j] == "E":

                    if end_flag:

                        raise Exception("Multiple exits")

                    else:

                        end_flag = True

                if c[i][j] == "S":

                    if start_flag:

                        raise Exception("Multiple entrances")

                    else:

                        start_flag = True

                        self.starting_spot = [i, j]


        for i in range(check_rect_num):

            if (c[0][i] != "R") or (c[-1][i] != "R"):

               print(c)

               raise Exception("Cave is not surrounded by Rocks")

        

        


        


    def get_starting_spot(self) :

        """Returns starting spot in cave."""

        return self.starting_spot


    def get_height(self) :

        """Returns height of underlying cave layout."""

        return self.height

    

    def get_width(self) :

        """Returns width of underlying cave layout."""

        return self.width


    def get_layout(self) :

        """Returns underlying cave layout."""

        return self.layout


    def __str__(self) :

        """

        Create full map of underlying cave layout and return as a string. 

        """

        s = ""

        for i in self.layout:

            for j in i:

                if j == "R":

                    s+="█"

                elif j == "_":

                    s+="░"

                elif j == "E":

                    s+="⍈"

                elif j == "S":

                    s+="◊"

                else:

                    s+="!"

            s+="\n"

        return s


class Adventure :

    """

    Adventure Class

    This contains all of the information about the current state of the adventure. Needs to be passed a Cave object. Has a DEFAULT_CAVE constant pointing to a default cave file.

    """


    DEFAULT_CAVE = "default_cave.txt"


    def __init__(self, cave:Cave) -> None:

        self.cave = cave                # adventure's cave is cave passed

        self.visited = [[1], [1]]       # at start, only visited square is (1,1) by default (changed in start_adventure())

        self.current_spot = [0, 0]      # current_spot in default cave begins at (0,0) by default (changed in start_adventure())


    def start_adventure(self) :

        """

        Creates the adventure out of the cave passed to it in the init method.

        1. TODO It creates the adventure's cave object. If it encounters an Exception, it proceeds to start the adventure with the default cave (make sure you have a valid default_cave.txt in the folder).

        2. TODO It retrieves the starting coordinates for the given cave object.

        3. It initializes the visited portion of the cave by illuminating the immediate surroundings of starting spot.

        """

        try:

            self.cave.create_cave()

        except:

            self.cave = Cave("default_cave.txt")

            self.cave.create_cave()


        self.current_spot = self.cave.starting_spot


        self.visited = []

        for i in range(self.cave.get_height()):

            self.visited.append([])

            for j in range(self.cave.get_width()):

                self.visited[i].append(0)

        self.set_visited()

        

        print(self.get_current_map())


    def get_current_map(self) :

        """

        Returns a map of the portion of the cave that has been visited so far.

        (Not part of Part 2.)

        """

        c = str(self.cave).split("\n")

        for i in range(len(c)):

            c[i] = list(c[i])

        new_string = ""

        for i in range(len(c)):

            for j in range(len(c[i])):

                if self.current_spot == [i, j]:

                    new_string+= "\x1b[37;41m"

                if self.visited[i][j] == 0:

                    new_string+="?"

                else:

                    new_string+=c[i][j]

                new_string+="\x1b[0m"

            new_string+="\n"

        return new_string


    def get_current_spot(self) :

        """

        Returns the coordinates of the current spot the cartographer is inhabiting.

        (Not part of Part 2.)

        """

        return self.cave.layout[self.current_spot[0]][self.current_spot[1]]

    

    def set_visited(self) :

        """

        Updates the area that the cartographer has visited using the current spot.

        (Not part of Part 2.) 

        """



        self.visited[self.current_spot[0]][self.current_spot[1]] = 1

        self.visited[max(self.current_spot[0]-1, 0)][self.current_spot[1]] = 1

        self.visited[min(self.current_spot[0]+1, self.cave.get_width()-1)][self.current_spot[1]] = 1

        self.visited[self.current_spot[0]][max(self.current_spot[1]-1,0)] = 1

        self.visited[self.current_spot[0]][min(self.current_spot[1]+1,self.cave.get_width()-1)] = 1

        self.visited[max(self.current_spot[0]-1, 0)][min(self.current_spot[1]+1,self.cave.get_width()-1)] = 1

        self.visited[min(self.current_spot[0]+1, self.cave.get_width()-1)][min(self.current_spot[1]+1,self.cave.get_width()-1)] = 1

        self.visited[max(self.current_spot[0]-1, 0)][max(self.current_spot[1]-1,0)] = 1

        self.visited[min(self.current_spot[0]+1, self.cave.get_width()-1)][max(self.current_spot[1]-1,0)] = 1


    def can_move(self, direction) :

        """

        Returns True if cartographer can move in given direction and False otherwise.

        (Not part of Part 2.)

        """

        dirmap = {"right":(0, 1), "left":(0, -1), "up":(-1, 0), "down":(1, 0)}

        return self.cave.get_layout()[self.current_spot[0]+dirmap[direction][0]][self.current_spot[1]+dirmap[direction][1]] != "R"

    

    def move(self, direction) :

        """

        Moves cartographer in given direction and updates the area visited.

        (Not part of Part 2.)

        """

        dirmap = {"right":(0, 1), "left":(0, -1), "up":(-1, 0), "down":(1, 0)}

        self.current_spot = [self.current_spot[0]+dirmap[direction][0], self.current_spot[1]+dirmap[direction][1]]
        


    def map_complete(self) :

        """

        Returns True if the map has been completely explored.

        (Not part of Part 2.)

        """

        for i in self.visited:

            for j in i:

                if j == 0:

                    return False

        if self.cave.layout[self.current_spot[0]][self.current_spot[1]] != "E":

            return False

        return True


# Other functions

def clear_screen() :

    """Clears the text in the console."""

    print("\n" * 1000)


def print_banner() :

    """Prints the welcome banner for the adventure."""


    print("""

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

~~~~ You are in a cave! ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Explore the cave by typing in commands. You can only exit the cave if the entire

cave has been explored. Good luck!

          """)


# ~ MAIN ~ #

if __name__ == "__main__" :

    # Let's Go 

    ## Begin the Adventure

    print_banner()

    input("Press Enter to start.")

    c = Cave("cave.txt")


    a = Adventure(c)

    a.start_adventure()

    print(a.get_current_map())

    i = input("Enter a direction or Q to quit: ").lower()

    while i != "q" and not a.map_complete():

        if i not in ("right", "left", "up", "down", "q"):

            print("INVALID INPUT!")

        else:

            if a.can_move(i):

                a.move(i)

                a.set_visited()

            else:

                print("Bad Move")

        print(a.get_current_map())

        if a.map_complete():

            break

        i = input("Enter a direction or Q to quit: ").lower()

    

    if a.map_complete():

        print('Winner Winner!')

        

    

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")