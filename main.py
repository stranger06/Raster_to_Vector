# Convert Raster image to Vector image

from PIL import Image
import numpy as np
import matplotlib.pyplot as pt
import matplotlib.image as mpimg
#import mahotas as mh

temp = Image.open('___') # name here
temp = temp.convert('1')
A = np.array(temp)
ima = np.empty((A.shape[0], A.shape[1]), None)

for i in range(len(A)):
    for j in range(len(A[i])):
        if A[i][j] == True:
            ima[i][j] = 0
        else:
            ima[i][j] = 1

x = []
y = []
c = 1

# LEFT
for j in range(len(ima)):
    for i in range(len(ima[0])):
        if ima[j][i] == 1:
            x.append(i)
            y.append(j)
            if c == 2:
                if y[-1]-y[-2] == 1 and x[-2]-x[-1] > 6:
                    x.clear()
                    y.clear()
                    c = 1
                    j = i
                    i = 0
                    break
                if y[-1]-y[-2] == 1 and x[-1]-x[-2] > 6:
                    j = len(ima)
                    break
                    
            else:
                lim_tl = i
                c = 2
            ima[j][i] = 0
            lim_lx = i
            lim_ly = j
            break

temp_x = [0]
temp_y = [0]
w = 0


for j in range(len(ima)):
    for i in range(len(ima[0])-1,0,-1):
        if ima[j][i] == 1 and i>0.5*len(ima[0]):
            temp_x.append(i)
            temp_y.append(j)
            if temp_y[-1]-temp_y[-2] == 1 and temp_x[-2]-temp_x[-1] > 6:
                w = 1
                break
            lim_rx = i
            lim_ry = j
            break
            
    if w == 1:
        break


#BOTTOM
for i in range(lim_lx+1,lim_rx):
    for j in range(len(ima)-1,0,-1):
        if ima[j][i] == 1:
            x.append(i)
            y.append(j)
            ima[j][i] = 0
            break

w = 0
#RIGHT
for j in range(lim_ry,0,-1):
    for i in range(len(ima[0])-1,0,-1):
        if ima[j][i] == 1:
            if y[-1]-j == 1 and x[-1]-i > 6:
                w = 1
                break
            x.append(i)
            y.append(j)
            ima[j][i] = 0
            lim_tr = i
            lim_ty = j
            break
            
    if w == 1:
        break

#TOP
for i in range(lim_tr-1, lim_tl, -1):
    for j in range(int(0.5*len(ima))):
        if ima[j][i] == 1:
            x.append(i)
            y.append(j)
            break


fig, ax = pt.subplots(1,2)
ax[0].imshow(ima, cmap='Greys',  interpolation='nearest')
ax[0].set_title("Original Raster Image")
ax[1].plot(x,y,color='black')
ax[1].set_title("Transformed Vector Image")
pt.xlim(0,len(ima[0]))
pt.ylim(len(ima),0)
pt.gca().set_aspect('equal')
pt.savefig("__") # name here
pt.show()
