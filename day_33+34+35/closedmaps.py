from given_classes import *
import time

class ClosedMap :
    """
    TODO A Closed Map (a map that uses closed linear hashing) that contains a large number of license plates.
    Each plate is a sequence of three letters and four numbers "ABC 1234".
    Create your own hash function this time!
    Handle collisions using the suggested method.
    """
    def __init__(self, capacity, step = 8, coll_method = "linear") -> None:
        self.items = [None for _ in range(capacity)]
        self.capacity = capacity
        self.step = step
        self.coll_method = coll_method
        self.size = 0

    def hash(self, key : str) -> int :
        """
        TODO A custom hash function. (Or the one from before.)
        One suggestion is: get the ASCII codes % 24 of the first TWO letters from the license plate and then append those to the front of the last four digits. You will need to multiply one by 10^4 and the other by 10^6 to do this.
        """
        try :
            last_four = int(key.split(" ")[1])
            first_let = (ord(key[0]) % 26) * (10 ** 4)
            second_let = (ord(key[1]) % 26) * (10 ** 6)
            idx = (first_let + second_let + last_four) % self.capacity
        except :
            idx = 0

        return idx

    def put(self, incoming_record : Record) :
        """
        TODO Inserts the record with the given key.
        """
        h = hash(incoming_record.plate)
        count=0
        while not self.items[(h+count)%self.capacity] == None and not count > self.capacity:
            count+=self.step
        if count > self.capacity:
            raise OverflowError
        self.size+=1
        self.items[(h+count)%self.capacity] = incoming_record

    def get(self, key : str) :
        """
        TODO Returns the record with the given key.
        """


        h = hash(key)
        i = h
        count = 0
        while not (self.items[(h+count)%self.capacity] == None) and self.items[(h+count)%self.capacity].plate != key and count<self.capacity:
            count+=self.step
        if self.items[(h+count)%self.capacity] and self.items[(h+count)%self.capacity].plate == key:
            return self.items[(h+count)%self.capacity]
        else:
            return None

    def delete(self, key: str) :
        """
        BONUS Returns the record with the given key.
        """
        pass

    def __len__(self) :
        return self.size
    
# TODO You may need to edit the program below.
def create_closed_map(file) :
    """
    Creates an open map and populates it with records.
    Requires the put and get methods of the OpenMap class.
    """
    total = sum(1 for l in file)
    file.seek(0)
    loaded = 0

    max_hash = 10 ** 7

    database = ClosedMap(
        capacity = total + max_hash,  # TODO If you change the hash, then change this
        step = 3                      # TODO You will need to change this
    ) 

    while True :
        line = file.readline()
        if len(line) > 10 : 
            new_rec = read_record(line)

            start = time.time()
            database.put(new_rec)
            dur = time.time() - start

            # print(f"Loaded {new_rec.plate} in {dur:6.4f} ({round(100 * loaded/total, 2):6.2f}%)")
            loaded += 1
        else : 
            break

    return database
