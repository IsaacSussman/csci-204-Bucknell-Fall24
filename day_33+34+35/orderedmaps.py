from given_classes import *

class OrderedMap :
    """
    TODO An Ordered Map that contains a large number of license plates.
    """

    def __init__(self) -> None:
        self.root = None
        self.size = 0

    def put(self, incoming_record : Record) :
        """
        TODO Adds a binary tree node to the ordered map that contains the incoming record. 
        """
        if self.root == None:
            self.root = BinaryNode(incoming_record)
            return
        pick = self.root
        self.size += 1
        while True:
            if incoming_record.plate <= pick.data.plate:
                if pick.left:
                    pick = pick.left
                else:
                    pick.left = BinaryNode(incoming_record)
                    return
            elif incoming_record.plate > pick.data.plate:
                if pick.right:
                    pick = pick.right
                else:
                    pick.right = BinaryNode(incoming_record)
                    return
                

            
    
    def get(self, key : str) -> Record :
        """
        TODO Retrieves a record that matches the given key.
        """
        if self.root == None:
            return None
        pick = self.root
        while True:
            if key == pick.data.plate:
                return pick.data
            elif key < pick.data.plate:
                if pick.left:
                    pick = pick.left
                else:
                    return None
            elif key > pick.data.plate:
                if pick.right:
                    pick = pick.right
                else:
                    return None
    
    def __len__(self) :
        return self.size


# You do not need to edit the program below, but you do need to implement put
def create_ordered_map(file) :
    """
    TODO Creates an ordered map and populates it with records.
    Requires the put and get methods of the OrderedMap class.
    """
    database = OrderedMap()

    while True :
        line = file.readline()
        if len(line) > 10 : 
            new_rec = read_record(line)
            database.put(new_rec)
        else : 
            break

    return database