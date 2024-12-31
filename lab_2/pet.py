'''CSCI 204 Lab 02 Class Design, Inheritance, and Exceptions
Lab section: CSCI 204.L62, Thursday 3-4:50
Student name(s): Isaac Sussman and Ethan Zeh
Instructor name: Samuel Gutekunst'''


class AgeException(Exception):
    def __init__(self, message="age is not within acceptable range >:(") -> None:
        """Represents an Exception raised due to an age not being within an acceptable range.

        Args:
            message (str, optional): The message the exception contains. Defaults to "age is not within acceptable range >:(".
        """
        self.message = message
        super().__init__(self.message)

class Pet:
    """Base Class: Pet
    Encapsulates information about a pet

    Attributes:
        self._name (str): Contains the name of the pet
        self._age (int): Contains the age of the pet
        self._activity (int): Contains the current activity of the pet
        self._species (str): Contains the species of the pet

    Constants:
        Pet.UNKNOWN (int): Equals 0. Represents when the pet's activity is unknown.
        Pet.WALKING (int): Equals 1. Represents when the pet is walking.
        Pet.EATING (int): Equals 2. Represents when the pet is eating.
        Pet.SLEEPING (int): Equals 3. Represents when the pet is sleeping.
        Pet.BARKING (int): Equals 4. Represents when the pet is making noise and is a dog (barking).
        Pet.MEOWING (int): Equals 5. Represents when the pet is making noise and is a cat (meowing).

    Raises:
        AgeException: Raises AgeException if the Pet is initialized with a negative age
    """
    UNKNOWN = 0
    WALKING = 1
    EATING = 2
    SLEEPING = 3
    BARKING = 4
    MEOWING = 5

    def __init__(self, name, species, age = 0, activity = None) -> None:
        """Constructs a new Pet object from a name, a species, and optionally an age and activity.

        Args:
            name (str): the name of the constructed pet.
            species (str): the species of the constructed pet.
            age (int, optional): the age of the constructed pet. Defaults to 0.
            activity (int, optional): the current activity of the constructed pet. Defaults to Pet.UNKNOWN.

        Raises:
            AgeException: Raised when a negative `age` is inputted 
        """
        self._name = name
        if age < 0:
            raise AgeException
        self._age = age
        self._activity = activity if activity else Pet.UNKNOWN
        self._species = species
    
    def __str__(self):
        """Converts the Pet object to a string

        Returns:
            str: a string of the format "`_name` (age: `_age`) is `_activity`" where `_activity` is replaced by the name of the activity
        """
        l = ["doing UNKNOWN", "walking", "eating", "sleeping", "barking", "meowing"]
        return f"{self._name} (age: {self._age}) is {l[self._activity]}."
    
    def walk(self):
        """Sets the current `_activity` to `Pet.WALKING`"""
        self._activity = Pet.WALKING

    def eat(self):
        """Sets the current `_activity` to `Pet.EATING`"""
        self._activity = Pet.EATING
    
    def sleep(self):
        """Sets the current `_activity` to `Pet.SLEEPING`"""
        self._activity = Pet.SLEEPING
    
    def make_noise(self):
        """Sets the current `_activity` to `Pet.BARKING` if `_species` is "Dog" or `Pet.MEOWING` if `_species` is "Cat"."""
        if self._species.lower() == "cat":
            self._activity = Pet.MEOWING
        elif self._species.lower() == "dog":
            self._activity = Pet.BARKING
    
    def celebrate_birthday(self):
        """Increments `_age` by 1"""
        self._age += 1
    
    def get_human_years(self):
        """Converts the Pet object's `_age` into human years.

        Returns:
            int: If `_species` is "Dog", returns `_age` multiplied by 7 . Otherwise, if `_species` is "Cat", then returns 0 if `_age` is 0, 15 if `_age` is 1, 24 if `_age` is 2, and `(_age - 2) * 4 + 24` if `_age` is greater than 2.
        """
        if self._species.lower() == "cat":
            return (15 if self._age > 0 else 0) + (9 if self._age > 1 else 0) + (self._age - 2 if self._age > 2 else 0) * 4
        elif self._species.lower() == "dog":
            return self._age * 7
    


    
        