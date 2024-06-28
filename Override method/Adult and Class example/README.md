## Adult and Child Class Example
# Overview
This Python script demonstrates the use of classes (Adult and Child) to represent individuals based on their age and determine if they can drive. It takes user inputs for name, age, hair colour, and eye colour, and creates an instance of either the Adult or Child class based on age.

# Classes Defined
Parent Class: Adult

Represents an adult with attributes name, age, hair_colour, and eye_colour.
Method can_drive(): Checks if the person is old enough to drive (age >= 18).
Child Class: Child (Inherits from Adult Class)

Represents a child, inheriting attributes and methods from the Adult class.
Overrides the can_drive() method to indicate that a child is too young to drive.
Usage
Input Requirements:

Prompts the user to enter:
Name
Age (must be an integer)
Hair colour
Eye colour
Instantiation:

Based on the entered age:
Creates an instance of Adult if age >= 18.
Creates an instance of Child if age < 18.
Driving Eligibility:

Calls the can_drive() method on the created instance to determine if the person can drive.
Exception Handling
Handles ValueError if the user inputs an invalid age (not an integer).
