import math
from datetime import datetime
import random

# using random function to generate random large datasets to use on the algorithm
import timeit
import time
import numpy as numpy

list=[]
for i in range(0,10000):
    s= random.randint(0,1000)
    list.append(0)

last_index= len(list)-1
list_length= len(list)
start = 0


def deletion(list):
    # this takes log n time
    if len(list)<1:
        return 0
    else:
        i = 1
        item = list[len(list)-i]
        list.remove(item)
        heap_maker(list)

def insertion(list, item):
    # this takes log n time
    list.append(item)
    heap_maker(list)

# this function is to be used when comparing with the biggest of the two children so we can sift through
def max_of_two_numbers(i, j):
    if i >= j:
        return i
    else:
        return j
def swapping(list, x, y):
    list[x],  list[y] = list[y], list[x]

counter= 0
def sifting_through(list,i,end_of_heap):
    global counter
    # first define the left and right child of the element
    # we had choice between recursion and while loop.
    # while was chosen because the logic of making it is much easier to understand then recursion
    # plus recursion started making recursion errors when the data sets were too big.
    while True:
        left = i * 2 + 1
        right = i * 2 + 2
        # this condition will check if the left and right of the element of this list is in the range of the heap/list
        # if it is in the heap range then we do operations inside if not we check lef and right if not then we break out of the loop
        # since it means the element is in the right position
        if max_of_two_numbers(left, right) < end_of_heap:
            if list[i] >= max_of_two_numbers(list[left], list[right]):
                break
            elif list[left]< list[right]:
                swapping(list, i, right)
                counter+=1
                i=right
            else:
                swapping(list, i, left)
                counter+=1

                i = left

        elif left < end_of_heap:
            if list[i]< list[left]:
                swapping(list,i,left)
                counter+=1

                i=left

            else:break

        elif right < end_of_heap:
            if list[i]< list[right]:
                swapping(list,i, right)
                counter+=1

                i = right
            else:break
        else: break

def heap_maker(list):
    global counter
    for i in range(last_index,-1,-1):
        sifting_through(list,i,list_length)

    for i in range(len(list)-1, start,-1):
        swapping(list, start, i)
        counter +=1
        sifting_through(list,start,i)


#time = datetime.now()
time= int(timeit.default_timer()*1_000)
heap_maker(list)
#time1= datetime.now()
time1= int(timeit.default_timer()*1_000)
print("thisis timer",time1-time)




this= list_length-1*math.log(list_length-1)
this1= 1000*math.log2(1000)
print(this, """""thissss""",this1)

print(counter)
heap_maker(list)
time3= datetime.now()

#print("time in seconds",time3-time2)


