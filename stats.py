'''
This file should be runnable to print map_statistics using 
$ python stats.py
'''

from collections import namedtuple, Counter
from ways import load_map_from_csv

def map_statistics(roads):
    '''return a dictionary containing the desired information
    You can edit this function as you wish'''
    Stat = namedtuple('Stat', ['max', 'min', 'avg'])
    link_count = 0
    max_dist = 0
    min_dist = 1
    avg_dist = 0
    avg_branch = 0
    cnt = Counter()
    for link in roads.iterlinks():
        link_count += 1
        cnt[link[3]] += 1
        if max_dist < link[2]:
            max_dist = link[2]
        if min_dist > link[2]:
            min_dist = link[2]
        avg_dist += link[2]
    Counter()
    avg_dist /= link_count
    for junction in roads.junctions():
        avg_branch += len(junction[3])
    avg_branch /= len(roads.junctions())
    max_branch = max(len(i[3]) for i in roads.junctions())
    min_branch = min(len(i[3]) for i in roads.junctions())
    return {
        'Number of junctions': len(roads),
        'Number of links': link_count,
        'Outgoing branching factor': Stat(max=max_branch, min=min_branch, avg=avg_branch),
        'Link distance': Stat(max=max_dist, min=min_dist, avg=avg_dist),
        # value should be a dictionary
        # mapping each road_info.TYPE to the no' of links of this type
        'Link type histogram': cnt  # tip: use collections.Counter
    }

def print_stats():
    for k, v in map_statistics(load_map_from_csv()).items():
        print('{}: {}'.format(k, v))


if __name__ == '__main__':
    from sys import argv

    assert len(argv) == 1
    print_stats()
