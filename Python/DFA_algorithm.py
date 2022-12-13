# Q = {1,2,3,4,5,6,7,8,9,10}
# while True:
#     b = input("->")
#     if not b != 0 or 1: break
#     if not b: break
#     a.append(b)
#
# print(a)
#
# a = []
# prompt = "-> "
# line = input(prompt)
#
# while line:
#     a.append(int(line))
#     line = input(prompt)
#
# print(a)

class DFA:
    current_state = None

    def __init__(self, states, alphabet, transition_function, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transition_function = transition_function
        self.start_state = start_state
        self.accept_states = accept_states
        self.current_state = start_state
        return

    def transition_to_state_with_input(self, input_value):
        if (self.current_state, input_value) not in self.transition_function.keys():
            self.current_state = None
            return
        self.current_state = self.transition_function[(self.current_state, input_value)]
        return

    def in_accept_state(self):
        return self.current_state in accept_states

    def go_to_initial_state(self):
        self.current_state = self.start_state
        return

    def run_with_input_list(self, input_list):
        self.go_to_initial_state()
        for inp in input_list:
            self.transition_to_state_with_input(inp)
            continue
        return self.in_accept_state()

    pass


# def generatenumbers(input):


def Code(n):
    m = 1
    code = ['0', '1']

    #global m
    while (m < n):
        m += 1
        reversed_code = sorted(code, reverse=True)
        for i in range(len(code)):
            code[i] = '0' + code[i]
        for i in range(len(code)):
            reversed_code[i] = '1' + reversed_code[i]
        for j in range(len(reversed_code)):
            code.append(reversed_code[j])

    return code
    # Code(input3), print(code)
states = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
alphabet = {'0', '1'}
tf = dict()
tf[(1, '0')] = 7
tf[(1, '1')] = 6
tf[(2, '0')] = 10
tf[(2, '1')] = 7
tf[(3, '0')] = 4
tf[(3, '1')] = 4
tf[(4, '0')] = 10
tf[(4, '1')] = 1
tf[(5, '0')] = 6
tf[(5, '1')] = 3
tf[(6, '0')] = 6
tf[(6, '1')] = 5
tf[(7, '0')] = 7
tf[(7, '1')] = 10
tf[(8, '0')] = 2
tf[(8, '1')] = 2
tf[(9, '0')] = 9
tf[(9, '1')] = 1
tf[(10, '0')] = 8
tf[(10, '1')] = 4

start_state = 1
accept_states = {5, 6, 7, 8}

generate = Code(int(input("enter input here : ")))
print(generate)

#result = list(map(int ,generate))
#print(result)

applythematrix = DFA(states, generate, tf , start_state, accept_states)
#answer = applythematrix.run_with_input_list(generate)
print(applythematrix.run_with_input_list(generate))

# applying_clas = DFA(states, tf, start_state, accept_states);
# inp_program = list('10101');
# print
# applying_clas.run_with_input_list()
# d.run_with_input_list(inp_program);
#We will refer to the smallest hypothesis DFAfor a Type-3 Grammar(G)as the canonical DFA of(G).