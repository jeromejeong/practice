import cv2
import numpy as np
import sys
import getopt

argv=sys.argv[1:]

try:
    opts, args=getopt.getopt(argv, "r:n:c:")
except:
    print("error")
    opts=[]

for opt, arg in opts:
    if opt in ['-r']:
        imgsource=arg	
    elif opt in ['-n']:
        n=int(arg)
    elif opt in ['-c']:
        contrast=int(arg)

print(imgsource,n,contrast)
print(opts)   


def truncate(value):
    if value < 0:
        value=0
    elif value > 255:
        value=255
    return value



#image route
image=cv2.imread(imgsource)

#print image information 
wsize=image.shape[1]
hsize=image.shape[0]
print("width=",wsize," ","height=",hsize," ", "channel=",image.shape[2])

#shrink image
divwsize=wsize//n
divhsize=hsize//n

simage=cv2.resize(image,dsize=(divwsize,divhsize),interpolation=cv2.INTER_AREA)
newsimage=np.array(simage)


#give a contrast

factor = (259*(contrast+255))/ (255*(259-contrast))

for i in range(divhsize):
    for j in range(divwsize):
        for k in range(3):
            newsimage[i,j,k]=truncate(factor*(simage[i,j,k]-128)+128)
                    

#convert to grayscale image
grayimage=cv2.cvtColor(newsimage, cv2.COLOR_BGR2GRAY)

#define 5 colors
black=(0,0,0)
white=(255,255,255)
yellow=(0,230,235)
darkgray=(100,100,100)
gray=(200,200,200)

#pixel color change to 5 colorsd
for i in range(divhsize):
    for j in range(divwsize):
        if grayimage[i,j]<60:
            simage[i,j]=black
        elif grayimage[i,j]<110:
            simage[i,j]=darkgray
        elif grayimage[i,j]<160:
            simage[i,j]=gray
        elif grayimage[i,j]<230:
            simage[i,j]=white
        else:
            simage[i,j]=yellow

#get the image bigger
againbigimage=cv2.resize(simage,dsize=(wsize,hsize),interpolation=cv2.INTER_AREA)            

##cv2.imshow("zzazan0",image)
##cv2.imshow("zzazan1",simage)
cv2.imshow("zzazan2",againbigimage)
##cv2.imshow("zzazan3",grayimage)
##cv2.imshow("zzazan4",newsimage)
cv2.waitKey(0)
