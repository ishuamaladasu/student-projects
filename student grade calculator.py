def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "Fail"


def main():
    name = input("Enter student name: ")
    marks = float(input("Enter marks (0-100): "))

    if marks < 0 or marks > 100:
        print("Invalid marks entered")
        return

    grade = calculate_grade(marks)

    print("\n--- Student Grade Report ---")
    print("Name   :", name)
    print("Marks :", marks)
    print("Grade :", grade)


main()
