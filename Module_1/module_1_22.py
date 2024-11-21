grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

grades = [sum(grade_set)/len(grade_set) for grade_set in grades]
students = sorted(list(students))

journal = {students[i]:grades[i] for i in range(len(students))}

print(journal)


