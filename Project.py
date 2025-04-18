class Student:
    def __init__(self, name, marks):
        self.name = name
        self.original_marks = marks
        self.updated_marks = marks
        self.original_rank = None
        self.updated_rank = None

    def update_marks(self, increment):
        self.updated_marks += increment


class StudentRankManager:
    def __init__(self):
        self.students = []

    def add_student(self, name, marks):
        student = Student(name, marks)
        self.students.append(student)

    def update_all_marks(self, updates):
        for student, increment in zip(self.students, updates):
            student.update_marks(increment)

    def assign_original_ranks(self):
        sorted_students = sorted(self.students, key=lambda s: s.original_marks, reverse=True)
        for idx, student in enumerate(sorted_students):
            student.original_rank = idx + 1

    def assign_updated_ranks(self):
        sorted_students = sorted(self.students, key=lambda s: s.updated_marks, reverse=True)
        for idx, student in enumerate(sorted_students):
            student.updated_rank = idx + 1

    def find_topper(self):
        return max(self.students, key=lambda s: s.updated_marks)

    def show_all_students(self):
        print(f"\n{'Name':<15}{'Original Marks':<17}{'Updated Marks':<17}{'Original Rank':<17}{'Updated Rank':<15}")
        print("-" * 80)
        for student in self.students:
            print(f"{student.name:<15}{student.original_marks:<17}{student.updated_marks:<17}"
                  f"{student.original_rank:<17}{student.updated_rank:<15}")


def main():
    manager = StudentRankManager()

    n = int(input("Enter number of students: "))

    # Input student names and marks
    print("\n--- Enter Student Details ---")
    for i in range(n):
        name = input(f"Enter name of student {i+1}: ")
        while True:
            try:
                marks = int(input(f"Enter marks of {name} (out of 10): "))
                if 0 <= marks <= 10:
                    break
                else:
                    print("Marks should be between 0 and 10.")
            except ValueError:
                print("Invalid input. Please enter an integer.")
        manager.add_student(name, marks)

    # Input updates
    print("\n--- Enter Mark Updates ---")
    updates = []
    for student in manager.students:
        while True:
            try:
                inc = int(input(f"Enter increment marks for {student.name}: "))
                updates.append(inc)
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")

    # Assign and display results
    manager.assign_original_ranks()
    manager.update_all_marks(updates)
    manager.assign_updated_ranks()

    print("\n--- Student Rank Details ---")
    manager.show_all_students()

    # Show Topper
    topper = manager.find_topper()
    print("\n--- Topper After Update ---")
    print(f"Name: {topper.name}")
    print(f"Marks Before Update: {topper.original_marks}")
    print(f"Marks After Update: {topper.updated_marks}")
    print(f"Rank Before Update: {topper.original_rank}")
    print(f"Rank After Update: {topper.updated_rank}")
    print(f"Rank Improvement: {topper.original_rank - topper.updated_rank} places")


if __name__ == "__main__":
    main()
