import cv2

# Load image
img = cv2.imread('ayub.jpeg')

# Set start and end coordinates of rectangle
x1, y1 = 275, 190
x2, y2 = 555, 570

# Set color and thickness of rectangle
color = (0, 255, 0)
thickness = 2

# Set text to be added
text = "Hello, Ayyub"

# Set font, font scale, color, and thickness
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
color = (0, 0, 255)  # (G,B,R)
thickness = 2

# Set position of text
x = 320
y = 560
# Add text to image
cv2.putText(img, text, (x, y), font, font_scale, color, thickness)

# Draw rectangle on image
cv2.rectangle(img, (x1, y1), (x2, y2), color, thickness)

# Display image with rectangle overlay
cv2.imshow('Image Overlay', img)

# Wait for a key press and then exit
cv2.waitKey(0)
cv2.destroyAllWindows()
