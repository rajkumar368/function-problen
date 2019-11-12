#!/usr/bin/env python
# coding: utf-8

# # problem related to function 
# 
# 1. Take two aregument,check if first number is even, multiply them otherwise add them and return the result
# 

# In[ ]:


def checkEven(num1,num2):
    if num1 % 2 == 0:
        return num1*num2
    else:
        return num1 + num2
    
checkEven(10,20)


# 2. Jack and jill Game -- jack increment by 2 and jill decrement by 2
#   
#    

# In[10]:


value = 0
def jackfunc():
    global value
    value+=2
    
def jillfunc():
    global value
    value-=1
    
i = 0
while i<10:
    jackfunc()
    i+=1
    
value

i = 0
while i<10:
    jillfunc()
    i+=1
    
value
# In[9]:


value = 0
def jackfunc(value):
    value+=2
    return value

def jillfunc(value):
    value-=1
    return value

i = 0
while i<10:
    value = jackfunc(value)
    i += 1
value


# 3. write a function which takes a string,check if string contains vowel print it once otherwise print it twice? 

# In[48]:


def checkstring(word,vowel):
    for char in word:
        if char in vowel:
            return True
    else:
        return False
        
checkstring("hello","el")


# In[ ]:


def timeCount(word,time):
    for t in range(time):
          print(word)


# In[69]:


def printCheck(word,vowel,time):
    if checkstring(word,vowel):
        print(word)
    else:
        timeCount(word,time)
        
printCheck("hello","aeiou",2)
printCheck("sdfr","aeiou",2)


# 4. use mymultFunc(10,20,31,43,18,7,40) and multiply all even number?

# In[115]:


res = 1
def mymultFunc(*args):
    global res
    for value in args:
        if value%2==0:
            res*=value
    return res
mymultFunc(10,20,30,7,23)       

            

