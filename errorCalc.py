
import math as math
import sympy as sy
from numpy import *

#constants
g = 9.80665
G = 6.67 * 10**-11

def ref():
    print("-------------\n\n")
    print("vf = v0 + a*t")
    print("xf = x0 + v0*t + (1/2)a*t^2")
    print("vf^2 = v0^2 + 2a(xf - x0)\n")

def kmPerHrToMPerS(km):
    m = (km*1000)/60**2
    return(m)
def mPerSToKmPerH(m):
    km = (m/1000)*60**2
    return(km)
def mPerSToFtPerS(m):
    ft = m*3.28084
    return(ft)
def miPerHrToFtPerS(mi):
    ft = (mi*5280)/60**2
    return(ft)

def mToFt(m):
   return(m * 3.280839895)

def ftToM(m):
   return(m / 3.280839895)

def arrToDegrees(arr):
    new = [0] * len(arr)
    for x in range(len(arr)):
        new[x] = math.degrees(arr[x])
    return new
def unit(arr): 
    temp = 0
    for x in arr:
        temp = temp + x**2
    return arr/sy.sqrt(temp)
def magnitude(arr):
    temp = 0
    for x in arr:
        temp = temp + x**2
    return sy.sqrt(temp)
def angle(arr):
    return degrees(math.atan(arr[1]/arr[0]))

#----------------------

d, t = sy.symbols('d t')
n = sy.sqrt(d**2 + 16*t**2)/d

nAns = n.subs({d:6.213, t:2.202})
print('n =: ',nAns)
deltad = 0.710
deltat = 0.015
deltan = sy.sqrt((n.diff(d)*deltad)**2 + (n.diff(t)*deltat)**2)
deltanAns = deltan.subs({d:6.214, t:2.202})
print('deltan =: ',deltanAns)

print('#---------------------------')
d, t, g = sy.symbols('d t g')
n = g*d/sy.sqrt(d**2 + 16*t**2)

print('n =: ',n.subs({d:17.41, t:2.202, g:nAns}))
deltad = 0.726
deltat = 0.015
deltag = deltanAns
deltan = sy.sqrt((n.diff(d)*deltad)**2 + (n.diff(t)*deltat)**2 + (n.diff(g)*deltag)**2)
print('deltag =: ',deltan.subs({d:17.41, t:2.202, g:nAns}))
