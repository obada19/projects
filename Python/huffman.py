import heapq

# this is the first part were we have variable length encoding

text = (input("enter a message to compress: "))   #"Du åt ca fire wienerpølser og tok taxi hjem fra byen med ære fra quizen."
#text = "Du åt ca fire wienerpølser og tok taxi hjem fra byen med ære fra quizen."
class Node:
    def __init__(self, letter, freq):
        self.freq = freq
        self.letter = letter
        self.right = None
        self.left = None
        #we can not compare two nodes in the heap directly so we have to define
        # the comparing. here we are defining it as comparing frequencies
    def __lt__(self, items):
        return self.freq < items.freq
        # we are also defining the equal mechanism
    def __eq__(self, items):
        # here we are adding null pointer exception
        if items!= None:
            return False
        # in case we have a node that is not of the type of the heap node that we want but still have frequency we return false as well
        if not isinstance(items, Node):
            return False
        return self.freq==items.freq

class huffmantree:
    def __init__(self):
        self.heap = []
        self.thecode = {}
        self.coded_in_one=""
        self.coded_in_letters= []

    def fequency_maker(self):
        frequency = {}
        for i in text:
            if not i in frequency:
                frequency[i] = 0
            frequency[i] += 1
        return frequency


    def adding(self, frequency_dictionary):
        for i in frequency_dictionary:
            node = Node(i, frequency_dictionary[i])
            heapq.heappush(self.heap, node)


    def merge(self):
        while len(self.heap)>1:
            node1 = heapq.heappop(self.heap)
            node2 = heapq.heappop(self.heap)

            merged = Node(None, node1.freq + node2.freq)
            merged.left = node1
            merged.right = node2

            heapq.heappush(self.heap, merged)

    # recursive method to travers the tree and give the codes to the letters
    def reading_the_code(self,root,code_variable):
        if root == None:
            return
        # first we check for letter
        if root.letter != None:
            # if we find a letter we assign the code that we reaced to in the dictionary called the code
            self.thecode[root.letter]= code_variable
            return
    # we recursivly check left and right with the above check statements
        self.reading_the_code(root.left, code_variable +"0")
        self.reading_the_code(root.right, code_variable +"1")
    #this methd intiliazes the reading the code method and putting the root and empty string for the variable used in the previos method
    def finishingthecode(self):
        root = heapq.heappop(self.heap)
        self.reading_the_code(root,"")

    def making_the_message_in_code(self, text):
        for i in text:
            for key in self.thecode:
                if i == key:
                    self.coded_in_letters.append(self.thecode[key])
        for i in text:
            self.coded_in_one += self.thecode[i]








# calling the class and it's methods
dj = huffmantree()
frequency_dictionary = huffmantree.fequency_maker(text)
dj.adding(frequency_dictionary)
dj.merge()
dj.finishingthecode()
dj.making_the_message_in_code(text)
print("1. this is the first part:")
print(f"this is the codes with the corresponding charachters:\n {dj.thecode}")
print(f"this is the message coded in letters seperated:\n {dj.coded_in_letters}")
print(f"this is the message coded in one:\n {dj.coded_in_one}","\n")




# this is the second part with fixed length encoding

def Fixed_length_encoding(codedinpieces):
    # it is neccessary to make a list containing the extra zeros that was added to each charachter
    # in order to use it to remove the extra zero when decompressing
    extra_info =[]
  # this loop takes ezch string turn them into list of integers
    for i in codedinpieces:
        usable_list_variable= [int(x) for x in str(i)]
        # here we check to see if remainder of modulo 8 in order to discarded the one that are already 8
        if len(usable_list_variable) % 8 !=0:
            # we then subtract 8 from the length of the list of the integer and add that number to the xtra info list
            extra = 8 - len(usable_list_variable)
            extra_info.append(extra)
    c = 0
   # here we add the zeros until we reach 8 which is a byte(fixed length)
    for i in extra_info:
        for y in range(i):
            codedinpieces[c] +="0"
        c+=1


Fixed_length_encoding(dj.coded_in_letters)
print("2. this is the second part:")
print("code in fixed length:\n",dj.coded_in_letters)