import cv2 as cv
# from canvas import create_canvas
import canvas
from utilities import show_in_matplotlib

# img = create_canvas(100,200,(255,255,255))
img = canvas.create_canvas(100, 200, (255, 255, 255))

s = 40
p = 5  # padding
r = 0
(l, t) = (r+p, p)
(r, b) = (l+s, t+s)
cv.rectangle(img, (l, t), (r, b), (255, 0, 0), -1)

(l, t) = (r+p, p)
(r, b) = (l+s, t+s)
cv.rectangle(img, (l, t), (r, b), (0, 255, 0), -1)

(l, t) = (r+p, p)
(r, b) = (l+s, t+s)
cv.rectangle(img, (l, t), (r, b), (0, 0, 255), -1)

(l, t) = (r+p, p)
(r, b) = (l+s, t+s)
cv.rectangle(img, (l, t), (r, b), (0, 0, 0), -1)

r = 0
p = 50
(l, t) = (r+5, p)
(r, b) = (l+s, t+s)
cv.rectangle(img, (l, t), (r, b), (255, 255, 0), -1)

(l, t) = (r+5, p)
(r, b) = (l+s, t+s)
cv.rectangle(img, (l, t), (r, b), (255, 0, 255), -1)

(l, t) = (r+5, p)
(r, b) = (l+s, t+s)
cv.rectangle(img, (l, t), (r, b), (0, 255, 255), -1)

(l, t) = (r+5, p)
(r, b) = (l+s, t+s)
cv.rectangle(img, (l, t), (r, b), (255, 255, 255), -1)

cv.imwrite('color_img.png', img)

show_in_matplotlib(img, None)
