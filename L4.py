import cv2
img=cv2.imread("Charizard.png")
startpoint =(0,100)
endpoint =(0,0)
color=(0,229,255)
thickness=10
r=cv2.line(img,startpoint,endpoint,color,thickness)
cv2.imshow("Image",r)
cv2.waitKey(0)
cv2.destroyAllWindows()