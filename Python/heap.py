import time
#insertions in heap(i) to o (logn)
#when isertion we go upwards.
# we start first by adding the element at the last position on the list.
# after that we divide it by to and then copmare it with the element
# and in max heap if it is bigger then change postion. other wise it stays there do this until it is not bigger.
# the formula for heap element is: element is at index i. left child is 2*i -right child is 2*i+1 and parent of this element is (i/2)
# we have min heap and max heap they are the opposite
# deletion in heap when reomving we take the first one that means in max heap we take the biggest and remove it and put the last element in its place
# after that we compare the two child nodes to be put as the new root which one is bigger. after that we take the biggest and put it as root and put the old root in its place.
# then we compare the childs of the old root and repeat the same process if its in the right place ok if not we do the same with it
# the time for remocing and insertion is dependent on the height whcih means (log n)
# after deletion we take the deleted element and place it in the freed place in the array which is the last one

#step 2 how to create a heap
# time taken is n log n  to isertion and n log n for deletion and that means 2 log n which s o(log n)



# what is the different with hipfy
# in hipfy we take the oppsosite direction to insertion which means deletion and we start from right to left and the time taken is o (n)
# this is faster

#priotityqueues
# if it is implemented using heap it will become faster
# and the priority of the element is its value som in min heap the lowest is the most priority
# and in max heap the highest number has heighst priority

# the 7.5 is probably the pririty queue algorithem


# implementation ideas.
# first make list that take keay nad to make binary tree
# make node to hold the values.
# make list holding the intial values
# reorder that list so that it make a heap using the formulas that we have
# add the sorted heap/list as nodes to the binary tree

# make ordered list first the add them as nodes
import heapq
from random import randint


def deletion(list):
    # this takes log n time
    if len(list)<1:
        return 0
    else:
        i = 1
        item = list[len(list)-i]
        list.remove(item)
        heapifying(list)

def insertion(list, item):
    # this takes log n time
    list.append(item)
    heapifying(list)

def sifting_down(list, i, boundary_of_Heap):
# when using big sample recursion here gives us recursion error
    while(True):
# maybe chanfe this formula to the one in the stated in the abdul
# it sounded correct
# 2 and one maybe done t osay that we dont need
# to change the location of the first and the second index as they shoyld be already in the right placei thinkkkk
        l, r= i*2+1, i*2+2
        # first checking if the left and right node are in the boundary
        # of the heap
        if max(l, r) < boundary_of_Heap:
            # if so then check if the root is bigger then left and right
            # if it is keep it the way it is
            if list[i] >= max(list[l], list[r]):
                break
#           if not and the left is bigger then the right then swap the left and the parent
            # and make left is as the parent
            elif list[l]> list[r]:
                swap(list,i,l)
                i=l
            # if the right is bigger then  put the right as parent and swap
            else:
                swap(list,i,r)
                i = r
                # if only the left leaf is in boundary of the array

        elif l < boundary_of_Heap:
            # if left leaf is bigger then i
            if list[l]>list[i]:
                # swap them and put left in its place
                swap(list,i,l)
                i = l
                # else go out
            else: break
            # the right is the one who is in the boundary
        elif r < boundary_of_Heap:
        #    check if it is larger
            if list[r]> list[i]:
                # if so swap and change them
                swap(list, i ,r)
                i = r
            else: break
        else: break

def heapifying(list):
    # this range does floor division and stops at the end(index 0) and goes one step backwards
    for i in range(len(list)-2//2,-1,-1):
        sifting_down(list, i, len(list))
        # this one stops at index 1 and starts from the last index
    for end in range(len(list)-1,0,-1):
        swap(list,0,end)
        sifting_down(list,0,end)

def swap(list,i,j):
    list[i], list[j] = list[j], list[i]

list0=[]
for i in range(0,50):
    n = randint(1,50000)
    list0.append(n)
list=[1,2,9,3,4,5,6,7,8,1]
list1=[6,5,42,32,22,1]
start = time.time()
heapifying(list)
heapifying(list0)
end = time.time()
print("start",start, "end",end)
print(list)
start1 = time.time()
heapq.heapify(list1)
end1=time.time()
print("start",start1, "end",end1)
#print(list1)
#print(list0)