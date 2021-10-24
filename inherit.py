class Feature:
    def feature1(self):
        print("Human has 2 eyes and 1 nose")
        print("And he has 2 ears")


class Human(Feature):
    def feature2(self):
        print("And also human has a mouth")


human_being=Human()
human_being.feature1()
human_being.feature2()