# use numpy and create 3d array with numbers fro 1 to 24 and reshape it intoshape (2,3,4)

# import numpy as np

# arr = np.arange(1, 25)

# arr_3d = arr.reshape(2, 3, 4)

# print("3D Array with shape (2, 3, 4):")
# print(arr_3d)
# print("Shape:", arr_3d.shape)

# indexing and accessing 

# print the firsg layer of the array

# print the element
# layer=1,row2 and column=3

# print first row of all layers 

# print the last row of all layers


# import numpy as np

# arr = np.arange(1, 25).reshape(2, 3, 4)

# print(arr[0])
# print(arr[1][2][3])
# print(arr[:, 0, :])
# print(arr[:, -1, :])

# boolean filtering 

# print all the elements whic are greater than 10

# count how many elements are even numbers

# replace all values less than 10 with 0


# import numpy as np

# arr = np.arange(1, 25).reshape(2, 3, 4)

# print(arr[arr > 10])

# print(np.sum(arr % 2 == 0))

# arr[arr < 10] = 0
# print(arr)


#marks of the students across multiple subjects and multiple exams. 
#analyse the performance using 3d numpy arrays

import numpy as np

marks = np.array([
    [[78, 82, 80], [65, 70, 68], [90, 92, 88], [72, 75, 74]],
    [[85, 88, 90], [72, 75, 78], [88, 86, 84], [80, 82, 85]],
    [[60, 62, 65], [55, 58, 60], [70, 72, 75], [68, 70, 72]],
    [[90, 92, 94], [85, 88, 87], [92, 94, 96], [88, 90, 89]],
    [[70, 72, 74], [65, 68, 67], [75, 78, 80], [72, 74, 76]]
])

print("Marks (Students × Subjects × Exams):")
print(marks)

student_avg = np.mean(marks, axis=(1, 2))
print("\nAverage marks of each student:")
print(student_avg)

subject_avg = np.mean(marks, axis=(0, 2))
print("\nAverage marks of each subject:")
print(subject_avg)

exam_avg = np.mean(marks, axis=(0, 1))
print("\nAverage marks of each exam:")
print(exam_avg)

print("\nStudents with average marks greater than 75:")
print(student_avg > 75)

top_student_index = np.argmax(student_avg)
print("\nTop scorer student index:")
print(top_student_index)

fail_exam=marks<60

print(fail_exam)

grace_marks=marks+5
grace_marks=np.clip(grace_marks,0,100)
print('grace marks: ', grace_marks)

#pass /fail status of students
status=np.where(student_avg >=80, 'Pass','fail')
print('student status ',status )
rank=np.argsort(student_avg)[::-1]
print('student ranks(best -> worst) ',rank ) 
#reshape for report
flat_data=marks.reshape(5,-1)
print('flat data for report: ',flat_data.shape)

#final report
print('original avg: ', student_avg)
print(' status ', status)