def required_conf(): #Returns a list of the required conf files
    list = ["camera.conf"]
    return list
def required_modules(): #Returns a list of the required conf files
    list = ["serialsetup"]
    return list
    
def setup():
    print("setup")
    
def camera():
    import numpy as np
    import cv2

    cap = cv2.VideoCapture(0)
    cap.set(3,640)
    cap.set(4,480)
    i=0
    while (cap.isOpened() == 0):
        i=i+1
        if i == 500:
            return -1
        
    while(True):
        # Capture frame-by-frame
        ret_val, frame = cap.read()
        
        
        # Display the resulting frame
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if cv2.getWindowProperty('frame',cv2.WND_PROP_VISIBLE) == 0:
            break
        # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
    return 0

