import cv2

def video_feed_simulation():
    video_path = "path/to/your/video_file.mp4"
    video = cv2.VideoCapture(video_path)
    while True:
        ret, frame = video.read()
        if not ret:
            video.release()
            video = cv2.VideoCapture(video_path)
            continue
        cv2.imshow("Video feed simulation", frame)
        if cv2.waitKey(25) & 0xFF == ord("q"):
            break
    video.release()
    cv2.destroyAllWindows()
