# Task 1
student_marks = {'Mike': 56, 'Alice': 78,
                 'Charlie': 81, 'Diana': 65, 'jon': 88}

student_name = input("Enter the student's name: ")

if student_name in student_marks:
    print("{}'s marks: {}".format(student_name, student_marks[student_name]))
else:
    print("No record found for student: {}".format(student_name))


# Task 2
numbers = list(range(1, 11))

first_five = numbers[0:5]

reverse = first_five[::-1]

print("First five elements:", first_five)
print("Reversed first five elements:", reverse)
