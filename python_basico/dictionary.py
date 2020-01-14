grades = {}
grades['algorithms'] = 9
grades['maths'] = 10
grades['web'] = 8
grades['databases'] = 10

for key in grades:
    print(key)

for value in grades.values():
    print(value)

for key,value in grades.items():
    print('key {}, value {}'.format(key, value)) 

gpa = 0

for value in grades.values():
    gpa += value

gpa /=len(grades)

print(gpa)  