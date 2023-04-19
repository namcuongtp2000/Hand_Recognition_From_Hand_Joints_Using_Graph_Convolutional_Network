import numpy as np
import sys

sys.path.extend(['../'])
from graph import tools
import networkx as nx

# Joint index:
# {0,  "WRIST"}
# {1,  "THUMB_CMC"},
# {2,  "THUMB_MCP"},
# {3,  "THUMB_IP"},
# {4,  "THUMB_TIP"},
# {5,  "INDEX_FINGER_MCP"},
# {6,  "INDEX_FINGER_PIP"},
# {7,  "INDEX_FINGER_DIP"},
# {8,  "INDEX_FINGER_TIP"},
# {9,  "MIDDLE_FINGER_MCP"},
# {10, "MIDDLE_FINGER_PIP"},
# {11, "MIDDLE_FINGER_DIP"},
# {12, "MIDDLE_FINGER_TIP"},
# {13, "RING_FINGER_MCP"},
# {14, "RING_FINGER_PIP"},
# {15, "RING_FINGER_DIP"},
# {16, "RING_FINGER_TIP"},
# {17, "PINKY_MCP"},
#{18, "PINKY_PIP"},
#{19, "PINKY_DIP"},
#{20, "PINKY_TIP"},

# Edge format: (origin, neighbor)
num_node = 21
self_link = [(i, i) for i in range(num_node)]
inward = [(1, 0), (2, 1), (3, 2), (4, 3), (5, 0), (6, 5), (7, 6), (8, 7), (9, 5), (10, 9), (11, 10), (12, 11),
        (13, 9), (14, 13), (15, 14), (16, 15), (17, 0), (17, 13), (18, 17), (19, 18), (20, 19) ]
outward = [(j, i) for (i, j) in inward]
neighbor = inward + outward


class Graph:
    def __init__(self, labeling_mode='spatial'):
        self.A = self.get_adjacency_matrix(labeling_mode)
        self.num_node = num_node
        self.self_link = self_link
        self.inward = inward
        self.outward = outward
        self.neighbor = neighbor

    def get_adjacency_matrix(self, labeling_mode=None):
        if labeling_mode is None:
            return self.A
        if labeling_mode == 'spatial':
            A = tools.get_spatial_graph(num_node, self_link, inward, outward)
        else:
            raise ValueError()
        return A


if __name__ == '__main__':
    A = Graph('spatial').get_adjacency_matrix()
    print('')
