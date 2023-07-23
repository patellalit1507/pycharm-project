class Bird:
    def intro(self):
        print("we comes unnder cateogary of birds ")

    def flight(self):
        print("all birds can fly")

class sparrow(Bird):
    def flight(self):
        print("i can fly ")
class ostrich(Bird):
    def flight(self):
        print("i cant fly")

obj_bird=Bird()
obj_sparrow=sparrow()
obj_ostrich=ostrich()

obj_bird.intro()
obj_bird.flight()

obj_sparrow.intro()
obj_sparrow.flight()

obj_ostrich.intro()
obj_ostrich.flight()
