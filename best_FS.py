from Problem import Node
from ways import tools
def best_first_graph_search(problem, f):
    node = Node(problem.start.state)
    frontier = tools.PriorityQueue(f)  # Priority Queue
    frontier.append(node)
    log = []
    closed_list = set()
    while frontier:
        print(f'size of closed list:{len(closed_list)}')
        node = frontier.pop()
        if problem.is_goal(node.state):
            return node.path()
        closed_list.add(node)
        frontier_func = None
        for child in node.expand(problem):
            for n in frontier.heap:
                if n[1].state.index == child.state.index:
                    frontier_func = n[0]
            if child not in closed_list and child not in frontier:
                frontier.append(child)

            elif child in frontier and f(child) < frontier_func:
                del frontier[child]
                frontier.append(child)
    return []