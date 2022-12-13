from collections import Counter
#import vigenereCipher
import numpy
import vigenerecipher
import pyperclip
#import freqAnalysis, detectEnglish

letterFrequency = {'E' : 12.0,
'T' : 9.10,
'A' : 8.12,
'O' : 7.68,
'I' : 7.31,
'N' : 6.95,
'S' : 6.28,
'R' : 6.02,
'H' : 5.92,
'D' : 4.32,
'L' : 3.98,
'U' : 2.88,
'C' : 2.71,
'M' : 2.61,
'F' : 2.30,
'Y' : 2.11,
'W' : 2.09,
'G' : 2.03,
'P' : 1.82,
'B' : 1.49,
'V' : 1.11,
'K' : 0.69,
'X' : 0.17,
'Q' : 0.11,
'J' : 0.10,
'Z' : 0.07 }
# this is an arbitrary cipher text i found decoded using vigenere to test the code on
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ciphertext = "MBQIZYLYUOEVHXGDPHBHFIPMGNDPOYVNUPYMLIIOPHUSMSELNLPFYXPBAJDEMIFBWPRHASXEEBGNLRUYUORXAUFJDNNMFMTOXNTFCILNAGFWACEIZYLYUTTRMBQXLCHZMQWEGHQECSTXFILXMBQMZGTFSPGIKHYFYXPUZUDXHVGJWHBHRBNXTLFIFVLNMSEWHZRUSIWUKXTXAUTBYKHPQSUYLNXJVIMBQSPWMIRVHEBNIILXUYOBFWXBQXLWWII" \
             "OLXMBQQFFEUEUYMZBFECMGEUOREGXOPXTEUUOTRZUNP" \
             "FXAIIUSIEIOBWKHPQSYQXHFXLRMMFPMYEFPPKIACEIZ" \
             "YLYIITGAYJQWEBHEXSCMBQSPEKYNVWPWILFCWHOFTTH" \
             "XBUTSSNMQSTKANZPHWHUDUSYKAAFDSNNMOOPBYEEZA" \
             "GCZGCSGNAGLFNFXEZDXLBSPXMSYVNLRIGSLZXLMHPX" \
           "IETPVPBAJDEWCEULRMXQTNIGXMOESYAQORLBMWILREC" \
             "WFRIGATJDOAUZQCSLMQSSELUNJESYUNFWPRUZEWMDYE" \
            "GFVAUFTFRECWFRIGATJDOAUZQCSLMQSTWGYDWZYLUZE" \
             "YSMMAHZSWUFDZRJOQSTRZ"
# use three letter to see how possible
printedposition = []
finalList = []
listwithfrequentAccurances = []
seen = set()
# STEP 3
n = 3

locations = []
dividedstrings = [ciphertext[i: i + n] for i in range(0, len(ciphertext), n)]


def find(dividedstring):
    global printedposition
    for i in dividedstring:
        for g in dividedstring:
            if i == g:
                printedposition.append(i)

        for s in range(0, len(dividedstring)):
            if dividedstring[s] == i:
                res = s + 1

                printedposition.append(res)

                break


def removNumber(list):
    return [x for x in list if isinstance(x, str)]


def findonlurepeated(reaptedlist):
    for i in s:
        if s.count(i) > 1:
            finalList.append(i)


def nonrepeatedfinallist(finallist1):
    for i in finalList:
        if i not in seen:
            seen.add(i)
            listwithfrequentAccurances.append(i)


result = []
counter = 0


def finddistance(listwithfrequenaccurances, dividedstrings):
    global counter

    # maybe taking the value and calculating the distance here
    for i in listwithfrequenaccurances:
        for g in enumerate(dividedstrings):
            if i == g[1]:
                result.append(g[0])


distances = []


def calculatingthesitance(result):
    c = 0
    # i is the value and result[i] is the value in the index
    # calculate the distances between the two numbers
    for i in result:
        if c == 0:
            h3 = result[c + 1] - i
        #  print(h3)

        if result[c + 1] < i:
            h = result[c + 1] - i
        # print(h)
        # s = i+1 - i
        # distances.append(s)

        elif i < result[c + 1]:
            h2 = result[c + 1] - result[c + 2]
            # print(h2)
    c += 1
    pass
    # what to do here


listOfListsOfFactors = []


def factorthenumber(distances):
    c = 0
    for g in distances:
        for i in range(2, g + 1):
            if g % i == 0:
                listOfListsOfFactors.append(i)


listOfListsOfFactors.sort()

mostfactorfreq = []


def mostfrequentfactor(listoflistsoffactors):
    global temp
    r = Counter(listoflistsoffactors)
    heighst = r.most_common(2)
    print("this is the two factors with the most values", heighst)
    for i, s in heighst:
        mostfactorfreq.append(i)


g = [20, 4, 6, 8, 10, 20, 10, 5, 5, 5]
# put the list of factors to be facotred here instead of g
factorthenumber(g)
find(dividedstrings)
s = removNumber(printedposition)
findonlurepeated(s)
nonrepeatedfinallist(finalList)
finddistance(listwithfrequentAccurances, dividedstrings)
calculatingthesitance(result)
mostfrequentfactor(listOfListsOfFactors)
listOfListsOfFactors.sort()
#print("this is just the values", mostfactorfreq)
keylength1 = mostfactorfreq[0]
keylength2 = mostfactorfreq[1]
# getting keylength as a singel variable or as a list try both maybe?
everynletter = []
last_item = len(ciphertext) - 1
#print(last_item)




#most freq fact is the one holding the most recurring values of factors
def getting_the_most_frequent_string(mostfreq, ciphertext):

     #this is for getting the range from 0 to range of the frequent factor
    for i in mostfreq:
       for j in range(i):
           s = ciphertext[j::i]
           everynletter.append(s)
getting_the_most_frequent_string(mostfactorfreq, ciphertext)
def freanalysis(nthletter):
    # we are encrypting by using a0 +b1 = 1b
    # so this means that when anaylsing the frequences we should remove the number of the letter from
# the nth letter list and the result that we get the recurreing characters are most likely the subkeys
  #  this can be used to decrypt at the end later
    keyindex= 0
    key=0# key.upper()
    for i in nthletter:
        for j in i:
            j -= LETTERS.find(key[keyindex])
            pass
# frequency analysis takes the nth letter copmares it to every letter in the alphbet and then check recurring letters and
# the most frequent one is most likely the one letter of the key
list_of_values_for_possible_subkeys= []
def freqanalsis(nthletter, letters):

    xindex = 0
    # looping through every possible subkey
    for i in nthletter:
        # taking every letter in the most freq list
        for j in i:
            # taking the value of the letter we have in the list in the letter list to get a value
            s = letters.find(j)
            for x in letters:
                #   subtracting the values from each other to see if we have someething reccurent
                s = s - letters.find(x[xindex])
                list_of_values_for_possible_subkeys.append(s)
                # returning the original value to s in order to subtract in the for loop
                s = letters.find(j)
freqanalsis(everynletter, LETTERS)
# this is the list that we get when subtracting every number in the every nth letter in absolute value.
# now we just have to find the value of each number and then putting it in a list to see frequency
#print("fhdsfdasfdafds333333333333333",len(list_of_values_for_possible_subkeys))
list_of_values_for_possible_subkeys = numpy.abs(list_of_values_for_possible_subkeys)
#print("fhdsfdasfdafds",len(list_of_values_for_possible_subkeys))
firstlist=[]
secondlist=[]
everynthletter_in_chars=[]

for i in everynletter:
    for j in i:
        everynthletter_in_chars.append(j)
thisisdividedlist=[]
for i in ciphertext:
    thisisdividedlist.append(i)
def finding_right_subkey():
    s1 = len(thisisdividedlist)/keylength1
    s2 = len(thisisdividedlist)/keylength2
    s3= int(s1)*keylength1
    s4= int(s2)*keylength2

    for i in  range(s3):
        s = everynthletter_in_chars[i]
        firstlist.append(s)
    for j in range(s3, len(everynthletter_in_chars)):
        s5= everynthletter_in_chars[j]
        secondlist.append(s5)


def findingthesubkey2():
   listvariables = firstlist/keylength1
   pass
list_of_values_for_possible_subkeys_letters= []
def findingcandidatesforsubkeys():
    for i in list_of_values_for_possible_subkeys:
        variableletter= LETTERS[i]
        list_of_values_for_possible_subkeys_letters.append(variableletter)


def seperating_the_two_lists():
    pass
list_of_values_for_possible_subkeys1right=[]
#finding_right_subkey()
#findingcandidatesforsubkeys()
counter1 = 0
def dividing():
    global counter1
    count = 0
    if counter1 == len(list_of_values_for_possible_subkeys)-1:
        return 0
    elif count == 0:
       for i in range(count,3):
           list_of_values_for_possible_subkeys1right.append(list_of_values_for_possible_subkeys[counter1])
           count+=1
           counter1 +=1

    if count ==3:
        list_of_values_for_possible_subkeys.append(" ")
        return dividing()

#dividing()
#print(list_of_values_for_possible_subkeys1right)
#print(len(everynthletter_in_chars))
#print(len(thisisdividedlist))
#print(len(firstlist), len(secondlist))

#print(len(list_of_values_for_possible_subkeys))
#print(len(list_of_values_for_possible_subkeys)/26)
#print(len(list_of_values_for_possible_subkeys_letters))
#print("distances",distances, result)
#print("first",firstlist)
#print("seond",secondlist)
#print(everynthletter_in_chars)
#print(list_of_values_for_possible_subkeys)
#print("this is the number of the most frequency: ",len(everynletter))
#print(len(ciphertext))
#print("this is every n letter", everynletter)





# def mostfrequentfactor(listoflistsoffactors):
#   global temp
# r = Counter(listoflistsoffactors)
# maximum = max(r, key=r.get)
# this gives us it with the value of the dictionary
# se =  max(r.items(), key=lambda k: k[1])
# print(maximum)
#  heighst = r.most_common(2)
# print("this is the two factors with the most values", heighst)
# for i, s in heighst:
#   mostfactorfreq.append(i)


# this works to remove duplicates
# for i in finalList:
#     if i not in resutl:
#         resutl.append(i)
# print("this is the result",resutl)
# print("this is the divided string", dividstringsinOneLine)
# find(dividstringsinOneLine)
# find(dividedstrings)
# s = findRepeatedSequences(ciphertext)
# s = find(dividedstrings)


# def findRepeatedSequences(ciphertext):
#     for i in range(0, len(ciphertext), n):
#        dividedstrings.append(ciphertext[i : i + n])


# pressing alt gr and 7 puts brackets on the matter
# important use of range and list iteration and appending in strings
# def findRepeatedSequences(ciphertext):
#    for i in range(0, length, n):
#       dividedstrings.append(ciphertext[i : i + n])
# findRepeatedSequences(ciphertext)
# using panda lib
# df = pd.DataFrame({'Number': listOfListsOfFactors})
# df1 = pd.DataFrame(data=df['Number'].value_counts(), columns=[['Number', 'Count']])
# df1['Count'] = df1['Number'].index
# list(df1[df1['Number'] == df1.Number.max()]['Count'])S

freq_match={}
def find_freq_match_score(ciphertext):
    global freq_match
    for i in ciphertext:
        counter3 = 0
        for j in ciphertext:
            if i == j:
                counter3 +=1
        freq_match.update({i:counter3})
    return freq_match
find_freq_match_score(ciphertext)
list_sorted_descending_most_freq_letters_in_ciphertext= sorted(freq_match, key=freq_match.get, reverse=True )
list_sorted_descending_most_freq_letters_in_english = sorted(letterFrequency, key=letterFrequency.get, reverse=True )
#print(list_sorted_descending_most_freq_letters_in_ciphertext)
#print(list_sorted_descending_most_freq_letters_in_english)
temperoraylist= []
temperoraylist1= []
def getting_mostfreq_and_leastfreq():
    counter4= 0
    global temperoraylist
    for i in list_sorted_descending_most_freq_letters_in_ciphertext:
        # this is made to 6 because we have two letters that has the same value=32
        if counter4==6:
            break
        else:
            temperoraylist.append(i)
            counter4 +=1

    counter4= 0
    for i in range(len(list_sorted_descending_most_freq_letters_in_ciphertext)-6,len(list_sorted_descending_most_freq_letters_in_ciphertext),1):
        # this is made to 6 because we have two letters that has the same value
        if counter4==6:
            break
        else:
            temperoraylist.append(list_sorted_descending_most_freq_letters_in_ciphertext[i])
            counter4 +=1



    counter4 = 0
    global temperoraylist1
    for i in list_sorted_descending_most_freq_letters_in_english:
        # this is made to 6 because we have 6 of the most common and uncommon in cipher text
        if counter4 == 6:
            break
        else:
            temperoraylist1.append(i)
            counter4 += 1

    counter4 = 0
    for i in range(len(list_sorted_descending_most_freq_letters_in_english) - 6,
                   len(list_sorted_descending_most_freq_letters_in_english), 1):
        # this is made to 6 because we have 6 of the most common and uncommon in cipher text

        if counter4 == 6:
            break
        else:
            temperoraylist1.append(list_sorted_descending_most_freq_letters_in_english[i])
            counter4 += 1

match_score_list=[]
def match_score():

    for i in list_sorted_descending_most_freq_letters_in_ciphertext[:6]:
        match_score = 0
        if i in list_sorted_descending_most_freq_letters_in_english[:6]:
            match_score +=1
            match_score_list.append([i,match_score])


    for i in list_sorted_descending_most_freq_letters_in_ciphertext[-6:]:
        match_score1 = 0
        if i in list_sorted_descending_most_freq_letters_in_english[-6:]:
            match_score1 += 1
            match_score_list.append([i,match_score1])


getting_mostfreq_and_leastfreq()
s=match_score()
# this is the possible subkeys
print(match_score_list)
#print(freq_match)
#print(temperoraylist)
#print(temperoraylist1)
# using the above method gives us possible subkeys according to english frequency mathcing and they are E and I and J
# the reason why I is also included because it has the same value of x in cipher text which means it could have in the later postion
# this is one of the faults of using a dictionary since letter with the same frequency might end up in wrong place
# frequency of I and X
# 'X': 32,'I': 32,
#['E', 'M', 'U', 'I', 'X', 'C', 'D', 'V', 'J', 'K']
#['E', 'T', 'A', 'O', 'I', 'K', 'X', 'Q', 'J', 'Z']