grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list(students)
students.sort(key=str.lower)
average_score_Aaron = sum(grades[0])/len(grades[0])
average_score_Bilbo = sum(grades[1])/len(grades[1])
average_score_Johnny = sum(grades[2])/len(grades[2])
average_score_Khendrik = sum(grades[3])/len(grades[3])
average_score_Steve = sum(grades[4])/len(grades[4])

class_diary = {students[0]: average_score_Aaron, students[1]: average_score_Bilbo, students[2]: average_score_Johnny, students[3]: average_score_Khendrik, students[4]: average_score_Steve}

print(class_diary)