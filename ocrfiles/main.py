import cv2 #importing cv2 library

face_cas = cv2.CascadeClassifier("frontface.xml") #upload frontface file

cap = cv2.VideoCapture(0) # starting camera stream

while cap.isOpened():
    ret, frame = cap.read() # reading camera frame

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #colored to gray function

    faces = face_cas.detectMultiScale(gray, 1.3, 5) #Stores the many number of faces

    for face in faces:
        x = face[0]
        y = face[1]
        w = face[2]
        h = face[3] # To store the values of the recatangle

        cv2.rectangle(frame, (x,y), (x+w ,y+h), (0,255,0), 7) #to make a rectangular around face
        print(x,y) #the x and y coordinate value



    cv2.imshow("Frame",frame) # showing camera stream

    if cv2.waitKey(1) & 0xFF == ord('q'): # to check if q is pressed

        break # if pressed exit while loop



cap.release() # turning off camera screen
cv2.destroyAllWindows() # closing the window which was showing camera stream


