import os
dir_path = os.path.dirname(os.path.realpath(__file__))
count = 0
# PART-1
# with open(dir_path+'/passwords.txt','r') as f:
#     lines = f.readlines()
#     for i in lines:
#         item = i.split()
#         limits = item[0].split("-")
#         x = item[2].count(item[1][0])
#         if int(limits[0]) <= x <= int(limits[1]):
#             count += 1
# PART-2
with open(dir_path+'/passwords.txt','r') as f:
    lines = f.readlines()
    for i in lines:
        item = i.split()
        limits = item[0].split("-")
        x = int(limits[0])-1
        y = int(limits[1])-1
        cx = ""
        if len(item[2]) > x:
            cx = item[2][x]  
        cy = ""    
        if len(item[2]) > y:
            cy = item[2][y]

        if not (cx == cy == item[1][0]) and  ((cx == item[1][0]) or (cy == item[1][0])):
            count += 1
print(count)            
