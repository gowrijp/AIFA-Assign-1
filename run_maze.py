import numpy as np
from termcolor import colored, cprint
import os
import time
import helper_func

from a_star import run_a_star
from allocate_targets import allocate

class Maze():
    def __init__(self, layout, original_layout, agents, targets, delivery):
        self.layout = layout
        self.original_layout = original_layout
        self.agents = agents #agents => initial position of bots
        self.targets = targets #targets => pick-up locations
        self.delivery = delivery #delivery => delivery locations
        #self.end_pos = end_pos

    def print_maze(self, clear=False):
        if clear:
            os.system('cls' if os.name == 'nt' else 'clear')
        for i in range(len(self.layout)):
            for j in range(len(self.layout[0])):
                if self.layout[i][j] == 'X':  # wall
                    cprint('\u2588\u2588', 'grey', end='')
                elif self.layout[i][j] == ' ':    # fresh node
                    cprint('\u2588\u2588', 'white', end='')
                elif self.layout[i][j] == 'S':    # start
                    cprint('\u2588\u2588', 'green', end='')
                elif self.layout[i][j] == 'R':    # end
                    cprint('\u2588\u2588', 'red', end='')
                elif self.layout[i][j] == 'E':    # end
                    cprint('\u2588\u2588', 'red', end='')
                elif self.layout[i][j] == 'O':    # opened
                    cprint('\u2588\u2588', 'yellow', end='')
                elif self.layout[i][j] == 'P':    # path
                    cprint('\u2588\u2588', 'blue', end='')
            print()

    # Blue box moves from start to end denoting the path taken by each bot
    def print_path(self, path):
        path_dict = {}
        for k in range(len(path)):
            path_dict[k] = path[k]
        for value in path_dict.values():
            self.layout[value[1]][value[0]] = 'P'
        self.print_maze()
        for value in path_dict.values():
            self.layout[value[1]][value[0]] = ' '

    def get_neighbours(self, node):
        y, x = node
        neighbours = [(y + 1, x), (y, x + 1), (y-1, x), (y, x - 1), (y, x)]
        return neighbours

def update_constraints(constraints, path):
    path_dict = {}
    for k in range(len(path)):
        path_dict[k] = path[k]
    for key, value in path_dict.items():
        constraints.append((key, value))
    return constraints

def run_solver(maze):
    paths = allocate(maze)
    sorted_paths = sorted(paths, key=lambda path: len(path), reverse=True)
    priority_path = sorted_paths.pop(0)
    constraints = []

    constraints = update_constraints(constraints, priority_path)

    final_paths = []
    final_paths.append(priority_path)

    for path in sorted_paths:
        lock = False
        for key, value in path.items():
            if (key, value) in constraints:
                lock = True
                break
        if lock:
            paa = run_a_star(maze, maze.original_layout, path.get(0), list(path.values())[-1],put_on_a_show=False, constraints=constraints)
            pa_dict = {}
            for k in range(len(paa)):
                pa_dict[k] = paa[k]
            final_paths.append(pa_dict)
            constraints = update_constraints(constraints, path)
        else:
            final_paths.append(path)

    print('Final paths: ')
    for path in final_paths:
        print(path)

    helper_func.plot_paths(maze.original_layout, final_paths)


def Main():
    layout = open('data/maze_layout.txt', 'r')
    maze, agents, targets, delivery = helper_func.process_layout(layout)
    maze = Maze(maze, maze, agents, targets, delivery)

    run_solver(maze)

Main()
