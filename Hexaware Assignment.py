#!/usr/bin/env python
# coding: utf-8

# # Ans 1

# In[7]:


def check(a):
    if(len(str(a))==3):
        print("It is three digit number")
    else:
        print("It is not three digit number")
if __name__ == "__main__":
    a=int(input())
    check(a)


# # Ans 2

# In[12]:


def check(a):
    if(a>=18):
        print("He is eligible to vote")
    else:
        print("He is not eligible to vote")
if __name__ == "__main__":
    a=int(input("enter age : "))
    check(a)


# # Ans 3

# In[13]:


def check(a):
    if(a>=60):
        print("He is senior citizen")
    else:
        print("He is not senior citizen")
if __name__ == "__main__":
    a=int(input("enter age : "))
    check(a)


# # Ans 4

# In[15]:


def check(a,b):
    if(a>b):
        print(b," is lowest no.")
    elif(a==b):
        print("both are equal")
    else:
        print(a," is lowest no.")
if __name__ == "__main__":
    a=int(input("enter 1st no. : "))
    b=int(input("enter 2nd no. : "))
    check(a,b)


# # Ans 5

# In[16]:


def check(a,b):
    if(a>b):
        print(a," is largest no.")
    elif(a==b):
        print("both are equal")
    else:
        print(b," is largest no.")
if __name__ == "__main__":
    a=int(input("enter 1st no. : "))
    b=int(input("enter 2nd no. : "))
    check(a,b)


# # Ans 6

# In[18]:


def check(a):
    if(a>=0):
        print("It is positive no.")
    else:
        print("It is negative no.")
if __name__ == "__main__":
    a=int(input("enter no. : "))
    check(a)


# # Ans 7

# In[19]:


def check(a):
    if(a%2==0):
        print("It is even no.")
    else:
        print("It is odd no.")
if __name__ == "__main__":
    a=int(input("enter no. : "))
    check(a)


# # Ans 8

# In[37]:


arr = ['zero','one','two','three','four','five','six','seven','eight','nine']
 
def number(n):
    if(n==0):
        return "Zero" 
    else:
        small_ans = arr[n%10]
        ans = number_2_word(int(n/10)) + small_ans + " "
    return ans
 
n = int(input())
print(number(n))


# # Ans 9

# In[38]:


def check(a):
    if(a%2==0 and a%3==0):
        print("It is divisible by 2 and 3")
    else:
        print("It is not divisible by 2 and 3")
if __name__ == "__main__":
    a=int(input("enter no. : "))
    check(a)


# # Ans 10

# In[41]:


def check(a,b,c):
    if (a >= b) and (a >= c):
        return a
    elif (b >= a) and (b >= c):
        return b
    else:
        return c
    
if __name__ == "__main__":
    a=int(input("enter 1st no. : "))
    b=int(input("enter 2nd no. : "))
    c=int(input("enter 3nd no. : "))
    print("The largest number is",check(a,b,c))


# In[ ]:




