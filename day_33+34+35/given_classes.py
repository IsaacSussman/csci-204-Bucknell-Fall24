class Record :
    def __init__(self, plate, make, color, name, birthdate) :
        self.plate = plate
        self.make = make
        self.color = color
        self.name = name
        self.birthdate = birthdate
    
    def __str__(self):
        return f"""
Plate number    \t{self.plate}
Manufacturer    \t{self.make}
Color           \t{self.color}
Driver Name     \t{self.name}
Driver Birthdate\t{self.birthdate}
"""
    
def read_record(line : str) -> Record :
    """
    Turns a comma-separated record of a car and its driver into a Record object that contains this information.
    """
    fields = line.split(",")
    rec = Record(fields[0], fields[1], fields[2], fields[3], fields[4].strip())
    return rec

class BinaryNode :
    """
    A bare-bones binary tree class.
    """
    def __init__(self, data):
        """Initialize a binary tree node with given data. The left and right branches are set to None."""
        self.data = data
        self.left = None
        self.right = None

class Node :
    """
    A bare-bones node class.
    """
    def __init__(self, data):
        """
        Initialize a node with given data. 
        This class treats the node as a linked list.
        The next Node pointer is initially set to None.
        """
        self.data = data
        self.next = None
    
    def append(self, data) :
        """
        Append a record to the end of the linked list.
        """
        current_node = self
        while current_node.next != None :
            current_node = current_node.next
        
        current_node.next = Node(data)

    def delete(self, node) :
        current_node = self
        while current_node.next != node :
            # If there is no such node
            if current_node.next == None :
                return 
            
            current_node = current_node.next
        
        current_node.next = node.next
