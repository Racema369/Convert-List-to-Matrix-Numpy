import numpy as np

a=[]
b=[]
while True:
    num1=int(input("Enter number for a: "))
    num2=int(input("Enter number for b: "))
    a.append(num1)
    b.append(num2)
    choice=input("Wanna Quit:Y/N :  ")
    if choice.upper()=="Y":
        break
print(a)
print(b)
matrix=np.column_stack((a,b))
print(matrix)
rmatrix=np.vstack((a,b))
print(rmatrix)
