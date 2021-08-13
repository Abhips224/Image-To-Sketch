import cv2

image=cv2.imread("captain_america.jpg")
gray_scale=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

invert_image = 255 - gray_scale
blur_image = cv2.GaussianBlur(invert_image, (21, 21), 0)
invert_blur = 255 - blur_image
pencil_sketch = cv2.divide(gray_scale, invert_blur, scale=256.0)
cv2.imshow("org_img",image)
cv2.imshow("image",pencil_sketch)

cv2.waitKey(0)
