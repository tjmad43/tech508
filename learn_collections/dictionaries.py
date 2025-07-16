# Working with dictionaries

student_1 = {"name":"susan",
             "stream":"tech",
             "completed_lessons":4,
             "completed_lesson_names":["variables","data_types","set up"]
             }
# A dictionary saves data as a key:value pair
print(student_1)
print(type(student_1))

# print value by giving key
print(student_1["stream"])
print(student_1["completed_lesson_names"])
print(type(student_1["completed_lesson_names"]))
print(student_1["completed_lesson_names"][0])

# change the value of a key
student_1["completed_lessons"] = 3
print(student_1)

# delete a value from list within dictionary
student_1["completed_lesson_names"].remove("data_types")
print(student_1)

# print dictionary keys
print(student_1.keys())