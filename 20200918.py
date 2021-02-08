def find_req_room2(lst):
    lst.sort()
    rooms = [[lst[0]]]
    for i in range(1,len(lst)):
        available = []
        for j in rooms:
            if (lst[i][0] in range(j[0],j[1])) or (lst[i][1] in range(j[0],j[1])):
                available.append(False)
            else:
                available.append(True)               
    return lst

def max_overlapping(intervals):
    starts = sorted(start for start, end in intervals)
    ends = sorted(end for start, end in intervals)
    current_max = 0
    current_overlap = 0
    i, j = 0, 0
    while i < len(intervals) and j < len(intervals):
        if starts[i] < ends[j]:
            current_overlap += 1
            current_max = max(current_max, current_overlap)
            i += 1
        else:
            current_overlap -= 1
            j += 1
    return current_max

def max_overlapping3(lst):
    lst.sort()
    maxrooms = 1
    for i in range(len(lst)-1):
        rooms = 1
        for j in range(i+1,len(lst)):
            if (lst[i][0] in range(lst[j][0],lst[j][1])) or (lst[i][1] in range(lst[j][0],lst[j][1])):
                rooms += 1
        if rooms > maxrooms:
            maxrooms = rooms
    return maxrooms

def max_overlapping2(lst):
    #lst.sort()
    maxrooms = 1
    for i in range(len(lst)-1):
        overlap_left, overlap_right = 1 , 1
        for j in range(i+1,len(lst)):
            if (lst[i][0] in range(lst[j][0],lst[j][1])):
                overlap_left += 1
            if (lst[i][1] in range(lst[j][0],lst[j][1])):
                overlap_right += 1
        if max(overlap_left, overlap_right) > maxrooms:
            maxrooms = max(overlap_left, overlap_right)
    return maxrooms    

lst = [[(30, 75), (0, 50), (60, 150) ,(70,100)], 
       [(30, 75), (30, 45)],
       [(30, 35)],
       [(0,110), (20,120), (30,50), (40,70), (60,80), (90,130), (100,140)]]
for i in lst:       
    print(max_overlapping(i))
    print(max_overlapping3(i))