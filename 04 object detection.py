import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
from gtts import gTTS
from playsound import playsound
import os

file = "./BootCamp.mp3"

def speech(text):
    print(text)
    lang = "en"
    output = gTTS(text=text, lang=lang, slow=True)
    output.save(file)
    playsound(file)

vid = cv2.VideoCapture(0)
labels = []

while True:
    ret, frame = vid.read()
    bbox, label, conf = cv.detect_common_objects(frame)
    output_image = draw_bbox(frame, bbox, label, conf)

    cv2.imshow("BootCamp-ObjDetection", output_image)

    for item in label:
        if item in labels:
            pass
        else:
            labels.append(item)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
i = 0
newSent = []
for label in labels:
    if i ==0:
        newSent.append(f"I Found a {label}, and, ")
    else:
        newSent.append(f"a {label}, ")
    
    i += 1

speech(" ".join(newSent))