#_*_ coding: utf-8 _*_
import cv2

a,b = map(int,input().split())


#컬러
img = cv2.imread("./adsada.jpeg",cv2.IMREAD_COLOR)
#흑백
gray = cv2.imread("./adsada.jpeg",cv2.IMREAD_GRAYSCALE)
#컬러
unchange = cv2.imread("./adsada.jpeg",cv2.IMREAD_UNCHANGED)

cv2.imwrite("adsada.jpeg",img)
#크기조절
small = cv2.resize(img,None,fx = a,fy = b,interpolation = cv2.INTER_AREA)
#이미지를 회전
rows,cols = img.shape[:2]
m = cv2.getRotationMatrix2D((cols/2,rows/2),90,0.5)

dst = cv2.warpAffine(img,m,(cols,rows))
cv2.imshow("Rotation",dst)

cv2.imshow("shrink",small)
cv2.waitKey(0)
cv2.destroyAllWindows()
