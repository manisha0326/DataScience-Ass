# 1. wap that asks for three numbers and prints the largest using a function.

a = int(input("Enter 1st integer number"))
b = int(input("Enter 2nd integer number"))
c = int(input("Enter 3rd integer number"))

def largest(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=c and b>=a:
        return b
    else:
        return c

print(largest(a,b,c))



'''
Output:
Enter 1st integer number 3
Enter 2nd integer number 4
Enter 3rd integer number -4
4
'''



# def largest(arr):
#     max_num = arr[0]
#     for a in arr[1:]:
#         if a>max_num:
#             max_num = a
#     return max_num

# largest([1,2,5,-8,0,4,5])