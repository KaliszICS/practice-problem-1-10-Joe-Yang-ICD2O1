'''
    Lesson: Math Library
    Author: Joe Yang
    Date Created: October 2, 2024
    Date Last Modified: October 2, 2024
'''

  import math 

def q1(): 
  #Write Assignment code here

  num= float(input("Input a number: "))
  print(math.sqrt(num))

def q2(): 
  #Write Assignment code here

  num= int(input("Input a number: "))
  print(math.isqrt(num))

def q3(): 
  #Write Assignment code here

  num= float(input("Input a number: "))
  print(math.floor(num))


def q4(): 
  #Write Assignment code here

  num= float(input("Input a number: "))
  print(math.ceil(num))

def q5(): 
  #Write Assignment code here

  num= float(input("Input a number: "))
  num2= float(input("Input another number: "))
  num= (num * num2 / 2)
  print(math.trunc(num))



#Do not alter the following code
#Comment out the following code when running your tests
'''
q1()
q2()
q3()
q4()
q5()
'''