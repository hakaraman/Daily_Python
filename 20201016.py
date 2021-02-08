"""
We're given a hashmap associating each courseId key with a list of courseIds values, which represents that the prerequisites of courseId are courseIds. Return a sorted ordering of courses such that we can finish all courses.

Return null if there is no such ordering.

For example, given {'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []}, should return ['CSC100', 'CSC200', 'CSCS300'].
"""



def courses_to_take(course_to_prereqs):
    # Copy list values into a set for faster removal.
    course_to_prereqs = {c: set(p) for c, p in course_to_prereqs.items()}

    todo = [c for c, p in course_to_prereqs.items() if not p]

    # Used to find courses D which have C as a prerequiste
    prereq_to_coures = {}
    for course in course_to_prereqs:
        for prereq in course_to_prereqs[course]:
            if prereq not in prereq_to_coures:
                prereq_to_coures[prereq] = []

            prereq_to_coures[prereq].append(course)

    result = [] # courses we need to take in order

    while todo:
        prereq = todo.pop()
        result.append(prereq)

        # Find which courses are now free to take

        for c in prereq_to_coures.get(prereq, []):
            course_to_prereqs[c].remove(prereq)
            if not course_to_prereqs[c]:
                todo.append(c)

    # Cicrcular dependency
    if len(result) < len(course_to_prereqs):
        return None
    return result


def ordered_courses(courses):
    c = courses.copy()
    result = []
    while [] in c.values():
        noreq = [k for k,v in c.items() if v == []]
        for i in noreq:        
            result.append(i)
            del c[i]
            c = {k1:[v2 for v2 in v1 if v2 != i] for k1,v1 in c.items()}
    return result if len(c) == 0 else None

def ordered_courses1(courses):
    c = courses.copy()
    result = []
    while [] in c.values():
        noreq = [k for k,v in c.items() if v == []]
        for i in noreq:        
            result.append(i)
            del c[i]
            for k,v in c.items():
                if i in v:
                    v.remove(i)
                    c[k] = v
    return result if len(c) == 0 else None

course = {'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': [], 'CSC400': ['CSC100', 'CSC300'], 'CSC500': ['CSC400']}

print(courses_to_take(course))
print(ordered_courses(course))
print(ordered_courses1(course))

answer=[]
for i in range(len(course.keys())):
    for j in course.keys():
        answer.append(j) if ((course[j]==answer or len(course[j])<=len(answer)) and j not in answer) else answer
print(answer)