
'''
amy 100
david 100
heraldo 50
aakansha 75
aleksa 150
'''
class Employee(object):
    def __init__(self,name,salary) :
        self.name = name
        self.salary = salary

    def __repr__(self):
        return f'{self.name} {self.salary}'
    def comparators(a,b):
        if a.salary > b.salary:
            return 1
        if a.salary < b.salary:
            return -1
        
employees=[]
for i in range(5):
    name,salary=input("enter name and salary with space : ").split()
    employees.append(Employee(name,salary))
    employees_sorted=sorted(employees, key=lambda emp:emp.salary)

for emp in employees_sorted:
    print(emp)


#Another way




from functools import cmp_to_key
class Player:
    def __init__(self, name, score):
        self.name=name
        self.score=score        
    def __repr__(self):
        return {'name':self.name,'score':self.score}
        
    def comparator(a, b):
        if a.score>b.score:
            return -1
        if a.score<b.score:
            return 1
        if a.name < b.name:
            return -1
        if a.name > b.name:
            return 1
        return 0

n = int(input())
data = []
for i in range(n):
    name, score = input().split()
    score = int(score)
    player = Player(name, score)
    data.append(player)
    
data = sorted(data, key=cmp_to_key(Player.comparator))
for i in data:
    print(i.name, i.score)