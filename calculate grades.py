exam1_grade = float(input('Enter score on Exam 1 (out of 50):\n'))
exam2_grade = float(input('Enter score on Exam 2 (out of 50):\n'))
exam3_grade = float(input('Enter score on Exam 3 (out of 50):\n'))
exam4_grade = float(input('Enter score on Exam 3 (out of 50):\n'))

weighted_grade1 = exam1_grade / 50
weighted_grade2 = exam2_grade / 50
weighted_grade3 = exam3_grade / 50
weighted_grade4 = exam4_grade / 50

average_exam_score_perc = (weighted_grade1 + weighted_grade2 + weighted_grade3 + weighted_grade4) / 4
avg_exam_score = average_exam_score_perc * 100

input()

print(f'Your overall grade is: {avg_exam_score}')

weighted_grade1 = exam1_grade / 50
weighted_grade2 = exam2_grade / 50
weighted_grade3 = exam3_grade / 75
weighted_grade4 = exam4_grade / 75

average_exam_score_perc2 = (weighted_grade1 + weighted_grade2 + weighted_grade3 + weighted_grade4) / 4
avg_exam_score2 = average_exam_score_perc2 * 100

print(f'Your overall grade is: {avg_exam_score2}')

input()

exam5_grade = float(input('Enter score on Exam 1 (out of 100):\n'))
exam6_grade = float(input('Enter score on Exam 2 (out of 100):\n'))
exam7_grade = float(input('Enter score on Exam 3 (out of 100):\n'))

assignment1_grade = float(input('Enter score on Assignment 1(out of 50):\n'))
assignment2_grade = float(input('Enter score on Assignment 2(out of 50):\n'))
assignment3_grade = float(input('Enter score on Assignment 3(out of 50):\n'))
assignment4_grade = float(input('Enter score on Assignment 4(out of 50):\n'))

avgerage_exam_scores3 = (exam5_grade + exam6_grade + exam7_grade) / 3
assignment1_grade = assignment1_grade / 50
assignment2_grade = assignment2_grade / 50
assignment3_grade = assignment3_grade / 50
assignment4_grade = assignment4_grade / 50
average_exam_score_perc3 = (assignment1_grade + assignment2_grade + assignment3_grade + assignment4_grade) / 4
avg_assignment_score = average_exam_score_perc3 * 100

overall_grade = (0.6 * avgerage_exam_scores3) + (0.4 * avg_assignment_score)
print(f'Your overall grade is: {overall_grade}')
