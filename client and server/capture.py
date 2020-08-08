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
        name = "img{}.png".format(index)
        image = "img/img{}.png".format(index)
        cv2.imwrite(image, frame)
        print("{} written".format(name))
        index += 1

    cam.release()

path = 'img/'
file_list = os.listdir(path)

for file in file_list:
    src = cv2.imread(path + file, cv2.IMREAD_COLOR)

    dst = cv2.resize(src, dsize=(244, 244), interpolation=cv2.INTER_AREA)
    #dst2 = cv2.resize(src, dsize=(0, 0), fx=0.3, fy=0.7, interpolation=cv2.INTER_LINEAR)

    #cv2.imshow("src", src)
    if (dst.shape[0] == 244) and (dst.shape[1] == 244):
        cv2.imshow("dst", dst)
    else:
        print('error')
    #cv2.imshow("dst2", dst2)
    os.remove(path + file)
    cv2.waitKey(0)

    #image = cv2.imread(path+file)
    #cv2.imshow('img', image)
    #cv2.waitKey(0)


cv2.destroyAllWindows()
