from typing import List
import sys
import water_gui

list_pos = []

def manhattan_distance(currentpos: List[int], goal: List[int]) -> int:
    return abs(currentpos[0] - goal[0]) + abs(currentpos[1] - goal[1])

def astar_search(grid, start, goal, heuristic=manhattan_distance, cost=1):
    """
    :param grid: 2D matrix, with the obstacles marked as '1', rest as '0'
    :param start: [x, y] list of initial position
    :param goal: [x, y] list of goal position
    :param heuristic: default to manhattan distance heuristic function
    :param cost: cost of moving one position in the grid, defaults to 1
    :return: minDict: Dictionary of f, g, h and current position (the goal state)
    :return: expanded: 2D matrix of same size as grid, for each element, the count when it was expanded or -1 if
             the element was never expanded.
    """
    global list_pos
    # list to hold the all possible best paths
    path = []
    iteration = 1 # to show at what point each path was expanded

    # don't go expand the same position twice, use a set to hold previously visited locations
    visited = set()
    visited.add(tuple(start))

    # 2D grid to show paths expanded
    x = start[0]
    y = start[1]
    expanded = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    expanded[x][y] = 0

    # f, g, and h to calculate which paths to expand
    g = 0
    h = heuristic([x, y], goal)
    f = g + h
    minDict = {
        'f': f,
        'g': g,
        'h': h,
        'currentpos': [x, y]
    }

    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]] # 4 directions: right, left, down, up
    while minDict['currentpos'] != goal:
        for row in expanded: # see where we have expanded on each iteration
            print(row)
        print(minDict) # see the current f, g, h and position on each iteration
        print()
        for dx, dy in directions: # check all four directions
            x2 = x + dx
            y2 = y + dy
            # check that we are in the bounds of the 2D grid
            if x2 in range(len(grid)) and y2 in range(len(grid[0])):
                # check that we have not expanded that location before, and we can go to that location (there is a 0 there)
                if (x2, y2) not in visited and grid[x2][y2] == 0:
                    # update the costs
                    g2 = g + cost
                    h2 = heuristic([x2, y2], goal)
                    f2 = g2 + h2
                    path.append([f2, g2, h2, [x2, y2]])
                    visited.add((x2, y2)) # add current position to visited set

        if not path: # if nothing was appended to the path, it is not possible to go there
            print('NO PATH POSSIBLE')
            exit(1)

        # minList is min of path to find the best path to take of the 4 directions checked
        minList = min(path)
        # update the minDict
        minDict['f'], minDict['g'], minDict['h'], minDict['currentpos'] = minList[0], minList[1], minList[2], [minList[3][0], minList[3][1]]
        # remove the minList from paths available since it's already been expanded
        path.remove(minList)
        f = minDict['f']
        g = minDict['g']
        h = minDict['h']
        x = minDict['currentpos'][0]
        y = minDict['currentpos'][1]
        width = len(grid)
        height = len(grid[0])
        list_pos.append([y,x])
        expanded[x][y] = iteration # to show when the position was expanded
        iteration += 1
    return minDict, expanded

def main(argv):
    global list_pos
    file = sys.argv[1] if argv else "small.txt"
    f = open(file)
    grid = []
    height = 0
    for line in f:
        row = line.strip().split()
        width = len(row) # get the width for the display
        height += 1 # get height for pygame display
        row = [int(_) for _ in row]
        grid.append(row)
        
    print("{} before running".format(file))
    for row in grid:
        print(row)
    print()
    # always start in top left
    start = [0, 0]
    list_pos.append(start)
    # goal is always bottom right
    goal = [len(grid) - 1, len(grid[0]) - 1]

    minDict, expand = astar_search(grid, start, goal)

    print("Final Path:")
    for row in expand:
        print(row)
    print(minDict)

    # run gui
    water_gui.run_game(width, height, grid, list_pos)
    

if __name__ == '__main__':
    main(sys.argv[1:]) if sys.argv else main()