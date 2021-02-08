"""
Given an unordered list of flights taken by someone, each represented as (origin, destination) pairs, and a starting airport, compute the person's itinerary. If no such itinerary exists, return null. If there are multiple possible itineraries, return the lexicographically smallest one. All flights must be used in the itinerary.

For example, given the list of flights [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')] and starting airport 'YUL', you should return the list ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'].

Given the list of flights [('SFO', 'COM'), ('COM', 'YYZ')] and starting airport 'COM', you should return null.

Given the list of flights [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')] and starting airport 'A', you should return the list ['A', 'B', 'C', 'A', 'C'] even though ['A', 'C', 'A', 'B', 'C'] is also a valid itinerary. However, the first one is lexicographically smaller.
"""
def compute_itenary(lst, start):
    def next_itenary(path, start, lst):
        if (len(lst) == 0):
            itenaries.append(path+'@'+start)
            return
  
        for i in range(len(lst)):
            if start == lst[i][0]:
                next_itenary(path + '@' + lst[i][0], lst[i][1], lst[:i]+lst[i+1:])
    itenaries = [] 
    for i in range(len(lst)):
        if lst[i][0] == start:
            next_itenary(lst[i][0], lst[i][1], lst[:i]+lst[i+1:])
    return sorted([i.split('@') for i in itenaries])[0] if itenaries else None

def compute_itenary1(lst):
    lst = [tuple(i) for i in lst]
    r = [[i] for i in lst if i[0] == "JFK"]
    for _ in range(len(lst)-1):
        temp = []
        for i in r:
            for j in lst: 
                if (j not in i) and (i[-1][1] == j[0]):
                    temp.append(i + [j])
        r = temp
    r = sorted(r)[0]
    return [i[0] for i in r] + [r[-1][1]] if r else None

def compute_itenary2(lst, start):
    r = [[i] for i in lst if i[0] == start]
    for _ in range(len(lst)-1):
        r = [i + [j] for i in r for j in lst if (j not in i) and (i[-1][1] == j[0])]
    r = sorted(r)[0]
    return [i[0] for i in r] + [r[-1][1]] if r else None

def compute_itenary3(lst, start):
    r = [[i] for i in lst if i[0] == start]
    for _ in range(len(lst)-1):
        r = [i + [j] for i in r for j in lst if (lst.count(j) != i.count(j)) and (i[-1][1] == j[0])]
    r.sort()
    return [i[0] for i in r[0]] + [r[0][-1][1]] if r else None

from collections import defaultdict

def findItinerary(tickets):
        
    if not tickets: return []
    
    graph = defaultdict(list)
    
    for ticket in tickets:
        t1 = ticket[0]
        t2 = ticket[1]
        graph[t1].append(t2)
        if t2 not in graph:
            graph[t2] = []
    
    for v in graph.values():
        v = v.sort(reverse=True)
    
    # use stack to evaluate
    stack = []
    stack.append('JFK')
    
    output = []
    while stack:
        curr = stack[-1]
        # print('curr',curr,'stack',stack,'graph',graph[curr])
        if len(graph[curr]) == 0:
            
            output.append(stack.pop())
        else:
            nbr = graph[curr].pop()
            stack.append(nbr)
    # print(output)
    return output[::-1]

def itinerary(flights, myItinerary):
    if isinstance(myItinerary, str):
        myItinerary = list(myItinerary)
    if not flights:
        return myItinerary
    last_destination = myItinerary[-1]
    for i, (first, destination) in enumerate(flights):
        flights_updated = flights[:i] + flights[i + 1:]
        myItinerary.append(destination)
        if first == last_destination:
            return itinerary(flights_updated, myItinerary)
        myItinerary.pop()
    return None 

lst = [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')]
#lst = [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')]
#lst = [["EZE","AXA"],["TIA","ANU"],["ANU","JFK"],["JFK","ANU"],["ANU","EZE"],["TIA","ANU"],["AXA","TIA"],["TIA","JFK"],["ANU","TIA"],["JFK","TIA"]]
lst = [["AXA","EZE"],["EZE","AUA"],["ADL","JFK"],["ADL","TIA"],["AUA","AXA"],["EZE","TIA"],["EZE","TIA"],["AXA","EZE"],["EZE","ADL"],["ANU","EZE"],["TIA","EZE"],["JFK","ADL"],["AUA","JFK"],["JFK","EZE"],["EZE","ANU"],["ADL","AUA"],["ANU","AXA"],["AXA","ADL"],["AUA","JFK"],["EZE","ADL"],["ANU","TIA"],["AUA","JFK"],["TIA","JFK"],["EZE","AUA"],["AXA","EZE"],["AUA","ANU"],["ADL","AXA"],["EZE","ADL"],["AUA","ANU"],["AXA","EZE"],["TIA","AUA"],["AXA","EZE"],["AUA","SYD"],["ADL","JFK"],["EZE","AUA"],["ADL","ANU"],["AUA","TIA"],["ADL","EZE"],["TIA","JFK"],["AXA","ANU"],["JFK","AXA"],["JFK","ADL"],["ADL","EZE"],["AXA","TIA"],["JFK","AUA"],["ADL","EZE"],["JFK","ADL"],["ADL","AXA"],["TIA","AUA"],["AXA","JFK"],["ADL","AUA"],["TIA","JFK"],["JFK","ADL"],["JFK","ADL"],["ANU","AXA"],["TIA","AXA"],["EZE","JFK"],["EZE","AXA"],["ADL","TIA"],["JFK","AUA"],["TIA","EZE"],["EZE","ADL"],["JFK","ANU"],["TIA","AUA"],["EZE","ADL"],["ADL","JFK"],["ANU","AXA"],["AUA","AXA"],["ANU","EZE"],["ADL","AXA"],["ANU","AXA"],["TIA","ADL"],["JFK","ADL"],["JFK","TIA"],["AUA","ADL"],["AUA","TIA"],["TIA","JFK"],["EZE","JFK"],["AUA","ADL"],["ADL","AUA"],["EZE","ANU"],["ADL","ANU"],["AUA","AXA"],["AXA","TIA"],["AXA","TIA"],["ADL","AXA"],["EZE","AXA"],["AXA","JFK"],["JFK","AUA"],["ANU","ADL"],["AXA","TIA"],["ANU","AUA"],["JFK","EZE"],["AXA","ADL"],["TIA","EZE"],["JFK","AXA"],["AXA","ADL"],["EZE","AUA"],["AXA","ANU"],["ADL","EZE"],["AUA","EZE"]]
x = findItinerary(lst)
print(len(x), x)
print(compute_itenary(lst,lst[0][0]))
#print(compute_itenary3(lst,lst[0][0]))
#print(itinerary(lst,['','JFK']))