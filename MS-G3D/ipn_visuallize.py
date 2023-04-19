import os
import sys
import pickle
import argparse
import numpy as np
from tqdm import tqdm
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# NTU RGB+D 60/120 Action Classes
actions = {
    0: "Pointing with one finger",
    1: "Pointing with two fingers",
    2: "Click with one finger",
    3: "Click with two fingers",
    4: "Throw up",
    5: "Throw down",
    6: "Throw left",
    7: "Throw right",
    8: "Open twice",
    9: "Double click with one finger",
    10: "Double click with two fingers",
    11: "Zoom in",
    12: "Zoom out",
}

ipn_skeleton_bone_pairs = tuple((i-1, j-1) for (i,j) in (
    (2, 1), (3, 2), (4, 3), (5, 4), (6, 1), (7, 6), (8, 7), (9, 8), (10, 6), (11, 10), (12, 11), (13, 12),
        (14, 10), (15, 14), (16, 13), (17, 16), (18, 1), (18, 14), (19, 18), (20, 19), (21, 20)
))

bone_pairs = {

    # NTU general
    'ipn': ipn_skeleton_bone_pairs
}


def visualize(args):
    data_path = args.datapath or 'D:\\TAI-LIEU-HOC-TAP\\Coding\\MS-G3D\\data\\{}\\val_data_joint.npy'.format(args.dataset)
    label_path = args.labelpath or 'D:\\TAI-LIEU-HOC-TAP\\Coding\\MS-G3D\\data\\{}\\val_label.pkl'.format(args.dataset)

    data = np.load(data_path, mmap_mode='r')
    with open(label_path, 'rb') as f:
        labels = pickle.load(f, encoding='latin1')

    bones = bone_pairs[args.dataset]
    print(f'Dataset: {args.dataset}\n')

    def animate(skeleton):
        ax.clear()
        ax.set_xlim([0,1])
        ax.set_ylim([0,1])
        ax.set_zlim([-1,1])
        for i, j in bones:
            joint_locs = skeleton[:,[i,j]]
            # plot them
            ax.plot(joint_locs[0],joint_locs[1],joint_locs[2], color='blue')

        action_class = labels[1][index] + 1
        action_name = actions[action_class]
        plt.title('Skeleton {} Frame #{} of total from {}\n (Action {}: {})'.format(index, skeleton_index[0], args.dataset, action_class, action_name))
        skeleton_index[0] += 1
        return ax

    for index in args.indices:
        mpl.rcParams['legend.fontsize'] = 10
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        ax.set_xlim([0,1])
        ax.set_ylim([0,1])
        ax.set_zlim([-1,1])

        # get data
        skeletons = data[index]
        action_class = labels[1][index] + 1
        action_name = actions[action_class]
        print(f'Sample index: {index}\nAction: {action_class}-{action_name}\n')   # (C,T,V,M)

        # Pick the first body to visualize
        skeleton1 = skeletons[..., 0]   # out (C,T,V)

        skeleton_index = [0]
        skeleton_frames = skeleton1.transpose(1,0,2)
        ani = FuncAnimation(fig, animate, skeleton_frames)

        plt.title('Skeleton {} from {} test data'.format(index, args.dataset))
        plt.show()


if __name__ == '__main__':
    # NOTE:Only supports joint data
    parser = argparse.ArgumentParser(description='IPN Hand Gesture Skeleton Visualizer')

    parser.add_argument('-d', '--dataset',
                        choices=['ipn'],
                        required=True)
    parser.add_argument('-p', '--datapath',
                        help='location of dataset numpy file')
    parser.add_argument('-l', '--labelpath',
                        help='location of label pickle file')
    parser.add_argument('-i', '--indices',
                        type=int,
                        nargs='+',
                        required=True,
                        help='the indices of the samples to visualize')

    args = parser.parse_args()
    visualize(args)


