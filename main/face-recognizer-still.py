import face_recognizer_module  # module with defined face recognition functions
import cv2
from PIL import Image

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
unknown_image = face_recognizer_module.load_image_file("face26.jpg")
face_locations = face_recognizer_module.face_locations(unknown_image)
face_encodings = face_recognizer_module.face_encodings(unknown_image, face_locations)

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
        name = "Gawor"

    face_names.append(name)

# Display the results
for (top, right, bottom, left), name in zip(face_locations, face_names):

    # Draw a box around the face
    cv2.rectangle(unknown_image, (left, top), (right, bottom), (255, 0, 0), 2)

    # Draw a label with a name below the face
    cv2.rectangle(unknown_image, (left, bottom - 35), (right, bottom), (255, 0, 0), cv2.FILLED)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(unknown_image, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

pil_image = Image.fromarray(unknown_image)
pil_image.show()
pil_image.save("test.png")