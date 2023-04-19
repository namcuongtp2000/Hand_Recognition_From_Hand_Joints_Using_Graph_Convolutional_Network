import cv2
import os
import mediapipe as mp
import sys
import glob
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands
# your function
def video2frames( video_file, output_path):
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    
    index = 0        
    
    with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
        while cap.isOpened():
            success, image = cap.read()
            if not success:
                break
            
            index += 1
            if index % 29 != 0:
                # To improve performance, optionally mark the image as not writeable to
                # pass by reference.
                image.flags.writeable = False
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                results = hands.process(image)

                # Draw the hand annotations on the image.
                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                
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
                            with open(txt_path,'a') as f:
                                f.write(repr(normalizedLandmark)+"\n")
                            f.close()
                    
            cv2.imwrite(output_path + '/' + str(index) + '.png', image)
            
            if cv2.waitKey(5) & 0xFF == 27:
                break

    cap.release()
    cv2.destroyAllWindows()

if __name__=="__main__":
# run all
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
            dir_out_name =  'D:\\NGHIEN-CUU-COMVIS\\Picture\\Output'
            output_path = os.path.join(dir_out_name,save_txt_name)
            video2frames(cap, output_path)




