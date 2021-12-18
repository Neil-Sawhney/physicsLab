from sympy import *
print("x")
x = float(input()) * 10**(-3)
print("y")
y = float(input()) * 10**(-3)
print("D")
D = float(input()) * 10**(-2)
print("a")
a = float(input()) * 10**(-3)
print("p")
p = float(input())

ans = (sin(atan(((x+y)/2)/D))*a)/p
print(ans * 10**9)