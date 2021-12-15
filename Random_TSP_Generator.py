import random

class random_generator():

    def __init__(self,cities_no):
        self.cities_no = cities_no

    def city_value_generation(self):
        Main_1 = []
        for i in range(0, self.cities_no):
            Main_2 = []
            for j in range(0, self.cities_no):
                if (i != j):
                    Main_2.append(random.randint(5, (self.cities_no * 50)))
                if (i == j):
                    Main_2.append(0)
            Main_1.append(Main_2)
        return Main_1

