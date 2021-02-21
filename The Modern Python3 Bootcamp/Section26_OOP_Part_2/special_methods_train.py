# Special Methods Train exercise

# Define the Train class

class Train():

        # Intansiate the class and assign the number of cars
        def __init__(self, cars):
                self.num_cars = cars

        # Create a __repr__ method that states the number of cars in the train
        def __repr__(self):
                # return f"{self.cars} car train"
                return "{} car train".format(self.num_cars)

        # Create/modify the __len__ method to report the length of the train
        def __len__(self):
                return self.num_cars

t = Train(15)
print(t)
print(len(t))