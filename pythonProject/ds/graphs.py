class graphs():
    def __init__(self,edges):
        self.edges=edges
        self.graph_dict={}

        for start,end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start]=[end]

        print(self.graph_dict)

    def find_paths(self,start,end,path=[]):
        path=path+[start]
        print(path)
        if start==end:
            return [path]
        if start not in self.graph_dict:
            return []

        paths=[]

        for node in self.graph_dict[start]:
            if node not in path:
               new_path=self.find_paths(node,end,path)
               for p in new_path:
                  #print(p)
                  paths.append(p)





        return paths







        




if __name__ == '__main__':
    routes=[
        ("mumbai","paris"),
        ("mumbai","dubai"),
        ('mumbai','tornto'),
        ("paris","dubai"),
        ("paris","new_york"),
        #('paris','california'),
        ("dubai","new_york"),
        ("dubai","paris"),
        ("new_york","tornto")
    ]
    d={
        "mumbai":["paris","dubai"]
    }
    k=graphs(routes)
    name=['mubai",new_york']
    print(k.find_paths("mumbai","tornto"))
   # k.find_paths(name)
