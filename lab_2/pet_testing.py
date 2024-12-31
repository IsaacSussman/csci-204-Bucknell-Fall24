'''CSCI 204 Lab 02 Class Design, Inheritance, and Exceptions
Lab section: CSCI 204.L62, Thursday 3-4:50
Student name(s): Isaac Sussman and Ethan Zeh
Instructor name: Samuel Gutekunst'''

from pet import *
import unittest

class TestPet(unittest.TestCase):
    def test_empty_init(self):
        """Tests the initialization of the class when only a name and a species are provided. Tests proper assignment of name, species, and defaults for age and activity"""
        mable = Pet("Mable", "Dog")
        self.assertEqual("Mable",mable._name, "Name improperly assigned")
        self.assertEqual("Dog", mable._species, "Species improperly assigned")
        self.assertEqual(Pet.UNKNOWN, mable._activity, "Activity should default to Pet.UNKNOWN if not assigned")
        self.assertEqual(mable._age, 0, "Age should default to 0 if not assigned")

    def test_init(self):
        """Tests the initialization of the class when all parameters are provided."""
        mable = Pet("Mable", "Dog", 42, Pet.EATING)
        self.assertEqual("Mable",mable._name, "Name improperly assigned")
        self.assertEqual("Dog", mable._species, "Species improperly assigned")
        self.assertEqual(Pet.EATING, mable._activity, "Activity improperly assigned")
        self.assertEqual(mable._age, 42, "Age improperly assigned")
    
    def test_Cat_age(self):
        """Tests that cat age starts at 0 and increments properly after a birthday."""
        kitty = Pet("Bamboo", "Cat")
        self.assertEqual(kitty._age, 0, "Cat age is not starting at 0")
        kitty.celebrate_birthday()
        self.assertTrue(kitty._age>0, "Cat age does not increment")
    
    def test_age(self):
        """Tests that dog age starts at 0 and increments properly after a birthday."""
        Doggy = Pet("DOG", "Dog")
        self.assertEqual(Doggy._age, 0, "Dog age is not starting at 0")
        self.assertEqual(Doggy.get_human_years(), 0, "Dog human age is not starting at 0")
        Doggy.celebrate_birthday()
        self.assertEqual(Doggy._age, 1, "Dog age is not incrementing to 1")
        self.assertEqual(Doggy.get_human_years(), 7, "Dog human age is not incrementing to 7")
    
    def test_species(self):
        Doggy = Pet("DOG", "Dog")
        kitty = Pet("CAT", "Cat")
        self.assertIn(Doggy._species, "Dog", "Species assigned improperly in Dogs")
        self.assertIn(kitty._species, "Cat", "Species assigned improperly in Cats") 


    def test_str(self):
        mable = Pet("Buddy", "Dog", 42, Pet.SLEEPING)
        self.assertEqual(str(mable), "Buddy (age: 42) is sleeping.", "__str__ is wrong")

    def test_activities(self):
        mable = Pet("Buddy", "Dog")
        self.assertEqual(mable._activity, Pet.UNKNOWN)
        mable.eat()
        self.assertEqual(mable._activity, Pet.EATING)
        mable.walk()
        self.assertEqual(mable._activity, Pet.WALKING)
        mable.sleep()
        self.assertEqual(mable._activity, Pet.SLEEPING)
        mable.make_noise()
        self.assertEqual(mable._activity, Pet.BARKING)
        mable  = Pet("Buddy", "Cat")
        self.assertEqual(mable._activity, Pet.UNKNOWN)
        mable.eat()
        self.assertEqual(mable._activity, Pet.EATING)
        mable.walk()
        self.assertEqual(mable._activity, Pet.WALKING)
        mable.sleep()
        self.assertEqual(mable._activity, Pet.SLEEPING)
        mable.make_noise()
        self.assertEqual(mable._activity, Pet.MEOWING)
    
    def test_human_age(self):
        mable  = Pet("Buddy", "Dog", 4)
        mable2  = Pet("Buddy", "Cat", 4)
        self.assertEqual(28, mable.get_human_years(), "Dog years not working (get_human_years)")
        self.assertEqual(32, mable2.get_human_years(),"Cat years not working (get_human_years)")
    
    def test_birthday(self):
        mable  = Pet("Buddy", "Cat")
        mable.celebrate_birthday()
        self.assertEqual(mable._age,1, "celebrate_birthday not incrementing properly")
    
    def test_bad_age(self):
        with self.assertRaises(AgeException, msg="Error is not raised for negative age"):
            myPet2 = Pet("Mickey", "Dog", age=-1)




unittest.main()