import cv2
import os

index = 1

while True:
    cam = cv2.VideoCapture(0)

    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break

    cv2.imshow("camera", frame)

    k = cv2.waitKey(1)
    if k % 256 == 27:
        break
    elif k % 256 == 32:
        name = "image{}.png".format(index)
        image = "img/image{}.png".format(index)
        cv2.imwrite(image, frame)
        print("{} written".format(name))
        index += 1

    cam.release()

path = 'img/'
file_list = os.listdir(path)

for file in file_list:
    image = cv2.imread(path + file)
    height, width, _ = image.shape
    if height > 224 or width > 224:
        src = cv2.resize(image, dsize=(224, 224), interpolation=cv2.INTER_AREA)
        cv2.imwrite(path + file, src)
        cv2.imshow('image', src)
    else:
        cv2.imshow('image', image)
    cv2.waitKey(0)

cv2.destroyAllWindows()
