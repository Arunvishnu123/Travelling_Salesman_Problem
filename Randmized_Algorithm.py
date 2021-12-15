import numpy as np

class Randomized_algo():

    def __init__(self,cities_no,data):
        self.data =data
        self.cities_no =cities_no

    def random_algo(self):
        data = np.array(self.data)

        # iteration = 20000
        iteration = int(input("Please enter the number of iterations to execute random approach:  "))

        def path_distance(route, data):
            li = []
            for i in range(0, self.cities_no):
                val = data[route[i]][route[i + 1]]
                li.append(val)
            cost = sum(li)
            return  cost

        rout = np.arange(data.shape[0])
        route = np.append(rout, 0)
        best_distance = path_distance(route, data)

        last_route = list(route)
        first_route = list(route)

        for i in range(iteration):
            np.random.shuffle(route[1:self.cities_no])
            test_route = route
            new_distance = path_distance(test_route, data)
            if new_distance < best_distance:
                last_route = list(test_route)
                best_distance = new_distance
        return best_distance,last_route
