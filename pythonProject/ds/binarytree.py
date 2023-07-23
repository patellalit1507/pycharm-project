class BinarySearchtreenode():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None



    def add_child(self,entry):
         if self.data==entry:
             return

         if self.data>entry:
             if self.left:
                self.left.add_child(entry)
             else:
                 self.left=BinarySearchtreenode(entry)

         else:
             if self.right:
                 self.right.add_child(entry)
             else:
                 self.right=BinarySearchtreenode(entry)

    def in_order_traversal(self):
        elements=[]
        if self.left:
            elements += self.left.in_order_traversal()
        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()
        return elements

    def Search_num(self,num):
        if num==self.data:
           return self

        if num>self.data:
            if self.right:
               #print("right")
               return self.right.Search_num(num)

            else:
                return False

        if num<self.data:
            if self.left:
              # print("left")
               return self.left.Search_num(num)

            else:
                return False
    def find_min(self):
        if self.left:
            return self.left.find_min()
        else:
            return self.data

    def find_max(self):
        if self.right:
            return self.right.find_max()
        else:
            return self.data

    def Remove_ele(self,num):
        if num<self.data:
            return self.left.Remove_num(num)
        elif n>self.data:
            return self.right.Remove_num(num)

        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

def create_list(list):
      root=BinarySearchtreenode(list[0])
      for i in range(1,len(list)):
          root.add_child(list[i])
      print(root.in_order_traversal())
      return root


if __name__ == '__main__':
    list=[3,4,4,34,55,233,222,34,34,44,2,43,23,23,44,33]
    numbers_tree=create_list(list)
   # numbers_tree.Search_num(222)
    #print(numbers_tree.find_min())
   # print(numbers_tree.find_max())
    n=int(input("enter no to remove: "))
    numbers_tree.Remove_ele(n)
    print(numbers_tree.in_order_traversal())











