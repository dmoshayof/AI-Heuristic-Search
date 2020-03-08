from ways import tools


def best_first_graph_search(problem, f):
    node = problem.start
    frontier = tools.PriorityQueue(f)  # Priority Queue
    frontier.append(node)
    closed_list = dict()
    while frontier:
        node = frontier.pop()
        if problem.is_goal(node.state):
            print(*node.path(), node.path_cost, len(closed_list.items()))
            return node.path()
        closed_list[node.state] = 3
        links = node.expand(problem)
        for child in links:
            is_in_Frontier = child not in frontier
            if child.state not in closed_list.keys() and is_in_Frontier:
                frontier.append(child)
            elif not is_in_Frontier and f(child) < frontier[child]:
                del frontier[child]
                frontier.append(child)
    return []
