import numpy as np

t = np.linspace(0, 10, 100)
x = np.cos(t)
y = np.sin(t)
z = t/2

final = np.column_stack((x, y , z))

print(final.shape)  # Output: (100, 3)
print(final.ndim)   # Output: 2
print(final.size)   # Output: 300   
print(final.dtype)  # Output: float64
print(final.itemsize)  # Output: 8 (bytes per float64)