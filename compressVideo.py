import cv2
import sys
import os
import numpy as np

argLength = len(sys. argv)
if(argLength != 3):
    print('Invalid number of arguments.')
    print('Input format: python compressVideo.py <VideoFile> <X>')
    sys.exit()

file_name = sys.argv[1]
scale_percent = int(sys.argv[2])

if scale_percent > 99 or scale_percent < 1:
    print('Invalid value for 2nd argument.')
    print('Valid range: 1 <= scale_percent <= 99')
    sys.exit()

valid_types = ('.mp4', '.wav', '.avi', '.mov')

file_type = os.path.splitext(file_name)[1]
if(file_type.lower() not in valid_types):
    print('File format not supported.')
    print('Supported formats: ', valid_types)
    sys.exit()

if not os.path.isfile(file_name):
    print('Video file not found.')
    sys.exit()

cap = cv2.VideoCapture(file_name)

ret, frame = cap.read()
if not ret:
    print('Video file not found.')
    sys.exit()

fps = cap.get(cv2.CAP_PROP_FPS)

width = int(frame.shape[1]*scale_percent/100)
height = int(frame.shape[0]*scale_percent/100)
dim = (width, height)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('video_output.mp4', fourcc, fps, dim)

length = cap.get(cv2.CAP_PROP_FRAME_COUNT)
ani = "|///———\\\||"
idx = 0
while True:	
    ret, frame = cap.read()

    if ret == True:
        print('', ani[idx%len(ani)], 'Compressing video:', int(idx*100/length)+1, '\b% complete', end="\r")
        idx += 1
        resized_frame = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)
        out.write(resized_frame)
    else:
        print('\bVideo compressed successfully.     ')
        break
    
cap.release()
out.release()
cv2.destroyAllWindows()