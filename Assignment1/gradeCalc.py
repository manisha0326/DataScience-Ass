# 5. Build a sipel grade calculator for multiple students. Input their marks in a list and print the grade using a function.

def calculate_grade(mark):
    if mark >= 90:
        return "A+"
    elif mark >= 80:
        return "A"
    elif mark >= 70:
        return "B"
    elif mark >= 60:
        return "C"
    elif mark >= 50:
        return "D"
    else:
        return "F"

marks = input("Enter marks of students separated by space: ").split()

marks = [int(m) for m in marks]

for i, mark in enumerate(marks, start=1):
    grade = calculate_grade(mark)
    print(f"Student {i}: Marks = {mark}, Grade = {grade}")



'''
Output:
Enter marks of students separated by space:  90 68 87 50 25 98
Student 1: Marks = 90, Grade = A+
Student 2: Marks = 68, Grade = C
Student 3: Marks = 87, Grade = A
Student 4: Marks = 50, Grade = D
Student 5: Marks = 25, Grade = F
Student 6: Marks = 98, Grade = A+
'''