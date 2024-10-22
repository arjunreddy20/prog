class Queue:
    def __init__(self):
        self.q=[]
        self.front= -1
        self.rear= -1
        
    def Enqueue(self,ele):
        if self.front==-1 :
            self.front+=1
        else:
            self.rear+=1
        self.q.append(ele)
        
    def Dequeue(self):
        if not self.q:
            print("it is empty")

        else:    
            if self.front > self.rear:
                self.front,self.rear=-1,-1            
            self.q.pop(0)
            self.rear-=1
            
    def is_empty(self):
        print(self.front==self.rear==-1)#not empty
        
    def get_first_element(self):
        if self.q:
            print(self.q[0])
    
obj=Queue()
obj.Enqueue(1)
obj.Enqueue(10)
obj.Enqueue(20)
obj.Enqueue(35)
obj.Enqueue(95)
obj.Enqueue(46)
print(obj.q)
obj.Dequeue()
obj.Dequeue()
obj.Dequeue()
obj.Dequeue()
obj.Dequeue()
obj.Dequeue()
obj.Dequeue()

print(obj.q)
obj.is_empty()
obj.get_first_element()
