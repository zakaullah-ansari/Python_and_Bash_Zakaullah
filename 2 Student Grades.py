# 2. Student Grades

"""

Create a dictionary where the keys are student names and the values are their grades. Allow the user to:

7. Add a new student and grade.
8. Update an existing student's grade.
9. Print all student grades.
10. Use a dictionary and basic operations with if / else.

"""

def manage_student_grades():
    """Demonstrates dictionary operations for adding, updating, and viewing student grades."""

    # Initial student grades dictionary
    grades_dict = {
        "Aamir": "A",
        "Raj": "B",
        "Arzoo": "C"
    }

    # 1. Print initial grades
    print("Initial Student Grades:", grades_dict)

    # 2. Add a new student
    new_name = input("Enter a name to add new student: ")
    new_grade = input(f"Enter a grade for {new_name}: ")
    grades_dict[new_name] = new_grade
    print(f"Added {new_name} with grade {new_grade}.")

    # Print updated dictionary
    print("Updated Student Grades:", grades_dict)

    # 3. Update an existing student's grade
    target_student = input("Enter the existing student's name: ")
    updated_grade = input(f"Enter the updated grade for {target_student}: ")
    if target_student in grades_dict:
        grades_dict[target_student] = updated_grade
        print(f"Updated {target_student}'s grade to {updated_grade}.")

    # 4. Print all student grades cleanly
    print("\nFinal Student Grades Roster:")
    for student, grade in grades_dict.items():
        print(f"  - {student}: {grade}")

manage_student_grades()
