import sys
sys.path.extend(['../'])

import pickle
import argparse

from tqdm import tqdm
from data_gen.preprocess import pre_normalization
num_joint = 21
max_body_true = 1
max_frame= 4500

import numpy as np
import os


def read_hands_filter(file):
        with open(file,'r') as f:
            hands_sequence = {}
            hands_sequence['numGesture'] = int(f.readline())
            hands_sequence['gesture_info'] = []

            for t in range(hands_sequence['numGesture']):
                gesture_info = {}
                gesture_info_key= [
                    'class_id', 'class_label', 'start_frame', 'stop_frame'
                    ]
                gesture_info = {
                    k:float (v)
                    for k,v in zip(gesture_info_key, f.readline().split())
                }
                # duration = numFrame
                gesture_info['duration'] = int(f.readline())
                gesture_info['frame_info'] = []

                for v in range(gesture_info['duration']):
                    frame_info = {}
                    frame_info['numJoint'] = int(f.readline())
                    frame_info['JointInfo']= []
                    for m in range(frame_info['numJoint']):
                        joint_info_key = [
                            'joint_id','x', 'y', 'z'
                        ]
                        joint_info = {
                            k:float(v)
                            for k,v in zip(joint_info_key,f.readline().split())
                        }
                        frame_info['JointInfo'].append(joint_info)
                    gesture_info['frame_info'].append(frame_info)
                hands_sequence['gesture_info'].append(gesture_info)
        return hands_sequence

def get_nonzero_std(s):  # tvc
    index = s.sum(-1).sum(-1) != 0  # select valid frames
    s = s[index]
    if len(s) != 0:
        s = s[:, :, 0].std() + s[:, :, 1].std() + s[:, :, 2].std()  # three channels
    else:
        s = 0
    return s


def read_xyz(file, max_body=1, num_joint=25):
    seq_info = read_hands_filter(file)
    data = np.zeros((max_body, seq_info['numFrame'], num_joint, 3))
    for n, f in enumerate(seq_info['gesture_info']):
        for m, b in enumerate(f['frame_info']):
            for j, v in enumerate(b['jointInfo']):
                if j < num_joint:
                    data[1, n, j, :] = [v['x'], v['y'], v['z']]
                else:
                    pass

    # select max energy hand
    energy = np.array([get_nonzero_std(x) for x in data])
    index = energy.argsort()[::-1][0:max_body_true]
    data = data[index]

    data = data.transpose(3, 1, 2, 0)
    return data

def gendata(data_path, data_out_path, label_out_path):
    sample_name = []
    sample_label = []
    for filename in sorted(os.listdir(data_path)):
        sample_name.append(filename)
        sample_label.append(action_class - 1)
    
    
    with open(label_out_path, 'wb') as f:
        pickle.dump((sample_name, list(sample_label)), f)

    fp = np.zeros((len(sample_label),max_frame, 3, num_joint), dtype=np.float32)

    # Fill in the data tensor `fp` one training example a time
    for i, s in enumerate(tqdm(sample_name)):
        data = read_xyz(os.path.join(data_path, s),max_body=1, num_joint=num_joint)
        fp[i, :, 0:data.shape[1], :, :] = data
        
    fp = pre_normalization(fp)
    np.save(data_out_path,fp)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='IPN-Hand Data Converter.')
    parser.add_argument(
        '--data_path', default='../data/IPN_raw')
    parser.add_argument(
        '--out_folder', default='../data/IPN')
    arg = parser.parse_args()

    part = ['val', 'train']
    for p in part:
        print('IPN ', p)
        if not os.path.exists(arg.out_folder):
            os.makedirs(arg.out_folder)
        data_path = '{}/IPN_{}'.format(arg.data_path, p)
        data_out_path = '{}/{}_data_joint.npy'.format(arg.out_folder, p)
        label_out_path = '{}/{}_label.pkl'.format(arg.out_folder, p)

        gendata(data_path, data_out_path, label_out_path)