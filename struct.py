from dataclasses import dataclass # C Program of struct in Python

@dataclass
class Student:
    name: str
    roll: int
    marks: float

# Create an instance and assign values
s1 = Student(name="Rahul", roll=101, marks=87.5)

# Print the values
print(f"Name: {s1.name}")
print(f"Roll: {s1.roll}")
print(f"Marks: {s1.marks:.1f}")