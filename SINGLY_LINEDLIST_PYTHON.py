class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linked_list:
    def __init__(self):
        self.head=None
    def insert(self,data):
        new_node=node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.next!=None:
                n=n.next
            n.next=new_node
    def display(self):
        if self.head==None:
            print('list is emptry\n')
        else:
            print('printing elements in the list')
            n=self.head
            while n!=None:
                print(n.data,'',end='')
                n=n.next
    def drop(self):
        if self.head==None:
            print('\n list is empty deletion ot possible')
        else:
            print('\ndeleting element in the list\n')
            n=self.head
            while n.next.next!=None:
                n=n.next
            print('element deleted-->:',n.next.data)
            n.next=None
        print('')
    def find(self,key):
        if self.head==None:
            print('\n list is empty...element not found')
        else:
            n=self.head
            while n.next!=None:
                if n.data==key:
                    print('element is found',n.data)
                    return
                n=n.next
        print('element is not found')


ob=linked_list()
l=[10,20,30,40,50,60,70,80,90]
for ele in l:
    ob.insert(ele)
print('\n')
ob.display()
ob.drop()
ob.find(60)
ob.display()
