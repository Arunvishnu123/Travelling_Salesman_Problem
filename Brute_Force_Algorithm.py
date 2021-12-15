from itertools import permutations


class l_brute_force:

    def __init__(self, no_cities,data):
        self.no_cities = no_cities
        self.data = data
        self.graph = {}
        self.city_str = self.city_str_c()

    # create the city pairs

    def city_str_c(self):
        str = "0123456789"
        city_comb = str[:self.no_cities]
        return city_comb

    def read_cities(self):
        return self.data
    # create the total combinations according to the no_cites.
    # for all combnations the first and last city is "City A"

    def find_combinations(self):
        comb_pat = []
        total_comb = permutations(list(self.city_str[1:]))
        for i in list(total_comb):
            comb_pat.append(list(i))
            comb_pat[len(comb_pat) - 1].insert(0, "0")
            comb_pat[len(comb_pat) - 1].insert(self.no_cities, "0")
        return comb_pat

    def switch(self, index):
        city_index_no = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "10": 10
        }
        return city_index_no.get(index)

    def calc_cost_eacomb(self):
        empty_li = []
        for cal in range(0, len(self.find_combinations())):
            empty_inside_li = []
            # print(self.read_cities())
            for cal2 in range(0, self.no_cities, 1):
                val1 = self.read_cities()[self.switch(self.find_combinations()[cal][cal2])][self.switch(self.find_combinations()[cal][cal2 + 1])]
                empty_inside_li.append(val1)
            empty_li.append(sum(empty_inside_li))
            check = empty_li.index(min(empty_li))
            min_Cost = min(empty_li)
            str11 = self.find_combinations()[check]
        return str11, min_Cost
