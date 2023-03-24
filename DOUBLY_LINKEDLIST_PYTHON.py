class node:
    def __init__(self,data):
        self.prev=None
        self.next=None
        self.data=data
class dll:
    def __init__(self):
        self.head=None

    def insert(self,data):
        new_node=node(data)

        if self.head==None:
            self.head=new_node
        else:
            n=self.head
            while n.next!=None:
                n=n.next
            new_node.prev=n
            n.next=new_node


    def display(self):
        if self.head==None:
            print('list is empty')
        else:
            n=self.head
            while n.next!=None:
                print(n.data,'',end='')
                n=n.next
            print(n.data)
        print('\nprinting elements in reverse order')
        while n.prev!=None:
            print(n.data,'',end='')
            n=n.prev
        print(n.data)
ob=dll()
l=[10,20,30,40,50,60,70,80,90]
for ele in l:
    ob.insert(ele)

ob.display()
