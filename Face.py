
import cv2 as cv
face_ref = cv.CascadeClassifier("face_ref.xml")
Camera = cv.VideoCapture(0)

def face_detection(frame):
    optimized_frame = cv.cvtColor(frame,cv.COLOR_BGR2RGB)
    face_detect = face_ref.detectMultiScale(optimized_frame,scaleFactor=1.1,minSize=(40,50),minNeighbors=3)
    return face_detect

def drawer_box(frame):
    for x,y,w,h in face_detection(frame):
        cv.rectangle(frame,(x,y),(x + w, y + h), (0,0,255), 4)

def Close_window():
    Camera.release()
    cv.destroyAllWindows()
    exit()

def main():
    while True:
        __, frame  = Camera.read()
        drawer_box(frame )
        cv.imshow("DEFF_FADE AI",frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            Close_window()  


if __name__ == "__main__" :
    main()


