class treenode():
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None

    def add_node(self,child):
        child.parent=self
        self.children.append(child)

    def get_level(self):
        level=0
        p=self.parent
        while p:
            level+=1
            p=p.parent
        return level

    def print_tree(self):
        print(" "*self.get_level()+"|-"+self.data)
        if self.children:
           for child in self.children:
             child.print_tree()




def build_product_tree():
    root=treenode("electronics")
    laptop=treenode("laptop")
    root.add_node(laptop)
    laptop.add_node(treenode("mac"))
    laptop.add_node(treenode("surface"))
    laptop.add_node(treenode("thinkpad"))

    mobile=treenode("mobile")
    root.add_node(mobile)
    mobile.add_node(treenode("iphone"))
    mobile.add_node(treenode("google"))
    mobile.add_node(treenode("vivo"))

    tablet=treenode('tv')
    root.add_node(tablet)
    tablet.add_node(treenode("samsung"))
    tablet.add_node(treenode("l G"))


    return root





if __name__ == '__main__':
    root=build_product_tree()
    root.print_tree()
