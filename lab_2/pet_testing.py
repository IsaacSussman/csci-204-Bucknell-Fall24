from pet import *
import unittest

class TestPet(unittest.TestCase):
    def test_empty_init(self):
        mable = Pet("Mable", "dog")
        self.assertEqual("Mable",mable._name, "Name improperly assigned")
        self.assertEqual("dog", mable._species, "Species improperly assigned")
        self.assertEqual(Pet.UNKNOWN, mable._activity, "Activity should default to Pet.UNKNOWN if not assigned")
        self.assertEqual(mable._age, 0, "Age should default to 0 if not assigned")

    def test_init(self):
        mable = Pet("Mable", "dog", 42, Pet.EATING)
        self.assertEqual("Mable",mable._name, "Name improperly assigned")
        self.assertEqual("dog", mable._species, "Species improperly assigned")
        self.assertEqual(Pet.EATING, mable._activity, "Activity improperly assigned")
        self.assertEqual(mable._age, 42, "Age improperly assigned")
    
    def test_str(self):
        mable = Pet("Buddy", "dog", 42, Pet.SLEEPING)
        self.assertEqual(str(mable), "Buddy (age: 42) is sleeping.", "__str__ is wrong")

    def test_activities(self):
        mable = Pet("Buddy", "dog")
        mable.eat()
        self.assertEqual(mable._activity, Pet.EATING)
        mable.walk()
        self.assertEqual(mable._activity, Pet.WALKING)
        mable.sleep()
        self.assertEqual(mable._activity, Pet.SLEEPING)
        mable.make_noise()
        self.assertEqual(mable._activity, Pet.BARKING)
        mable  = Pet("Buddy", "cat")
        mable.make_noise()
        self.assertEqual(mable._activity, Pet.MEOWING)
    
    def test_human_age(self):
        mable  = Pet("Buddy", "dog", 4)
        mable2  = Pet("Buddy", "cat", 4)
        self.assertEqual(28, mable.get_human_years(), "dog years not working (get_human_years)")
        self.assertEqual(32, mable2.get_human_years(),"cat years not working (get_human_years)")
    
    def test_birthday(self):
        mable  = Pet("Buddy", "cat")
        mable.celebrate_birthday()
        self.assertEqual(mable._age,1, "celebrate_birthday not incrementing properly")
    
    def test_age_validator(self):
        myPet2 = Pet("Mickey", "dog", age=1)
        with self.assertRaises(AgeException, msg="Error is not raised for negative age"):
            myPet2 = Pet("Mickey", "dog", age=-1)




unittest.main()