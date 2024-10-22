class count_object:
    count=0
    def __init__(self):
        count_object.count+=1
    def display(self):
        print(count_object.count)
def main():
    a=count_object()
    b=count_object()
    c=count_object()
    count_object.display(count_object)
main()


class count_object:
    count=0
    def __init__(self) -> None:
        count_object.count+=1
    @classmethod
    def display(cls):
        print(count_object.count)  #in place of count_object.count we can use cls.count
def main():
    a=count_object()
    b=count_object()
    c=count_object()
    count_object.display()
main()