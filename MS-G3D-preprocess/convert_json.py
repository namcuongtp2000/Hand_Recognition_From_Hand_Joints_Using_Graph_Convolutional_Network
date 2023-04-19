from glob import glob
import json
import os.path
import re

root = "/home/saurabh/Documents/Study_Matter/VLR_16824/project/json_test_crop"
out_dir = "/home/saurabh/Documents/Study_Matter/VLR_16824/project/data"

label_out = {}
for dir_path in glob(f"{root}/*"):
    dir_name = os.path.basename(dir_path)
    frame_data = {}
    for file_path in glob(f"{dir_path}/*.json"):
        out = {}
        max_idx = 0
        with open(file_path) as json_ptr:
            m = re.search(r".*?_(\d+)_(\d+)_keypoints\.json",os.path.basename(file_path))
            if not m:
                raise Exception("Regex should match")
            frame_0 = int(m.group(2))
            file_num = int(m.group(1))
            src = json.load(json_ptr)
            xys = src["people"][0]["pose_keypoints_2d"]
            xy = [p for i, p in enumerate(xys) if i % 3 != 2]
            s = [p for i, p in enumerate(xys) if i % 3 == 2]
            frame_data[frame_0+1] ={}
            cur_data = frame_data[frame_0+1]
            cur_data["frame_index"] = frame_0+1
            cur_data["skeleton"] = [{"pose": xy,
                                    "score": s}]
            if frame_0+1 > max_idx:
                max_idx = frame_0+1
        if file_num in range(2930,2945):
            label = "right"
            label_idx = 0
        elif file_num in range(2945, 2960):
            label = "left"
            label_idx = 1
        elif file_num in range(2960, 2975):
            label = "parallel"
            label_idx = 2
        else:
            raise Exception("File numbers should be between 2930-2974")
    out["data"] = []
    for idx in range(1, max_idx+1):
        out["data"].append(frame_data[idx])
    out["label"] = label
    out["label_index"] = label_idx
    label_out[dir_name] = {"has_skeleton" : True,
                           "label": label,
                           "label_idx": label_idx}

    with open(f"{out_dir}/train/{dir_name}.json", "w") as out_json:
        json.dump(out, out_json)

with open(f"{out_dir}/train_label.json", "w") as label_file:
    json.dump(label_out, label_file)