import csv, sys
from random import randint

reader = csv.reader(open(r'C:\\Users\\obada\\Downloads\\worldcities.csv', encoding="utf8"))
cityname = []
latitudereal = []
latitude = []
freq_random = []
count = 1
for i in reader:
    if i[4] == "Norway":
        cityname.append(i[0]),
        latitude.append(i[2]),
        freq_random.append(count)
        count += 1

for i in latitude:
    s = float(i)
    latitudereal.append(s)
listwith_freq4 = [list(i) for i in zip(cityname, latitudereal, freq_random)]

keys = [list(i) for i in zip(cityname, latitude)]
costs = {}


class Node:
    def __init__(self, key, freq, city):
        self.key = key
        self.freq = freq
        self.city = city

    def __str__(self):
        return f"Node(key={self.key},freq={self.freq}, city={self.city})"



def printintthebinarytree(root, key, i, j, parent, is_left):


    if i > j or i < 0 or j > len(root) - 1:
        return

    node = root[i][j]
    if parent == -1:  # root does not have a parent
        print(f"{key[node]} is the root of the binary search tree.")
    elif is_left:
        print(f"{key[node]} is the left child of key {parent}.")
    else:
        print(f"{key[node]} is the right child of key {parent}.")

    printintthebinarytree(root, key, i, node - 1, key[node], True)
    printintthebinarytree(root, key, node + 1, j, key[node], False)

def findoptimalbinraysearchtree(nodes):
    nodes.sort(key=lambda node: node.key)
    number = len(nodes)
    keys = [nodes[i].key for i in range(number)]
    freq =[nodes[i].freq for i in range(number)]
    cost = [[freq[i] if i == j else 0 for j in range(number)] for i in range(number)]
    suming = [[freq[i] if i == j else 0 for j in range(number)] for i in range(number)]
    root = [[i if i == j else 0 for j in range(number)] for i in range(number)]
    for interval_length in range(2, number + 1):
        for i in range(number - interval_length + 1):
            j = i + interval_length - 1
            # setting the value to infinity
            cost[i][j] = sys.maxsize
            suming[i][j] = suming[i][j - 1] + freq[j]
            # r is a temporarial root
            for r in range(root[i][j - 1], root[i + 1][j] + 1):
                # optimal cost for the left subtree
                left = cost[i][r - 1] if r != i else 0
                # optimal cost for the right subtree
                right = cost[r + 1][j] if r != j else 0
                coste = left + suming[i][j] + right

                if cost[i][j] > coste:
                    cost[i][j] = coste
                    root[i][j] = r
        print(f"\n this is The cost of optimal Binary search tree which is {cost[0][number - 1]}.")
    printintthebinarytree(root, keys, 0, number - 1, -1, False)

def search(nodes, input):
    for x in nodes:
        if type(input) is str:
            if input == x.city:
                print(x)
        for x in nodes:
            if type(input) is str:
                if float(input) == x.key:
                    print(x)





nodes = [Node(i[1], i[2], i[0]) for i in listwith_freq4 ]


input1 = input("search for city or latitude")


findoptimalbinraysearchtree(nodes)
search(nodes, input1)
