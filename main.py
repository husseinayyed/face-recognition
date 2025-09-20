import cv2
face_detection = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
while True:
    frame = cv2.imread("messi.jpg")
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_detection.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
      frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
      frame = cv2.putText(frame,"FACE",(x,y),cv2.FONT_HERSHEY_COMPLEX,1.3,color=(0,255,0),thickness=2)
    num_faces = len(faces)
    if num_faces < 1:print("no face detected")
    elif num_faces == 1:print("1 face was detected successfully")
    else: print(f"{num_faces} faces were detected successfully")
    cv2.imshow('Hussein Ayed', frame)
    if cv2.waitKey(0): break
cv2.destroyAllWindows()