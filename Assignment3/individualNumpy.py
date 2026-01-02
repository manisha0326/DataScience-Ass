import numpy as np

# 20 data values
data = np.array([12, 7, 15, 10, 18, 20, 8])

# Quartiles
Q1 = np.percentile(data, 25)
Q2 = np.percentile(data, 50)  # Median
Q3 = np.percentile(data, 75)

IQR = Q3 - Q1

print("Q1:", Q1)
print("Q2 (Median):", Q2)
print("Q3:", Q3)
print("Interquartile Range:", IQR)
