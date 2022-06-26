# import necessary libraries 
  
import cv2 
import numpy as np 
  
# Turn on Laptop's webcam
cap = cv2.VideoCapture(0)
  
  
while True:
      
    ret, frame = cap.read()
  
    # Locate points of the documents or object which you want to transform
    src = np.float32([[143, 36], [441, 65], [112, 223], [461, 245]])   #points 1,2,4,3 from top left corner in clockwise order
    dst = np.float32([[0, 260], [640, 260],[0, 400], [640, 400]])
      
    # Apply Perspective Transform Algorithm
    matrix = cv2.getPerspectiveTransform(src, dst)
    result = cv2.warpPerspective(frame, matrix, (640, 480))
    # Wrap the transformed image
  
    cv2.imshow('frame', frame) # Inital Capture
    cv2.imshow('frame1', result) # Transformed Capture
  
    if cv2.waitKey(24) == 27:
        break
  
cap.release()
cv2.destroyAllWindows()