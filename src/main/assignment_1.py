#Lorelai Barnes
#Assignment 1

import numpy as np
import struct


#Number 1

a = '010000000111111010111001'
a = a.ljust(64,'0')

sign = '0'
exponent = '10000000111'
mantissa = '1110101110010000000000000000000000000000000000000000'

e = 0
exp = 0
m = 0
man = 0
s = 0
for i in range(len(sign)):
  if(int(sign[i])==0):
    s = 1
  else:
    s = -1
for i in range(len(exponent)):
  e = int(exponent[i])
  exp += e*(2**(10-i))
  i+=1
          
for i in range(len(mantissa)):
  m = int(mantissa[i])
  man += m*(2**(-(i+1)))
  i+=1
            

ans = s*(2**(exp-1023))*(man+1)

print(ans,"\n")

#Number 2
chop = ans - 0.5
print(round(chop,0),"\n")

#Number 3
print(round(ans,0),"\n")

#Number 4
s = round(s,3)
exp = round(exp,3)
man = round(man,3)
t = 2**(exp-1023)
t = round(t,3)
r = s*(t-0.20575)*(man+1)

ab = ans - r
print(round(ab,4))
re = 0.4375/ans
print(re,"\n")


#Number 5
k=1

x = 1
def series(x):
  equ = 0
  for k in range(1,4):
    
    equ = equ + (-1**k)*(x**k/k**3)
    
  print(equ)
n = 10**(4/3) - 1
n= round(n)
print(n,"\n")

#Number 6
#A

def bisection_method(left: float, right: float, given_function: str):
   
    x = left
    intial_left = eval(given_function)
    x = right
    intial_right = eval(given_function)
    if intial_left * intial_right >= 0:
        print("Invalid inputs. Not on opposite sides of the function")
        return

    tolerance: float = .001
    diff: float = right - left

    
    max_iterations = 20
    iteration_counter = 2
    while (diff >= tolerance and iteration_counter <= 20):
        iteration_counter += 1
        if (iteration_counter >16):
          print(iteration_counter,"\n")

        # find function(midpoint)
        mid_point = (left + right) / 2
        x = mid_point
        evaluated_midpoint = eval(given_function)

        if evaluated_midpoint == 0.0:
            break
        
        # find function(left)
        x = left
        evaluated_left_point = eval(given_function)
        
        
        first_conditional: bool = evaluated_left_point < 0 and evaluated_midpoint > 0
        second_conditional: bool = evaluated_left_point > 0 and evaluated_midpoint < 0

        if first_conditional or second_conditional:
            right = mid_point
        else:
            left = mid_point
        
        diff = abs(right - left)

    
        
yes = 0
if yes == 0:

    # bisection gives us the first zero of any function to a certain error threshold
    left = -10
    right = 10
    function_string = "x**3 - 4*(x**2) - 10"
    bisection_method(left, right, function_string)
    


#B
def f(x):
    return x**3 + 4*(x**2) - 10

# Defining derivative of function
def g(x):
    return 3*(x**2) + 8*x

# Implementing Newton Raphson Method

def newtonRaphson(x0,e,N):
    
    step = 1
    flag = 1
    condition = True
    while condition:
        if g(x0) == 0.0:
            print('Divide by zero error!')
            break
        
        x1 = x0 - f(x0)/g(x0)
        
        x0 = x1
        step = step + 1
        
        if step > N:
            flag = 0
            break
        
        condition = abs(f(x1)) > e
    
    print(step)


# Input Section
x0 = 7
e = 0.0001
N = 20

# Converting x0 and e to float
x0 = float(x0)
e = float(e)

# Converting N to integer
N = int(N)

newtonRaphson(x0,e,N)

   
a = '010000000111111010111001'
a = a.ljust(63,'0')
a = int(a)

from math import *

# main function: call fp(float number n different from 0)
def fp(n):
  # base-2 scientific notation
  global s,e,m
  s,e=0,0
  p=1
  if n==1:
      s=1
  if fabs(n)>=2:
      p=-1
  while(p*fabs(n)*pow(2,p*e))<p:
    e=e+1
  if p==-1 and fabs(n)!=2:
      e=e-1
  m=fabs(n)*pow(2,p*e)
  e=-1*p*e
  np=pow(-1,s)*m*pow(2,e)
  print("\nBase-2 scientific notation:",
      "\nn= (-1)^S x 2^E x M (M=1.F)",
      "\nS="+str(s)+"\tE="+str(e)+"\tM="+str(m),
      "\nn="+str(np))
  print("\nIEEE-754:")
  print("\nHalf precision (binary16):")
  # IEEE-754 half precision (binary16)
  binaryxx(15,5,10)
  print("\nSingle precision (binary32):")
  # IEEE-754 single precision (binary32)
  binaryxx(127,8,23)
  print("\nDouble precision (binary64):")
  # IEEE-754 double precision (binary64)
  binaryxx(1023,11,52)

# IEEE-754 template
def binaryxx(eo,ed,md):
  print("S="+str(s),
      "\nE="+tobin(e+eo,ed)+" ("+str(e+eo)+")",
      "\nF="+tobin(round(modf(m)[0]*pow(2,md)),md)+
      " ("+str(round(modf(m)[0]*pow(2,md)))+")",
      "\nn="+str(pow(-1,s)*(1+round(modf(m)[0]*pow(2,md))/(pow(2,md)))*pow(2,e)))


