import itertools

class Dynamic_Algo():

    def __init__(self,cities_no,data):
        self.data = data
        self.cities_no = cities_no

    def solve_tsp_dynamic(self):

        cities_a = {(frozenset([0, idx + 1]), idx + 1): (dist, [0, idx + 1]) for idx, dist in
                    enumerate(self.data[0][1:])}
        for m in range(2, len(self.data)):
            cities_b = {}
            for cities_set in [frozenset(C) | {0} for C in itertools.combinations(range(1, len(self.data)), m)]:
                for j in cities_set - {0}:
                    cities_b[(cities_set, j)] = min([(cities_a[(cities_set - {j}, k)][0] + self.data[k][j],
                                                      cities_a[(cities_set - {j}, k)][1] + [j])
                                                     for k in cities_set if k != 0 and k != j])
            cities_a = cities_b
        res = min([(cities_a[d][0] + self.data[0][d[1]], cities_a[d][1]) for d in iter(cities_a)])
        return res[1]

    def calculate_cost(self):
        li = []
        comb = self.solve_tsp_dynamic()
        comb.append(0)
        for i in range(0, self.cities_no):
            val = self.data[comb[i]][comb[i + 1]]
            li.append(val)
        cost = sum(li)
        return comb, cost

