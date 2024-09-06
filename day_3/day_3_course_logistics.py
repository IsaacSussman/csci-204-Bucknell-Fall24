'''
In-Class Exercise 3: Course Logistics
Date: August 30, 2024

* Make sure you submit this file as "day_3_course_logistics.py"

----------------------------------------------------------
Authors:
- Isaac
- Ethan
- Alexey
----------------------------------------------------------

End Product: This file contains Course and Student classes capturing the logistical structure of a college course.
'''

class Student:
    def __init__(self, first_name: str, last_name: str, grad_year: int, major: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.grad_year = grad_year
        self.major = major
    
    def __eq__(self, value: object) -> bool:
        # Credit: https://stackoverflow.com/a/1227325
        if not isinstance(value, Student):
            return NotImplemented
        return self.first_name == value.first_name and self.last_name == value.last_name and self.grad_year == value.grad_year and self.major == value.major 

class Course:
    def __init__(self, name: str, capacity: int) -> None:
        self.name = name
        self.capacity = capacity
        self.roster = []
        self.waitlist = []
    
    def is_full(self) -> bool:
        return len(self.roster) >= self.capacity
    
    def is_empty(self) -> bool:
        return len(self.roster) == 0
    
    def is_enrolled(self, student: Student) -> bool:
        for i in self.roster:
            if i == student:
                return True
        return False

    def enroll_student(self, student: Student):
        if (self.is_enrolled(student)):
            raise Exception("Student is already enrolled")
        elif self.is_full():
            self.waitlist.append(student)
        elif not self.is_enrolled(student):
            self.roster.append(student)
            
    
    def drop(self, student: Student):
        self.roster.remove(student)
        if self.waitlist != []:
            self.roster.append(self.waitlist.pop(0))

