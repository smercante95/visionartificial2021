import cv2

video = cv2.VideoCapture('TP3y4.mp4')
fps = video.get(cv2.CAP_PROP_FPS)
waitKey_Value = int(1000 / fps)
print('El video tiene un frame rate de', fps)
while (video.isOpened()):
    ret, frame = video.read()
    if ret is True:
        cv2.imshow('Video en curso', frame)
        if (cv2.waitKey(waitKey_Value) & 0xFF == ord('q')):
            break
    else:
        break

video.release()
cv2.destroyAllWindows()