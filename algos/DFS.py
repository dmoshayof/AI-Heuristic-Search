import math

def ida_star(path,problem, node, f_limit, f):
    f_node=f(node)
    if f_node>f_limit:
       return f_node
    if problem.is_goal(node.state):
        return -1
    min=math.inf
    for child in node.expand(problem):
        if child.state not in path:
            path.insert(0,child.state)
            f_limit=ida_star(path,problem,child,f_limit, f)
            if f_limit==-1:
                return -1
            if f_limit<min:
                min=f_limit
            del path[0]
    return min