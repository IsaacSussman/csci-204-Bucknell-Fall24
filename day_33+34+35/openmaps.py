from given_classes import *

class OpenMap :
    """
    TODO An Open Map (a map that uses open hashing) that contains a large number of license plates.
    Each plate is a sequence of three letters and four numbers "ABC 1234".
    Handle collisions using open hashing.
    """
    def __init__(self, size = 10000 * 26) -> None:
        self.items = [None for _ in range(size)]
        self.size = 0

    def hash(self, key : str) -> int :
        """
        A hash map that takes the ascii code of the first character (modulo 26) and appends the last four numbers in the license plate to it. 
        """
        try :
            last_four = int(key.split(" ")[1])
            idx = (10 ** 4) * (ord(key[0]) % 26) + last_four
        except :
            idx = 0

        return idx

    def put(self, incoming_record : Record) :
        """
        TODO Adds a record to the open map that contains the incoming record. 
        """
        n = Node(incoming_record)
        h = self.hash(incoming_record.plate)
        if self.items[h] == None:
            self.items[h] = n
        else:
            self.items[h].append(incoming_record)
        self.size += 1

    def get(self, key : str) -> Record :
        """
        TODO Returns the record that corresponds to the given key. 
        """
        h = self.hash(key)
        if self.items[h] == None:
            return None
        else:
            c = self.items[h]
            while True:
                if c.data.plate == key:
                    return c.data
                elif c.next == None:
                    return None
                else:
                    c = c.next
    
    def delete(self, key : str) :
        """
        BONUS Deletes the record associated with a given key.
        """
        pass
            
    def __len__(self) :
        return self.size

# You do not need to edit the program below, but you do need to implement put
def create_open_map(file) :
    """
    Creates an open map and populates it with records.
    Requires the put and get methods of the OpenMap class.
    """
    total = sum(1 for l in file)
    file.seek(0)
    loaded = 0

    database = OpenMap()

    while True :
        line = file.readline()
        if len(line) > 10 : 
            new_rec = read_record(line)
            database.put(new_rec)

            print(f"Loaded {round(100 * loaded/total, 2):6.2f}%")
            loaded += 1
        else : 
            break

    return database