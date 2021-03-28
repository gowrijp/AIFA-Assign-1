# AIFA-Assign-1

To run the program, please use the following steps.

- Install Python 3.6 with pip
- Run `pip3 install -r requirements.txt`
- Run `python run_maze.py`

The layout of the maze is as defined in the file `data/maze_layout.txt` where X denotes the boundaries and blocked cells where the bot cannot move to, and A denotes the initial position of the bots. The initial position of the 4 bots can be changed by editing the `data/maze_layout.txt` file.  


By default the program takes 4 pickup and delivery locations for the bot. Please enter your inputs when prompted.  
       
![Sample Input](https://github.com/gowrijp/AIFA-Assign-1/blob/main/Assets/input-sample.PNG)    

  
The final path taken for each bot is printed on console on successful execution of the algorithm before the start of the visualization.  

A* Search algorithm is one of the most popular and best techniques used in path-finding and graph traversals.Here we used the same to solve this problem using priority queue data structure (heapq).Since we are allowed to move only in four directions only (right, left, top, bottom), we used the Manhattan Distance heuristic which is nothing but the sum of absolute values of differences in the goal’s x and y coordinates and the current cell’s x and y coordinates respectively, i.e.,  

`h = abs (current_cell.x – goal.x) + abs (current_cell.y – goal.y)`  

The allocate function in allocate_targets.py finds the best combination of pickup-delivery for each of the initial position of the bots in the warehouse using the a* algorithm and least time required to reach the targets.  

The ArtistAnimation function from matplotlib library is used to animate the final path of each bot.
