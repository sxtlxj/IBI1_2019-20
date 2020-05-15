# What does this piece of code do?
# Answer: find the primer factor of a number between 1 and 100

# Import libraries
# randint allows drawing a random number, 
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

p=False #set p is False to get into the loop
while p==False:
    p=True
    n = randint(1,100) #get a number that is between 1 and 100
    u = ceil(n**(0.5)) #take the ceiling of the square root of n
    for i in range(2,u+1): #find the primer factor of n
        if n%i == 0: # if there is still a primer factor, change p to False so that n can get into the loop again
            p=False


     
print(n)
