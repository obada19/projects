




from array import array
from itertools import repeat
import collections
from random import *

listofprofit = []
listofdeadline = []



def generator():
    for i in range(0, 50):
        n = randint(1, 40)
        s = randint(1, 40)
        listofdeadline.append(n)
        listofprofit.append(s)


#initalizing = generator()
# adding the list in the following order is neccessary in order to use sort built in function on the profit
list_of_lists = [list(joined) for joined in zip(listofprofit, listofdeadline)]
dict_jobs_p_n_d = {}

c = 1

for i in list_of_lists:
    sd = "job"
    sd += str(c)
    dict_jobs_p_n_d.update({sd: i})
    c += 1
# print(f"this is list of job number : [profit , deadline]:\n{dict_jobs_p_n_d}")
sorting = sorted(dict_jobs_p_n_d.items(), key=lambda x: x[1], reverse=True)
sorted_dict = dict(sorting)
dict_to_list = list(sorted_dict.items())

# aquring the highest deadline to use in intiating the list
maxvalue_deadline= max(listofdeadline)

# initiating a list with only None's times the max value in order to use it like an array in other languages
# where we can insert a value directly to a given index
job_sche_max_profit = [None] * (maxvalue_deadline)


def job_scheduling():
    for i in dict_to_list:
        for j in i[1:2]:
            current = j[1]
            current = current-1
            if job_sche_max_profit[current]== None:
               job_sche_max_profit[current] = i
            else:
                while job_sche_max_profit[current]!= None:
                    current -= 1
                    if job_sche_max_profit[current] == None:
                       job_sche_max_profit[current] = i
                       break
                    elif job_sche_max_profit[current] == job_sche_max_profit[0] and job_sche_max_profit[current]!=None:
                        break

def finding_maxmimum_profit(job_sche_max_profit):
    global maximum_profit_sum
    for i in job_sche_max_profit:
        if i != None:
            for k in i[1:2]:
                maximum_profit_sum+= k[0]
       # this is done to skip any none values that can occure
        elif i == None:
            skip = True
            continue

job_scheduling()
maximum_profit_sum = 0
finding_maxmimum_profit(job_sche_max_profit)

print(f"this is the sum of maximum profit:\n{maximum_profit_sum}")
print(f"this is the job scheduling that gives maximum profit:\n{job_sche_max_profit}")









