values = [5, 10, 15, 20, 25, 30, 35]
freq = [2, 4, 6, 8, 6, 4, 2]

data = []

for i in range(len(values)):
    for j in range(freq[i]):
        data.append(values[i])

data.sort()
n = len(data)

Q1 = data[int((n+1)/4) - 1]
Q2 = data[int((n+1)/2) - 1]
Q3 = data[int(3*(n+1)/4) - 1]

IQR = Q3 - Q1

print("Q1:", Q1)
print("Q2 (Median):", Q2)
print("Q3:", Q3)
print("Interquartile Range:", IQR)
