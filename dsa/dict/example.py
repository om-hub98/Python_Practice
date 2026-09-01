students = {
    "Alice": {"age": 20, "major": "Computer Science"},
    "Bob": {"age": 22, "major": "Mathematics"},
    "Charlie": {"age": 21, "major": "Physics"},
}

list_of_students = list(students.keys())
list_of_majors = [students[student]["major"] for student in list_of_students if students[student]["age"] > 20]


# for student in list_of_students:
#     if students[student]["age"] > 20:
#         list_of_majors.append(students[student]["major"])
        
#print(list_of_students)
#print(list_of_majors)

name = "Alice "

reversed_name = name[::-1]
print(reversed_name)

#for i in range(10, 0, -1):
   # print(i)