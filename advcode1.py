import os
dir_path = os.path.dirname(os.path.realpath(__file__))
lst = []
# PART-1
with open(dir_path+'/expense.txt','r') as f:
    lines = f.readlines()
    for i in range(len(lines)):
        for j in range(i+1,len(lines)):
            if int(lines[i]) + int(lines[j]) == 2020:
                print(int(lines[i]),int(lines[j]),int(lines[i]) * int(lines[j]))
                
# PART-2
with open(dir_path+'/expense.txt','r') as f:
    lines = f.readlines()
    for i in range(len(lines)):
        for j in range(i+1,len(lines)):
            for k in range(i+1,len(lines)):
                if int(lines[i]) + int(lines[j]) + int(lines[k]) == 2020:
                    print(int(lines[i]),int(lines[j]),int(lines[k]),int(lines[i]) * int(lines[j]) * int(lines[k]))
