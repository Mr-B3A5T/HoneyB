import cv2

# Open a video stream
cap = cv2.VideoCapture('path/to/your_video_file.mp4')

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display the resulting frame
    cv2.imshow('CCTV Camera', frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if not ret:
        # if video finished then rewind
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

# Release the video stream
cap.release()

# Close all windows
cv2.destroyAllWindows()
