data = [12, 7, 15, 10, 18, 20, 8]

# Sort data
data.sort()
n = len(data)

# Quartile positions
Q1 = data[int((n+1)/4) - 1]
Q2 = data[int((n+1)/2) - 1]
Q3 = data[int(3*(n+1)/4) - 1]

IQR = Q3 - Q1

print("Q1:", Q1)
print("Q2 (Median):", Q2)
print("Q3:", Q3)
print("Interquartile Range:", IQR)
