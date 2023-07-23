from heapq import heapify,heappop,heappush

class heapqueue():
    def __init__(self):
        self.heap=[]

    def insertQueue(self,k):
        heappush(self.heap,k)

    def printheap(self):
        print(self.heap)




obj=heapqueue()
obj.insertQueue(1)
obj.insertQueue(5)
obj.insertQueue(3)
obj.insertQueue(4)
obj.insertQueue(2)
obj.insertQueue(2)
obj.insertQueue(4)


obj.printheap()
