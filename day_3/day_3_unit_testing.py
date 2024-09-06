'''
In-Class Exercise 3: Course Logistics
Date: August 30, 2024

* Make sure you submit this file as "day_3_unit_testing.py"

----------------------------------------------------------
Authors:
- Isaac
- Ethan
- Alexey
----------------------------------------------------------

End Product: This file performs unit tests on the Course class.

'''

from day_3_course_logistics import *
import unittest

class TestCourse(unittest.TestCase):
    def test_is_empty(self):
        test_course = Course("Silly Billies 101", 1)
        self.assertTrue(test_course.is_empty(), "Course is not created empty")
    
    def test_is_empty(self):
        test_course = Course("Silly Billies 101", 1)
        self.assertFalse(test_course.is_full(), "Course is full")

    def test_is_enrolling(self):
        test_course = Course("Silly Billies 101", 1)
        s = Student("A",'B', 3,'D')
        s2 = Student("8734",'B', 3,'D')
        test_course.enroll_student(s)
        self.assertTrue(test_course.is_enrolled(s), "Student is not enrolled")
        with self.assertRaises(Exception):
            test_course.enroll_student(s)
        test_course.enroll_student(s2)
        self.assertTrue(s2 in test_course.waitlist, "Waitlist is not taking overflow")
    
    def test_is_dropping(self):
        test_course = Course("Silly Billies 101", 1)
        s = Student("A",'B', 3,'D')
        s2 = Student("8734",'B', 3,'D')
        test_course.enroll_student(s)
        test_course.enroll_student(s2)
        test_course.drop(s)
        self.assertTrue(test_course.is_enrolled(s2))

        
    
    def test_init(self):
        test_course = Course("Silly Billies 101", 1)
        self.assertEqual(test_course.capacity, 1, "Capacity is improperly assigned")
        self.assertEqual(len(test_course.roster), 0, "Roster is improperly generated")
        self.assertEqual(len(test_course.waitlist), 0, "Waitlist is improperly generated")
        self.assertEqual(test_course.name, "Silly Billies 101", "Name is improperly assigned")
    
    def test_drop(self):
        pass

    

unittest.main()