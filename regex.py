import re
str_list=[]
num_list=[]
with open("regex_sum_1958296.txt") as file:
    for line in file:
        line=line.rstrip()
        str_list+=re.findall("[0-9]+", line)
        if len(str_list)==0:
            continue
    for i in str_list:
        num_list.append(int(i))
    print(sum(num_list))
        
    