# MRO Genetics Exercise

# This exercise illustrates the concept of multiple inheritance. A child class called Child inherits the attributes of the Mother and Father classes, in that order

class Mother():
        def __init__(self):
                self.eye_color = "brown"
                self.hair_color = "dark brown"
                self.hair_type = "curly"

class Father():
        def __init__(self):
                self.eye_color = "blue"
                self.hair_color = "blond"
                self.hair_type = "straight"

class Child(Mother, Father):
        def __init__(self):
                Mother.__init__(self)
                Father.__init__(self)


mike = Child()
print(mike.eye_color)
print(mike.hair_color)
print(mike.hair_type)
