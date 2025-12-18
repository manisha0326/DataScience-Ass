# 2. print a multiple table for a number, but highlight multiples of 5.

num = int(input("Enter a number: "))
print(f"Multiplication table of {num}: ")
for i in range(1,11):
    multi = num * i
    if multi % 5 == 0:
        print(f"{num} * {i} = *{multi}")
    else:
        print(f"{num} * {i} = {multi}")


'''
Output:
Enter a number:  6
Multiplication table of 6: 
6 * 1 = 6
6 * 2 = 12
6 * 3 = 18
6 * 4 = 24
6 * 5 = *30
6 * 6 = 36
6 * 7 = 42
6 * 8 = 48
6 * 9 = 54
6 * 10 = *60
'''
