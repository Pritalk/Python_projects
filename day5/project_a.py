'''
Find max from the given list without using inbuilt function.
'''

student_scores = [150, 142, 185, 203, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
#print(max(student_scores))

max_num = 0
for num in student_scores:
    if num > max_num:
        max_num = num
print(max_num)
