import cv2
from imutils.video import FileVideoStream
from imutils.video import FPS
import imutils
from cv2 import VideoWriter
import mediapipe as mp
import importlib
from drawing_utils import *
import os
import glob
import sys
import time

mp_drawing = importlib.import_module('drawing_utils')
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands


def Mediapipe_hands(input, output, frame_w, frame_h):
    
    with mp_hands.Hands(
        model_complexity=0,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as hands:
        while cap.isOpened():
            success, image = cap.read()
            if not success:
                """print("Ignoring empty camera frame.")
                    # If loading a video, use 'break' instead of 'continue'.
                continue"""
                break
            
            # To improve performance, optionally mark the image as not writeable to
            # pass by reference.
            image.flags.writeable = False
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            results = hands.process(image)

            # Draw the hand annotations on the image.
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            imageHeight, imageWidth, _ = image.shape
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(
                    image,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style())
                    for point in mp_hands.HandLandmark:
                        normalizedLandmark= hand_landmarks.landmark[point]
                        #pixelCoordinatesLandmark=mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)
         
                        #print(point)
                        #print(pixelCoordinatesLandmark)
                        #print(normalizedLandmark)
                        #txt_path= 'D:\\NGHIEN-CUU-COMVIS\\Coding\\mediapipe\\coordinate-file-3.txt'
                        
                        
                        with open(txt_path,'a') as f:
                            f.write(repr(normalizedLandmark)+"\n")
                        f.close()
            # Flip the image horizontally for a selfie-view display
            #cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))
            out.write(cv2.flip(image, 1))
    
            if cv2.waitKey(5) & 0xFF == 27:
                break
    cap.release()
    out.release()

    cv2.destroyAllWindows()


if __name__=="__main__":
   """ # For webcam/video input:
    cap = cv2.VideoCapture('D:\\NGHIEN-CUU-COMVIS\\Picture\\1CM1_1_R_#217.avi')
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    out=cv2.VideoWriter('D:\\NGHIEN-CUU-COMVIS\\Picture\\output_video01.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))
    Mediapipe_hands(cap,out,frame_width,frame_height)"""

#READ FILES FROM A FOLDER  

pathfile = 'D:\\NGHIEN-CUU-COMVIS\\Picture\\Input'
"""
# Change the directory
os.chdir(pathfile)
# iterate through all file
for file in os.listdir():
    # Check whether file is in text format or not
    if file.endswith(".avi"):
        file_path = f"{pathfile}\{file}"
        print(file_path)
        # call read text file function
        cap = cv2.VideoCapture(file_path)
        frame_width = int(cap.get(3))
        frame_height = int(cap.get(4))
        #Output
        dir_out_name = 'D:\\NGHIEN-CUU-COMVIS\\Picture\\Output'
        out_basename = os.path.basename(file)
        save_out_name = out_basename.replace('.avi','')
        out = VideoWriter(os.path.join(dir_out_name,save_out_name+"."+'avi'), cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))
        #Data
        dir_txt_name = 'D:\\NGHIEN-CUU-COMVIS\\Picture\\Data'
        txt_basename = os.path.basename(file)
        save_txt_name = txt_basename.replace('.avi','')
        txt_path = os.path.join(dir_txt_name,save_txt_name+"."+'txt')
        #Processing
        Mediapipe_hands(cap,out,frame_width,frame_height)
        continue
"""
"""
#READ FILES FROM MULTIPLE DIRECTORIES
# Folder Path
pathfile = 'D:\\NGHIEN-CUU-COMVIS\\Picture\\Input\\**\\*.avi'
for file in glob.iglob(pathfile, recursive= True): #iglob returns an iterator which will be executed simultaneously 
    if os.path.isfile(file): #filter dirs
        cap = cv2.VideoCapture(file)
        frame_width = int(cap.get(3))
        frame_height = int(cap.get(4))
        print(file)
        #Data
        dir_txt_name = 'D:\\NGHIEN-CUU-COMVIS\\Picture\\Data'
        txt_basename = os.path.basename(file)
        save_txt_name = txt_basename.replace('.avi','')
        txt_path = os.path.join(dir_txt_name,save_txt_name+"."+'txt')
        #Output
        dir_out_name = 'D:\\NGHIEN-CUU-COMVIS\\Picture\\Output'
        out_basename = os.path.basename(file)
        save_out_name = out_basename.replace('.avi','')
        out = VideoWriter(os.path.join(dir_out_name,save_out_name+"."+'avi'), cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))
        #Processing
        Mediapipe_hands(cap,out,frame_width,frame_height)
        continue

"""
""""
#step 1, set up the captures:
#
pathfile = 'D:\\NGHIEN-CUU-COMVIS\\Picture\\Input\\**\\*.avi'
caps = []
for file in glob.iglob(pathfile,recursive=True):
    caps.append(cv2.VideoCapture(file))
    print(caps)
        
#step 2, iterate through videoframes, collect images, and stitch them
#    
while True:
    frames = [] # frames for one timestep
    for cap in caps:
        frame_width = int(cap.get(3))
        frame_height = int(cap.get(4))
        print(file)
        #Data
        dir_txt_name = 'D:\\NGHIEN-CUU-COMVIS\\Picture\\Data'
        txt_basename = os.path.basename(file)
        save_txt_name = txt_basename.replace('.avi','')
        txt_path = os.path.join(dir_txt_name,save_txt_name+"."+'txt')
        #Output
        dir_out_name = 'D:\\NGHIEN-CUU-COMVIS\\Picture\\Output'
        out_basename = os.path.basename(file)
        save_out_name = out_basename.replace('.avi','')
        out = VideoWriter(os.path.join(dir_out_name,save_out_name+"."+'avi'), cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))
        #Processing
        Mediapipe_hands(cap,out,frame_width,frame_height)

    # stitch a new frame from frames
    # append to output video
"""



cap = cv2.VideoCapture(str(sys.argv[1]))
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
dir_txt_name = 'D:\\NGHIEN-CUU-COMVIS\\Picture\\Data'
save_name = str(sys.argv[1]).replace('.avi','')
dir_out_name = 'D:\\NGHIEN-CUU-COMVIS\\Picture\\Output'
out=cv2.VideoWriter(os.path.join(dir_out_name,save_name+"."+'avi'),cv2.VideoWriter_fourcc('M','J','P','G'), 30, (frame_width,frame_height))
txt_path = os.path.join(dir_txt_name,save_name +"."+'txt')
Mediapipe_hands(cap,out,frame_width,frame_height)
        


        
        