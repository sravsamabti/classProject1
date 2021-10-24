class Person:
    def __init__(self,name ):
        self.name=name

    def speak(self):
        print(f"Hi! Iam {self.name}")


person1=Person("sravani")
person1.speak()
person2=Person("Lakshmi")
person2.speak()
person3=Person("Nalluri")
person3.speak()