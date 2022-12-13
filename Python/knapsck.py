capacity = 6404180
weight = [382745,
          799601,
          909247,
          729069,
          467902,
          44328,
          34610,
          698150,
          823460,
          903959,
          853665,
          551830,
          610856,
          670702,
          488960,
          951111,
          323046,
          446298,
          931161,
          31385,
          496951,
          264724,
          224916,
          169684]
profit = [825594, 1677009, 1676628, 1523970, 943972, 97426, 69666, 1296457, 1679693, 1902996,
          1844992,
          1049289,
          1252836,
          1319836,
          953277,
          2067538,
          675367,
          853655,
          1826027,
          65731,
          901489,
          577243,
          466257,
          369261]
solution = 110111000110100100000111




# 2
def binary_knapsack(weight, capacity, profit, number):
    # base condition ending if the list or capacity is zero
    if number == 0 or capacity == 0:
        return 0
    # condition removing the values of weight that are exceeds capacity
    elif weight[number - 1] > capacity:
        return binary_knapsack(weight, capacity, profit, number - 1)
    else:
        # recursively taking trying every item
        return max(binary_knapsack(weight, capacity, profit, number - 1),
                   # this one takes the first one that we stop on
                   profit[number - 1] + binary_knapsack(weight, capacity - weight[number - 1], profit, number - 1))

number = len(profit)
print(f"this is the total profit:\n{binary_knapsack(weight, capacity, profit, number)}")


# in the case of two lists it returned the list with the hegihst number
# in case of nested list it returned the height tuble