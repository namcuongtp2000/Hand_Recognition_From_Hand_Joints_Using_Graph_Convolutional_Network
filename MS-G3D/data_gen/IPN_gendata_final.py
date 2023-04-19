import sys
sys.path.extend(['../'])

import pickle
import argparse

from tqdm import tqdm
from preprocess import pre_normalization
num_joint = 21
max_body_true = 1
max_frame= 670

import numpy as np
import os


def read_hands_filter(file):
    with open(file, 'r') as f:
        print('Processing: %s'%file)
        hands_sequence = {}
        hands_sequence['numFrame'] = int(f.readline())
        hands_sequence['frameInfo'] = []
        # num_body = 0
        for t in range(hands_sequence['numFrame']):
            frame_info = {}
            frame_info['numBody'] = int(f.readline())
            frame_info['bodyInfo'] = []

            for m in range(frame_info['numBody']):
                body_info = {}
                body_info_key = [
                    'class_id', 'start_frame', 'stop_frame'
                ]
                body_info = {
                    k: float(v)
                    for k, v in zip(body_info_key, f.readline().split())
                }
                body_info['numJoint'] = int(f.readline())
                body_info['jointInfo'] = []
                for v in range(body_info['numJoint']):
                    joint_info_key = [
                        'x', 'y', 'z'
                    ]
                    joint_info = {
                        k: float(v)
                        for k, v in zip(joint_info_key, f.readline().split())
                    }
                    body_info['jointInfo'].append(joint_info)
                frame_info['bodyInfo'].append(body_info)
            hands_sequence['frameInfo'].append(frame_info)

    return hands_sequence

def get_nonzero_std(s):  # tvc
    index = s.sum(-1).sum(-1) != 0  # select valid frames
    s = s[index]
    if len(s) != 0:
        s = s[:, :, 0].std() + s[:, :, 1].std() + s[:, :, 2].std()  # three channels
    else:
        s = 0
    return s


def read_xyz(file, max_body=1, num_joint=21):
    seq_info = read_hands_filter(file)
    data = np.zeros((max_body, seq_info['numFrame'], num_joint, 3))
    for n, f in enumerate(seq_info['frameInfo']):
        for m, b in enumerate(f['bodyInfo']):
            for j, v in enumerate(b['jointInfo']):
                if m < max_body and j < num_joint:
                    data[m, n, j, :] = [v['x'], v['y'], v['z']]
                else:
                    pass

    # select max energy hand
    energy = np.array([get_nonzero_std(x) for x in data])
    index = energy.argsort()[::-1][0:max_body_true]
    data = data[index]

    data = data.transpose(3, 1, 2, 0)
    return data


def gendata(data_path, data_out_path, label_out_path,ignored_sample_path=None):
    '''if ignored_sample_path != None:
        with open(ignored_sample_path, 'r') as f:
            ignored_samples = [line.strip() + '.txt' for line in f.readlines()]
    else:
        ignored_samples = []'''
    sample_name = []
    sample_label = []
    for file in sorted(os.listdir(data_path)):
        #if file in ignored_samples:
        #    continue
        with open(os.path.join('D:\\TAI-LIEU-HOC-TAP\\Coding\\MS-G3D\\data\\IPN_raw\\IPN_train',file),'r') as f:
                lines=list(f.readlines())
                data = [str(line).replace('\n','') for line in lines]
                target_label = int(float(str(data[2]).split(' ')[0]))
        sample_name.append(file)
        sample_label.append(target_label-2)
    
    
    with open(label_out_path, 'wb') as f:
        pickle.dump((sample_name, list(sample_label)), f)

    fp = np.zeros((len(sample_label),3, max_frame, num_joint,1), dtype=np.float32)

    # Fill in the data tensor `fp` one training example a time
    for i, s in enumerate(tqdm(sample_name)):
        data = read_xyz(os.path.join(data_path, s),max_body=1, num_joint=num_joint)
        fp[i, :, 0:data.shape[1], :, :] = data
        
    fp = pre_normalization(fp)
    np.save(data_out_path,fp)

if __name__ == '__main__':

        data_path = 'D:\\TAI-LIEU-HOC-TAP\\Coding\\MS-G3D\\data\\IPN_raw\\IPN_train'
        #ignored_sample_path = 'D:\\NGHIEN-CUU-COMVIS\\Coding\\MS_G3D\\data\\IPN_raw\\ignore_file.txt'
        data_out_path = 'D:\\TAI-LIEU-HOC-TAP\\Coding\\MS-G3D\\data\\IPN_balanced\\IPN_train\\train_data_joint.npy'
        label_out_path = 'D:\\TAI-LIEU-HOC-TAP\\Coding\\MS-G3D\\data\\IPN_balanced\\IPN_train\\train_label.pkl'

        gendata(data_path, data_out_path, label_out_path)