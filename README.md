# Hand_Recognition_From_Hand_Joints_Using_Graph_Convolutional_Network

This project follows this below Flow chart:

<img src="/img/flow_chart.png" alt="Flow Chart" title="Flow Chart">

# **1. Dataset**

This project using IPN Dataset: https://gibranbenitez.github.io/IPN_Hand/

# **2. Hand joints recognition API**

Using Mediapipe Hands API from Google: https://developers.google.com/mediapipe/solutions

Installation: pip install mediapipe

# **3. Model Architecture**

Replace skeleton input information of whole body into hand joints information and format to fit the input of MS-G3D model.

Reference model architectures:

https://github.com/kenziyuliu/MS-G3D

https://github.com/lshiwjx/2s-AGCN

# **4. Pretrained models and visualize demo**

You should notice that there are 2 types of pretrained models. The first one are the output of file {MODELS}/data_gen/{gendata.py} with MODELS may be 2s-AGCN or MS-G3D, gendata.py for example IPN_gendata.py or IPN_gen_bone_data.py. This process will take input are hand joints' coordinates from text files, label 21 lines each of 21 hand joints' 3D coordinates in the definition of Mediapipe Hands and finally, generate 2 types of output files : npy and pkl for the MODELS input. You can use any different datasets and estimation processes that you want but make sure they are formated and labeled for {gendata.py}. Here's the pretrained models of IPN dataset and extracted features by Mediapipe hands for that process:

https://drive.google.com/drive/folders/1qjz1tRHnDAIrcbEqkpoOS8b72pvLXyTp

For the second training process, after getting npy and pkl files which data are formated and labeled, you can follow the the readme file from authors of {MODELS} to train your own dataset and take the top accuracy weight or checkpoint models to predict of recognize actions or gestures in test process.

# **5. Issues**

You should modify your real local computer file paths instead of my owns.

This is a test projects and it made a lot of mistakes when can't classify hand gesture labels and recognize exact some hand gestures with short duration.

