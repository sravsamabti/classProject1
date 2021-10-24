class Person:
    def __init__(self,name ):
        self.name=name

    def talk(self):
        print(f"Hi! Iam {self.name}")


person1=Person("sravani")
person1.talk()
person2=Person("Lakshmi")
person2.talk()
person3=Person("Nalluri")
person3.talk()