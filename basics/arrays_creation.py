import numpy as np

# define a list of integers
data = [85, 84, 80 ,70]

# Create a numpy array from the list
array = np.array(data)

# Calculate the mean of the array using numpy mean function
mean = np.mean(array)

# Create an array of zeros with 5 elements
zeros = np.zeros(5)

# Create an array of 5 evenly spaced values between 0 and 10
line_space = np.linspace(0, 10, 5)
print("Line space:", line_space)
