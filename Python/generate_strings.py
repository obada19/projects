class State:
 def __init__(self,value,accepted):
     self.value = value
     self.accepted = False
     self.nextState0 = None
     self.nextState1 = None

 def setNextState0(self,nextState0):
     self.nextState0= nextState0
 def setNextState1(self,nextState1):
     self.nextState1 = nextState1
 def getValue(self):
     return self.value



state1 = State(1,False)
state2 = State(2,False)
state3 = State(3,False)
state4 = State(4,False)
state5 = State(5,True)
state6 = State(6,True)
state7 = State(7,True)
state8 = State(8,True)
state9 = State(9,False)
state10 = State(10,False)




state1.setNextState0(state6)
state1.setNextState1(state7)
state2.setNextState0(state10)
state2.setNextState1(state7)
state3.setNextState0(state4)
state3.setNextState1(state4)
state4.setNextState0(state10)
state4.setNextState1(state1)
state5.setNextState0(state9)
state5.setNextState1(state3)
state6.setNextState0(state6)
state6.setNextState1(state5)
state7.setNextState0(state7)
state7.setNextState1(state10)
state8.setNextState0(state2)
state8.setNextState1(state2)
state9.setNextState0(state9)
state9.setNextState1(state1)
state10.setNextState0(state8)
state10.setNextState1(state4)

final_states = [state5,state6,state7,state8]
m = 1
alphabet = ['0','1']

S_negative = []
S_positive = []

F_positive = [state5,state6,state7,state8]
F_negative = [state1,state2,state3,state4,state9,state10]
def allPossiableStrings(n):
    global  m


    while(m < n):
        m+=1
        reversed_alphabet = sorted(alphabet,reverse=True)
        for i in range(len(alphabet)):
            alphabet[i] = '0' + alphabet[i]
        for i in range(len(alphabet)):
            reversed_alphabet[i] = '1' + reversed_alphabet[i]
        for j in range(len(reversed_alphabet)):
            alphabet.append(reversed_alphabet[j])



    return alphabet



def get_training_set(allStrings,language):
    global S_negative
    global S_positive
    total =[]
    for s in language:
        if s in allStrings:
            allStrings.remove(s)
    S_negative = allStrings
    S_positive = language
    total.append(S_positive)
    total.append(S_negative)
    return total





def generate_strings(l,state,finale_states):
    temp_language =[]
    language =[]
    state_next =State
    c =1
    length =0
    while(c <=l):

        all_strings = allPossiableStrings(c)
        for string in all_strings:
            temp_language.append(string)
        c+=1
    for s in temp_language:
        state = state1

        for ch in s:
            if ch == '0':
                state = state.nextState0
            if ch == '1':
                state = state.nextState1
        if state in final_states:
#            print(state.value)
            language.append(s)
   # print("training set",get_training_set(temp_language,language))
    get_training_set(temp_language, language)
    return language
#print("thisissss",S_positive)
leng = 3
count = 0
#print("accepted strings up to length",leng,": ",generate_strings(leng,state1,final_states))
# for i in S_negative:
#     count +=1
# print(count)
#

generate_strings(15,state1, final_states)
print(len(S_positive),len(S_negative))
#print("thisissss", S_positive, S_negative)