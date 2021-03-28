from a_star import run_a_star
import numpy as np
import time
from helper_func import plot_paths
from itertools import permutations

class Rated_combination():
    def __init__(self, pathway, rating):
        self.pathway = pathway
        self.rating = rating

def rate_pathway(pathway, distance_table):
    distance = 0
    for combination in pathway:
        distance += distance_table[combination[0]][combination[1]]
    return distance

def find_combination(distance_table):
    agents_vec = []
    for k in range(len(distance_table)):
        agents_vec.append(k)

    combinations = []
    targets_perms = permutations(agents_vec)
    for perm in targets_perms:
        combinations.append(zip(agents_vec, perm))

    rated_combinations = []
    for i in range(len(combinations)):
        pathway = []
        for j in combinations[i]:
            pathway.append(j)
        rated_comb = Rated_combination(
            pathway=pathway, rating=rate_pathway(pathway, distance_table))
        rated_combinations.append(rated_comb)

    return rated_combinations

# return smallest overall distance travelled by agents
def sort_by_overall_dist(rated_combinations):
    rated_combinations = sorted(
        rated_combinations, key=lambda x: x.rating, reverse=False)
    return rated_combinations


def allocate(maze):
    distance_table = [[0 for x in range(len(maze.targets))]
                      for y in range(len(maze.agents))]
    path_table = [[0 for x in range(len(maze.targets))]
                  for y in range(len(maze.agents))]

    for i in range(len(maze.agents)):
        for j in range(len(maze.targets)):
            maze.layout = maze.original_layout
            path = run_a_star(maze, maze.original_layout, maze.agents[i], maze.targets[j], put_on_a_show=True, constraints=None)
            path2 = run_a_star(maze, maze.original_layout, maze.targets[j], maze.delivery[j], put_on_a_show=True, constraints=None)
            path_f = path + path2
            path_dict = {}
            for k in range(len(path_f)):
                path_dict[k] = path_f[k]

            distance_table[i][j] = len(path_f)
            path_table[i][j] = path_dict

    sorted_combs = sort_by_overall_dist(find_combination(distance_table))
    best_solution = sorted_combs[0]

    paths = []
    for path in best_solution.pathway:
        paths.append(path_table[path[0]][path[1]])

    return paths
