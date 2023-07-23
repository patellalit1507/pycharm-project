class node():
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedlist():
    def __init__(self):
        self.head=None

    def printlist(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next

    def push(self,add_data):
        new_node=node(add_data)
        new_node.next=self.head
        self.head=new_node

    def insert_after(self,previous_node,new_data):
        if previous_node==None:
            print("must lie within list")
        new_node=node(new_data)
        new_node.next=previous_node.next
        previous_node.next=new_node
    def Add_last(self,new_data):
        temp=self.head
        new_node=node(new_data)


        if self.head==None:
            self.head=new_node


        while(temp.next!=None):
            temp=temp.next
        temp.next=new_node

    def Delete_ll(self,key):
        temp=self.head
        if(temp is not None):
            if(temp.data==key):
                self.head=temp.next
                temp=None
                return
        while(temp!=None):
            if(temp.data==key):
                break
            prev=temp
            temp=temp.next

        if(temp==None):
           return
        prev.next=temp.next








llist=linkedlist()
llist.head=node(1)
second=node(2)
third=node(5)
tale=node(3)

llist.head.next=second
second.next=third
third.next=tale
#llist.printlist()
llist.push(12)
#llist.printlist()
llist.insert_after(second,20)
#llist.printlist()
llist.Add_last(7)
llist.Delete_ll(20)
llist.Add_last(20)
llist.printlist()
