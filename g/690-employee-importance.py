# https://leetcode.com/problems/employee-importance/
from collections import defaultdict

class Employee:
    def __init__(self, id, importance, subordinates):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

def getImportance(employees, id):
    d = defaultdict()
    for employee in employees:
        d[employee.id] = [employee.subordinates, employee.importance]

    result = d[id][1]
    queue = d[id][0]

    while queue:
        popped = queue.pop()
        elem = d[popped]
        queue.extend(elem[0])
        result += elem[1]

    return result

    



print(getImportance([Employee(1, 5, [2,3]), 
                    Employee(2, 3, []), 
                    Employee(3, 3, [])], 1))