"""
Copyright David Miall, 2020
"""

def required_conf(): #Returns a list of the required conf files
    list = ["camera.conf"]
    return list
def required_modules(): #Returns a list of the required conf files
    list = 0
    return list
    
def setup():
    print("setup")
    
def camera(serial_dev):
    try:
        f = open("conf/camera.conf","r")
    except:
        print("Missing camera.conf")
        return -1
    camera_device = f.read()
    import cv2, string
    try:
        cap = cv2.VideoCapture(int(camera_device))
    except:
        cap = cv2.VideoCapture(camera_device)
    cap.set(3,1280)
    cap.set(4,720)
    i=0
    while (cap.isOpened() == 0):
        i=i+1
        if i == 1000:
            return -1
        
    while(True):
        # Capture frame-by-frame
        if serial_dev == -1:
            output = "No Meter."
        else : 
            output = serial_dev.readline().decode("utf-8", "ignore")
            output = ''.join(filter(lambda x: x in set(string.printable), output))
            output = output[:-1]
        ret_val, frame = cap.read()
        cv2.putText(frame, output,
		(50, 100), cv2.FONT_HERSHEY_TRIPLEX, 3.0, (0, 128, 255), 3)
        
        # Display the resulting frame
        cv2.imshow('Camera', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if cv2.getWindowProperty('Camera',cv2.WND_PROP_VISIBLE) == 0:
            break
        # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
    return 0

