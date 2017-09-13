import face_recognizer_module  # module with defined face recognition functions
import cv2  # OpenCV

# Get a video from default webcam
video_capture = cv2.VideoCapture(0)

# Load pictures of people to read their faces
# save encodings of their faces to _face_encodings variables
wiktor_image = face_recognizer_module.load_image_file("face2.png")
wiktor_face_encoding = face_recognizer_module.face_encodings(wiktor_image)[0]

stonka_image = face_recognizer_module.load_image_file("face1.png")
stonka_face_encoding = face_recognizer_module.face_encodings(stonka_image)[0]

gawor_image = face_recognizer_module.load_image_file("face3.png")
gawor_face_encoding = face_recognizer_module.face_encodings(gawor_image)[0]

# wiktor = 0, stonka = 1, gawor = 2
known_faces = [
    wiktor_face_encoding,
    stonka_face_encoding,
    gawor_face_encoding
]

# Initialize variables for face locations, encodings and objects' names
face_locations = []
face_encodings = []
face_names = []

process_this_frame = True  # used to process every other frame to make the program faster

while True:
    # Capture a single frame
    ret, frame = video_capture.read()

    # Resize the frame
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    if process_this_frame:

        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognizer_module.face_locations(small_frame)
        face_encodings = face_recognizer_module.face_encodings(small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:

            # See if the face is a match for the known face(s)
            match = face_recognizer_module.compare_faces(known_faces, face_encoding, tolerance=0.50)
            name = "Unknown"

            if match[0]:
                name = "Wiktor"
            elif match[1]:
                name = "Stonka"
            elif match[2]:
                name = "Blue Fox"

            face_names.append(name)

    process_this_frame = not process_this_frame  # negate

    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Press q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Stop the webcam
video_capture.release()
cv2.destroyAllWindows()
