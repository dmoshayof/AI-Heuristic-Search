from ways import load_map_from_csv as load
from ways import compute_distance
from ways import tools
from ways import draw
from algos import best_first_graph_search
from algos import ida_star
from Problem import Problem, Node
import math

'''
Parse input and run appropriate code.
Don't use this file for the actual work; only minimal code should be here.
We just parse input and call methods from other modules.
'''

# do NOT import ways. This should be done from other files
# simply import your modules and call the appropriate functions

''''
  import csv
  from itertools import islice
  roads = load('israel.csv', 0,300000)
 # roads = load()
  problems = []
  junctions = roads.junctions()
  with tools.dbopen('problems.csv', 'rt') as f:
      it = islice(f, 0, sys.maxsize)
      for row in csv.reader(it):
          if len(row) != 0:
              start = Node(junctions[int(row[0])])
              goal = Node(junctions[int(row[1])])
              problem = Problem(start, goal, roads)
              problems.append(problem)
  paths = []
  for p in problems:
      t = time.time()
      paths.append(best_first_graph_search(p, f=g))
      paths.append('\n')
      print('--- %s sec---' % str(time.time() - t))
  file = open('UCSruns.txt', 'w')
  file.writelines(paths)
  '''''


def find_ucs_rout(source, target):
    'call function to find path, and return list of indices'

    def g(node):
        return node.path_cost

    '''
    # roads = load()
    import csv
    from itertools import islice
    roads = load('israel.csv', 0, 300000)
    # roads = load()
    problems = []
    total_h = []
    junctions = roads.junctions()
    with tools.dbopen('problems.csv', 'rt') as f:
        it = islice(f, 0, sys.maxsize)
        for row in csv.reader(it):
            if len(row) != 0:
                start = Node(junctions[int(row[0])])
                goal = Node(junctions[int(row[1])])
                problem = Problem(start, goal, roads)
                problems.append(problem)
    paths = []
    times = []
    for p in problems:
        t = time.time()
        paths.append(best_first_graph_search(p, f=g))
        paths.append('\n')
        times.append(time.time() - t)
    file = open('ucs.txt', 'w')
    file.write(' '.join(str(j) for j in paths))
    file2 = open('ucsTimes.txt', 'w')
    file2.write(' '.join(str(j) for j in times))
    '''
    roads = load()
    start = Node(roads[source])
    goal = Node(roads[target])
    p = Problem(start, goal, roads)
    return best_first_graph_search(p, f=g)


'''
    paths = []
    times = []
    for p in problems:
        t = time.time()
        paths.append(best_first_graph_search(p, f=lambda n: g(n) + h(n)))
        times.append(time.time() - t)
    file = open('Astar.txt', 'w')
    file.write(' '.join(str(j) for j in paths))
    file2 = open('AstarTimes.txt', 'w')
    file2.write(' '.join(str(j) for j in times))'''


def find_astar_route(source, target):
    'call function to find path, and return list of indices'

    def g(node):
        return node.path_cost

    def h(node):
        junction = roads[node.state]
        target = roads[goal.state]
        x = compute_distance(junction.lat, junction.lon, target.lat,
                             target.lon) / 110
        return x

    roads = load()
    start = Node(roads[source])
    goal = Node(roads[target])
    p = Problem(start, goal, roads)
    return best_first_graph_search(p, f=lambda n: h(n) + g(n))


def find_idastar_route(source, target):
    def g(node):
        return node.path_cost

    def h(node):
        junction = roads[node.state]
        target = roads[goal.state]
        x = compute_distance(junction.lat, junction.lon, target.lat,
                             target.lon) / 110
        return x

    roads = load()
    #roads = load('israel.csv',0,50)
    start = Node(roads[source])
    goal = Node(roads[target])
    p = Problem(start, goal, roads)
    limit_cost = h(start)
    path = [start.state]
    while (True):
        import time
        t = time.time
        next = ida_star(path, p, start, limit_cost, f=lambda n: g(n) + h(n))
        if next == -1:
            print(t-time.time)
            return path[::-1]
        if next == math.inf:
            return None
        limit_cost = next


def dispatch(argv):
    source, target = int(argv[2]), int(argv[3])
    if argv[1] == 'ucs':
        path = find_ucs_rout(source, target)
    elif argv[1] == 'astar':
        path = find_astar_route(source, target)
    elif argv[1] == 'idastar':
        path = find_idastar_route(source, target)
    print(' '.join(str(j) for j in path))


if __name__ == '__main__':
    from sys import argv

    dispatch(argv)
