import cv2

img = cv2.imread('background.jpg')
h, w, _ = img.shape

p1, p2 = (20, h // 2), (w - 20, h // 2)
cv2.arrowedLine(img, p1, p2, (0, 255, 0), 3, tipLength=0.03)
cv2.arrowedLine(img, p2, p1, (0, 255, 0), 3, tipLength=0.03)

cv2.putText(img, f"Width: {w}px", (w // 2 - 80, h // 2 - 15), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

# Save and show
cv2.imwrite('output.jpg', img)
cv2.imshow('Width', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
