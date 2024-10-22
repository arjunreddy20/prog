class Stack:
    def __init__(self):
        self.sta=[]

    def insert(self,ele):
        self.sta.append(ele)
    def remove(self):
        if self.sta:
            self.sta.pop()
    def is_empty(self):
        if not self.sta:
            return True
        else:
            return False
    def display(self):
        return self.sta
obj=Stack()
obj.insert(1)
obj.insert(2)
obj.insert(15)
print(obj.display())
obj.remove()
obj.insert(105)
obj.insert(121)
print(obj.display())
print(obj.is_empty())