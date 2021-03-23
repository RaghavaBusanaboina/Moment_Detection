import cv2

vid = cv2.VideoCapture('videotest.avi')

_, frame1 = vid.read()
_, frame2 = vid.read()
while vid.isOpened():
    differnce = cv2.absdiff(frame1, frame2)
    grey_img = cv2.cvtColor(differnce, cv2.COLOR_BGR2GRAY)
    blur_img = cv2.GaussianBlur(grey_img, (5, 5), 0)
    x, thresh = cv2.threshold(blur_img, 20, 255, cv2.THRESH_BINARY)
    dilated_img = cv2.dilate(thresh, None, iterations=3)
    conters, x1 = cv2.findContours(dilated_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for conter in conters:
        (x, y, w, h) = cv2.boundingRect(conter)
        if cv2.contourArea(conter) < 700:
            continue
        else:
            cv2.rectangle(frame1, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow('out', frame1)
    frame1 = frame2
    ret, frame2 = vid.read()

    if cv2.waitKey(100) & 0xFF == ord('q'):
        break
vid.release()
cv2.destroyAllWindows()
