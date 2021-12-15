import math

class greedy_algo():

    def __init__(self,cities_no,data):
        self.cities_no = cities_no
        self.data = data

    def new_list(self):
        li = []
        for i in range(0, self.cities_no):
            li.append(self.data[i][0])
        return li

    def matrix_gen(self):
        matrix = self.data
        infi = math.inf
        for i in range(0, self.cities_no):
            for j in range(0, self.cities_no):
                if (i == j):
                    matrix[i][j] = infi
                if (j == 0):
                    matrix[i][j] = infi
        return matrix

    def find_lowest_cost(self):
        cities =self.cities_no
        main_matrix = self.new_list()
        matrix = self.matrix_gen()
        infi = math.inf
        cost_li = []
        com_li = []
        min_value = min(matrix[0])
        min_index = matrix[0].index(min(matrix[0]))
        for j in range(0, cities):
            matrix[j][min_index] = infi
        cost_li.append(min_value)
        com_li.append(min_index)
        for i in range(0, cities - 2):
            min_cost = min(matrix[com_li[i]])
            cost_li.append(min_cost)
            index_1 = matrix[com_li[i]].index(min(matrix[com_li[i]]))
            com_li.append(index_1)
            for j in range(0, cities):
                matrix[j][index_1] = infi
        cost_li.append(main_matrix[com_li[cities - 2]])
        total_cost = sum(cost_li)
        com_li.insert(0,0)
        com_li.append(0)
        return (total_cost, com_li)