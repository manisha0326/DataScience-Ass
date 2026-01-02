import numpy as np

values = np.array([5, 10, 15, 20, 25, 30, 35])
freq = np.array([2, 4, 6, 8, 6, 4, 2])

# Expand data
data = np.repeat(values, freq)

Q1 = np.percentile(data, 25)
Q2 = np.percentile(data, 50)
Q3 = np.percentile(data, 75)

IQR = Q3 - Q1

print("Q1:", Q1)
print("Q2 (Median):", Q2)
print("Q3:", Q3)
print("Interquartile Range:", IQR)
