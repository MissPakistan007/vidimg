
import cv2
import os


video_path = r"C:\Users\CP\Desktop\hello.mp4"
output_dir = r"C:\Users\CP\Desktop\hi" 


if not os.path.exists(output_dir):
    os.makedirs(output_dir)

vidcap = cv2.VideoCapture(video_path)
count = 0


if not vidcap.isOpened():
    print(f"Error: Could not open video file at {video_path}")
else:
    while True:
       
        ret, image = vidcap.read()
        
        if ret:
           
            filename = os.path.join(output_dir, f"imgN{count:05d}.jpg") # Use f-string and padding for better sorting
            
            cv2.imwrite(filename, image)
            
            cv2.imshow("Video Frame", image)
            
           
            if cv2.waitKey(1) & 0xFF == ord('q'):
                print("Stopping extraction by user request.")
                break
                
            count += 1
        else:
       
            print("Video extraction complete.")
            break

vidcap.release()
cv2.destroyAllWindows()
