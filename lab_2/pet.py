'''CSCI 204 Lab 02 Class Design, Inheritance, and Exceptions
Lab section: CSCI 204.L62, Thursday 3-4:50
Student name(s): Isaac Sussman
Instructor name:  Samuel Gutekunst'''

class AgeException(Exception):
    def __init__(self, message="age is not within acceptable range >:(") -> None:
        self.message = message
        super().__init__(self.message)

class Pet:
    """Base Class: Pet
    Encapsulates information about a pet

    Attributes:
        self._name
        self._age
        self._activity
        self._species

    Raises:
        AgeException: _description_
    """
    UNKNOWN = 0
    WALKING = 1
    EATING = 2
    SLEEPING = 3
    BARKING = 4
    MEOWING = 5

    def __init__(self, name, species, age = 0, activity = None) -> None:
        """_summary_

        Args:
            name (_type_): _description_
            species (_type_): _description_
            age (int, optional): _description_. Defaults to 0.
            activity (_type_, optional): _description_. Defaults to None.

        Raises:
            AgeException: _description_
        """
        self._name = name
        if age < 0:
            raise AgeException
        self._age = age
        self._activity = activity if activity else Pet.UNKNOWN
        self._species = species
    
    def __str__(self):
        l = ["doing UNKNOWN", "walking", "eating", "sleeping", "barking", "meowing"]
        return f"{self._name} (age: {self._age}) is {l[self._activity]}."
    
    def walk(self):
        self._activity = Pet.WALKING

    def eat(self):
        self._activity = Pet.EATING
    
    def sleep(self):
        self._activity = Pet.SLEEPING
    
    def make_noise(self):
        if self._species.lower() == "cat":
            self._activity = Pet.MEOWING
        elif self._species.lower() == "dog":
            self._activity = Pet.BARKING
    
    def celebrate_birthday(self):
        self._age += 1
    
    def get_human_years(self):
        if self._species.lower() == "cat":
            return (15 if self._age > 0 else 0) + (9 if self._age > 1 else 0) + (self._age - 2 if self._age > 2 else 0) * 4
        elif self._species.lower() == "dog":
            return self._age * 7
    


    
        