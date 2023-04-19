import os
'''pathfile = 'D:\\NGHIEN-CUU-COMVIS\\Coding\\MS-G3D\\data\\IPN_raw\\IPN_val'
for file in sorted(os.listdir(pathfile)):
    with open(os.path.join(pathfile,file), 'r') as f:
        print(file)'''
with open('D:\\NGHIEN-CUU-COMVIS\\Coding\\MS-G3D\\data\\IPN_raw\\IPN_val\\1CM1_1_R_#219_6.txt','r') as f:
        hands_sequence = {}
        hands_sequence['numFrame'] = int(f.readline())
        hands_sequence['frameInfo'] = []
        # num_body = 0
        for t in range(hands_sequence['numFrame']):
            frame_info = {}
            frame_info['numBody'] = int(f.readline())
            print(frame_info['numBody'])
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