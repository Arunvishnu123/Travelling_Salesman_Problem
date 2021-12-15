from Brute_Force_Algorithm import l_brute_force
from Dynamic_Algorithm import Dynamic_Algo
from Random_TSP_Generator import random_generator
from Greedy_Algorithm import greedy_algo
from Randmized_Algorithm import Randomized_algo
import Branch_And_Bound
import time

if __name__ == '__main__':

 # Randomly generate traveling salesman problem,here 0 stands for city 1 ,1 stand for city 2 like that

 while(True):

  Algo_need_to_run = input(("1. Enter C to generate random tsp problem\n2. Enter B to run Brute Force approach/\n3. Enter R to run Randomized Approach\n4. Enter G to run Greedy Algorithm\n5. Enter BB to run Branch and Bound Algorithm"))

  if(Algo_need_to_run == "C" or Algo_need_to_run == "c"):
      cities_no = int(input(("Enter the city Number")))
      random_tsp_generator = random_generator(cities_no)
      random_tsp = random_tsp_generator.city_value_generation()
      print(random_tsp)

  # Brute Force Algorithm
  if (Algo_need_to_run == "B" or Algo_need_to_run == "b"):
     Brute_Force = l_brute_force(cities_no, random_tsp)
     start_time = time.time()
     Combinations = Brute_Force.calc_cost_eacomb()
     finish_time = time.time()
     duration = finish_time - start_time
     print("Brute Force_Algorithm", Combinations)
     print("time delay in seconds", duration)

  #Dynamic Algorithm
  if (Algo_need_to_run == "D" or Algo_need_to_run == "d"):
      Dynamic = Dynamic_Algo(cities_no,random_tsp)
      start_time = time.time()
      Dynamic_result = Dynamic.calculate_cost()
      finish_time = time.time()
      duration = finish_time - start_time
      print("Dynamic Algorithm", Dynamic_result)
      print("time delay in seconds", duration)

  #  Greedy Algorithm
  if (Algo_need_to_run == "G" or Algo_need_to_run == "g"):
      Greedy = greedy_algo(cities_no, random_tsp)
      start_time = time.time()
      Greedy_result = Greedy.find_lowest_cost()
      finish_time = time.time()
      duration = finish_time - start_time
      print("Greedy Algorithm", Greedy_result)
      print("time delay in seconds", duration)

  # Randimized Algorithm
  if (Algo_need_to_run == "R" or Algo_need_to_run == "r"):
      Randomized = Randomized_algo(cities_no,random_tsp)
      start_time = time.time()
      Randomized_result = Randomized.random_algo()
      finish_time = time.time()
      duration = finish_time - start_time
      print("Randomized Algorithm", Randomized_result)
      print("time delay in seconds", duration)

  # Branch and Bound
  if (Algo_need_to_run == "BB" or Algo_need_to_run == "bb"):
      Branch_And_Bound.N = cities_no
      start_time = time.time()
      Branch_And_Bound.TSP(random_tsp)
      print("Branch and Bound",Branch_And_Bound.final_res,Branch_And_Bound.final_path)
      finish_time = time.time()
      duration = finish_time - start_time
      print("time delay in seconds", duration)







