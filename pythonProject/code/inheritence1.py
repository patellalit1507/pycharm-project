class A:
    def __init__(self,name="rahul"):
        self.name=name
class B(A):
    def __init__(self,roll):
        self.roll=roll
        A.__init__(self)
object=B(23)
print(object.name)