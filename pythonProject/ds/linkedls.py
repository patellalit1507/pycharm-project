class Node():
    def __init__(self,key):
        self.data=key
        self.next=None



class Linked_list():
    def __init__(self):
        self.head=None

    def Print_list(self):
        temp=self.head
        while(temp!=None):
            print(temp.data)
            temp=temp.next

    def Delete_Node(self,position):
        temp=self.head
        if(position==0):
            self.head=temp.next
            temp=0
            return
        for i in range(position):
            prev=temp
            temp=temp.next
        prev.next=temp.next


llist=Linked_list()
llist.head=Node(1)
second=Node(2)
third=Node(3)
tail=Node(4)

llist.head.next=second
second.next=third
third.next=tail
llist.Print_list()
llist.Delete_Node(2)
llist.Print_list()



