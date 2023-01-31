import socket
import cv2
import numpy as np
import tkinter as tk
from tkinter import messagebox

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_address = ('0.0.0.0', 8000)
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

# Load a sample video file
cap = cv2.VideoCapture('sample_video.mp4')

# Define the login credentials
username = "admin"
password = "secret"

# Create a Tkinter window for the dashboard
root = tk.Tk()
root.title("CCTV System Dashboard")

def login():
    # Get the entered username and password
    entered_username = username_entry.get()
    entered_password = password_entry.get()

    # Check if the entered credentials are correct
    if entered_username == username and entered_password == password:
        # Show the video feed
        frame.pack()
        root.after(30, update_frame)
    else:
        # Show an error message
        messagebox.showerror("Error", "Invalid username or password")

# Add a label and entry for the username
username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

# Add a label and entry for the password
password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

# Add a button to log in
login_button = tk.Button(root, text="Login", command=login)
login_button.pack()

# Add a label to display the video feed
frame = tk.Label(root, text="CCTV Feed")

def update_frame():
    ret, img = cap.read()
    if ret:
        # Convert the frame to a photo image
        img = cv2.resize(img, (640, 480))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        img = ImageTk.PhotoImage(img)

        # Update the label with the new image
        frame.configure(image=img)
        frame.image = img

    # Schedule the next update
    root.after(30, update_frame)

def start_server():
    while True:
        # Wait for a connection
        print('waiting for a connection')
        connection, client_address = sock.accept()

        try:
            print('connection from', client_address)

            # Send the fake CCTV footage
            while cap.isOpened():
                ret, frame = cap.read()
                if ret:
                    # Convert the frame to a byte array
                    frame = cv2.resize(frame, (640, 480
