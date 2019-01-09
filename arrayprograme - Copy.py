import numpy as np 
height = [1.73, 1.68, 1.71, 1.89, 1.79]
weight = [65.4, 99.9, 45.67, 67.8, 78.56]
np_height = np.array(height)
np_weight = np.array(weight)
bmi = np_weight/np_height**2
print(bmi)
print(type(bmi))
np_height_m = np_height*0.0254
print(np_height_m)
np_weight_kg = np_weight*0.453592
print(np_weight_kg)
bmichanged = np_weight_kg/np_height_m**2
print(bmichanged)
np_height_n = np.array(height)*0.0254
print(np_height_n)
np_2d = ([[1.71, 1.99, 1.45, 1.33],
	    [65.43, 34.55, 67.44, 78.43]])
print(np_2d)
print(type(np_2d))
print(np_2d[1])
print(np_2d[0][2])
print(np_2d[1][1:3])
print(np_2d[0:2])
meen = np.mean(np_2d[:][0])
print(meen)
meedian = np.median(np_2d[:][1])
print(meedian)
print(np.std(np_2d[:][1]))
