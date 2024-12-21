import numpy as np
data_type=[('name', 'S15'), ('class', int), ('height', float)]
students_details=[{'James', S, 48.5}, ('Nail', 6, 52.5),('Paul', S, 42.10), ('Pit', S, 40.11)]
students=np.array(students_details, data_type)
print("Original array: ")
print(students)
print("Sort by height")
print(np.sort(students, 'height'))