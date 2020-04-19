########################################################################################################################
# Task
# Given the names and grades for each student in a Physics class of N students, store them in a nested list
# and print the name(s) of any student(s) having the second lowest grade.
#
# Note: If there are multiple students with the same grade, order their names alphabetically
# and print each name on a new line.
########################################################################################################################

if __name__ == '__main__':

    students = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        students.append([])
        students[i] = [score, name]
    students.sort()
    # print(list(students))
    min = students[0][0]
    count = 0

    for i in range(len(students)):
        if min == students[i][0]:
            count += 1
    # print(count)
    for j in range(0, count):
        students.pop(0)
        # print(students)

    min = students[0][0]
    for i in range(len(students)):
        if min == students[i][0]:
            print(students[i][1])

