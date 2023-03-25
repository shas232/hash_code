import face_recognition
import numpy as np
import argparse
import imutils
import cv2
import time
import os

video_capture = cv2.VideoCapture(0)

obama_image = face_recognition.load_image_file("image.jpeg")
obama_face_encoding = face_recognition.face_encodings(obama_image)[0]

process_this_frame = True

while process_this_frame:

     ret, frame = video_capture.read()

      small_frame = cv2.resize(frame, (0, 0), fx=1, fy=1)

       face_locations = face_recognition.face_locations(small_frame)
        face_encodings = face_recognition.face_encodings(
            small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:

             match = face_recognition.compare_faces(
                  [_face_encoding], face_encoding)
              name = ""

               if match[0]:
                    name = ""
                    wi.destroy()
                    func()
                    process_this_frame = False
                    # wi.mainloop()

                face_names.append(name)

        #process_this_frame = not process_this_frame

        for (top, right, bottom, left), name in zip(face_locations, face_names):

            top *= 1
            right *= 1
            bottom *= 1
            left *= 1

            cv2.rectangle(frame, (left, top),
                          (right, bottom), (51, 221, 82), 2)

            cv2.rectangle(frame, (left, bottom - 35),
                          (right, bottom), (51, 221, 82), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6),
                        font, 1.0, (255, 255, 255), 1)

        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
