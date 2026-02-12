import json

# =========================
# Student Class
# =========================
class Student:
    def __init__(self, roll, name, age, course):
        self.roll = roll
        self.name = name
        self.age = age
        self.course = course

    def to_dict(self):
        return {
            "roll": self.roll,
            "name": self.name,
            "age": self.age,
            "course": self.course
        }

# =========================
# Student Manager Class
# =========================
class StudentManager:
    def __init__(self, filename="students.json"):
        self.filename = filename
        self.students = []
        self.load_data()

    # Load from file
    def load_data(self):
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
                self.students = data
        except:
            self.students = []

    # Save to file
    def save_data(self):
        with open(self.filename, "w") as f:
            json.dump(self.students, f, indent=4)

    # Add student
    def add_student(self):
        roll = input("Enter roll: ")
        name = input("Enter name: ")
        age = input("Enter age: ")
        course = input("Enter course: ")

        student = Student(roll, name, age, course)
        self.students.append(student.to_dict())
        self.save_data()
        print("Student added successfully")

    # Display all
    def display_all(self):
        if not self.students:
            print("No students found")
            return

        for s in self.students:
            print(s)

    # Search
    def search_student(self):
        roll = input("Enter roll to search: ")
        for s in self.students:
            if s["roll"] == roll:
                print("Found:", s)
                return
        print("Student not found")

    # Update
    def update_student(self):
        roll = input("Enter roll to update: ")
        for s in self.students:
            if s["roll"] == roll:
                s["name"] = input("New name: ")
                s["age"] = input("New age: ")
                s["course"] = input("New course: ")
                self.save_data()
                print("Updated successfully")
                return
        print("Student not found")

    # Delete
    def delete_student(self):
        roll = input("Enter roll to delete: ")
        for s in self.students:
            if s["roll"] == roll:
                self.students.remove(s)
                self.save_data()
                print("Deleted successfully")
                return
        print("Student not found")

# =========================
# Menu
# =========================
manager = StudentManager()

while True:
    print("\n1.Add  2.Display  3.Search  4.Update  5.Delete  6.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        manager.add_student()
    elif choice == "2":
        manager.display_all()
    elif choice == "3":
        manager.search_student()
    elif choice == "4":
        manager.update_student()
    elif choice == "5":
        manager.delete_student()
    elif choice == "6":
        break
    else:
        print("Invalid choice")
