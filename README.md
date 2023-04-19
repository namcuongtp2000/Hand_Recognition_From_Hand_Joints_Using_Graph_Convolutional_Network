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

https://drive.google.com/drive/folders/1qjz1tRHnDAIrcbEqkpoOS8b72pvLXyTp

# **5. Issues**

You should modify your real local computer file paths instead of my owns.

This is a test projects and it made a lot of mistakes when can't classify hand gesture labels and recognize exact some hand gestures with short duration.

