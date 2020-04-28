#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.
def ReverseUser(fname, lname):
  
  return  fname[::-1]+" "+lname[::-1]
ReverseUser("Hanen", "Fourati")


# In[13]:


# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn
def Cal(n):
  a= str(n)
  b= int(a)
  aa= str(n)+str(n)
  bb= int(aa)
  aaa= str(n)+str(n)+str(n)
  bbb= int(aaa)
  c= str(b+bb+bbb)
  return  c+"("+a+"+"+aa+"+"+aaa+")"
Cal(5)


# In[17]:


# Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user.
num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))


# In[19]:


# Write a program to check whether a given year is a leap year or not.
def IsLeap (year):
 if (( year%400 == 0)or (( year%4 == 0 ) and ( year%100 != 0))):
    print("%d is a Leap Year" %year)
 else:
    print("%d is Not the Leap Year" %year)
IsLeap (2000)


# In[21]:


# Write a program to remove the characters which have odd index values of a given string.
def OddIndexString(str):
  result = "" 
  for i in range(len(str)):
    if i % 2 == 0:
      result = result + str[i]
  return result

print(OddIndexString("hello team"))


# In[39]:


#In this challenge, you must discount a price according to its value.

def Discount(price):
  result = "" 

  if price>=500 :
    result = price*0.5
  elif (price<500) and (price>=200) :
    result = price*0.3
  elif price<200:
    result = price*0.1
            
  return int(result)

Discount(1000)

