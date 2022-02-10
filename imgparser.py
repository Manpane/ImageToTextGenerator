import numpy as np
import cv2
import os
import time
RADIUS = 2
PIXEL_LENGTH = 2
def getAppropriateChar(per):
    if per>90:
        return " "*PIXEL_LENGTH
    if per>80:
        return "."*PIXEL_LENGTH
    if per>70:
        return ","*PIXEL_LENGTH
    if per>60:
        return "^"*PIXEL_LENGTH
    if per>50:
        return "*"*PIXEL_LENGTH
    if per>40:
        return "="*PIXEL_LENGTH
    if per>30:
        return "O"*PIXEL_LENGTH
    if per>20:
        return "#"*PIXEL_LENGTH
    if per>-1:
        return "0"*PIXEL_LENGTH
def percentageOfColor(R,G,B):
    R_ = (R/255)*100
    B_ = (B/255)*100
    G_ = (G/255)*100
    per = int((R_+B_+G_)/3)
    return per
def getAveragePixelValue(i,j):
    global image
    if RADIUS==0:
        current = image[i][j]
        return percentageOfColor(current[0],current[1],current[2])
    total = 0
    count = 0
    for x in range(i-RADIUS,i+RADIUS):
        for y in range(j-RADIUS,j+RADIUS):
            if not (x<0 or y<0 or x>image.shape[0]-1 or y > image.shape[1]-1):
                current = image[x][y]
                total+=percentageOfColor(current[0],current[1],current[2])
                count+=1
    averagePer = total/count
    return averagePer
def createArt():
    global image,RADIUS
    startTime = time.time()
    tl = []
    i=0
    r=0
    if RADIUS == 0:
        r = 1
    else:
        r = RADIUS
    while i<image.shape[0]:
        lineString = ""
        j=0
        while j<image.shape[1]:
            lineString+=getAppropriateChar(getAveragePixelValue(i,j))
            j+=r
        i+=r
        tl.append(lineString)
    print("Finished in : ",format(time.time()-startTime,'.2f')," seconds")
    while True:
        destName = input("Enter name for final txt file :")
        if len(destName)>0:
            break
        else:
            print("Final name too short.")
    with open(f"{destName}.txt","w") as file:
        for line in tl:
            file.write("\t\t\t"+line+"\n")

    
while True:
    filename = ""
    while True:
        filename = input("Enter the image filename :")
        try:
            with open(filename,"rb") as f:
                break
        except Exception as e:
            print(str(e),"\n")

    image = np.array(cv2.imread(filename))
    createArt()
    os.system("cls")




