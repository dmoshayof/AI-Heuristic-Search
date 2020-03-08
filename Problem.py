from ways import compute_distance
from ways.info import SPEED_RANGES
import numpy as np
class Problem:
    def __init__(self, start, goal, graph):
        self.start = start
        self.goal = goal
        self.roads = graph

    def actions(self, s):
        return self.roads[s.index].links

    def succ(self, s, a):
        nodes = [self.roads[l.target] for l in s.links]
        for n in nodes:
            if a.target == n.index:
                return n

    def is_goal(self, s):
        return s == self.goal.state

    def get_link(self, s, a):
        link = [l for l in s.links if l.target == a.index]
        return link[0]

    def kph_to_mpm(self, speed):
        return (1000 / 60) * speed

    def step_cost(self, s, a):
        link = a
        max_speed = max(SPEED_RANGES[link.highway_type])
        time = float(link.distance)/max_speed
        return time /1000



class Node:
    def __init__(self, junction, parent=None, action=None, path_cost=0):
        self.state = junction.index
        self.parent = parent
        self.links = junction.links
        self.path_cost = path_cost
        self.h = 0
        self.depth = 0
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def total_cost(self):
        return self.g + self.h

    def path(self):
        path = []
        current_node = self
        while current_node:
            path.append(current_node.state)
            current_node = current_node.parent
        path.reverse()
        return [s for s in path]

    def expand(self,problem):
        nodes = self.links
        send = []
        for l in nodes:
            next_state = problem.roads[l.target]
            time =self.path_cost + problem.step_cost(self,l)
            next_node = Node(next_state,self,None,time)
            send.append(next_node)
        return send


    def __repr__(self):
        return f"<{self.state}>"

    def __lt__(self, node):
        return self.state < node.state

    def __eq__(self, other):
        return isinstance(other, Node) and self.state == other.state

    def __ne__(self, other):
        return not (self == other)

    def __hash__(self):
        return hash(self.state)