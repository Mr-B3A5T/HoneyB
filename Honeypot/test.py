from flask import Flask, Response
import cv2
import socket

app = Flask(__name__)

# Load the video file
video = cv2.VideoCapture("footage.mp4")

# Create a TCP/IP socket for the honeypot
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_address = ('0.0.0.0', 12345)
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)

def generate_frames():
    # Continuously accept incoming connections and log them
    while True:
        print('Waiting for a connection...')
        connection, client_address = server_socket.accept()
        try:
            print('Accepted connection from', client_address)
            while True:
                # Read a frame from the video
                ret, frame = video.read()

                # If the video has ended, restart it
                if not ret:
                    video.set(cv2.CAP_PROP_POS_FRAMES, 0)
                    ret, frame = video.read()

                # Encode the frame to a JPEG image and send it to the client
                jpeg_frame = cv2.imencode('.jpg', frame)[1].tobytes()
                connection.sendall(jpeg_frame)
        finally:
            connection.close()

@app.route('/')
def index():
    return """
    <html>
    <head>
        <title>CCTV Honeypot</title>
    </head>
    <body>
        <img src="http://localhost:12345/video_feed"/>
    </body>
    </html>
    """

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
