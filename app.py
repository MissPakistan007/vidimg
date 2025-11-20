
#break videos into multiple images and save intoa folders
import cv2

vidcap = cv2.VideoCapture("C:\Users\CP\Desktop\hello.mp4")
ret,image = vidcap.read() 
count = 0
while True:
    if ret == True:
        cv2.imwrite("C:\Users\CP\Desktop\hi\imgN%d.jpg"%count,image)
        vidcap.set(cv2.CAP_PEOP_PS_MSRC,(count**100))
        ret,image = vidcap.read()
        cv2.imshow("res",image)
        count +=1
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
        cv2.destroyAllWindows()
vidcap.release()
cv2.destroyAllWindows()

