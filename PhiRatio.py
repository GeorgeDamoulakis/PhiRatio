import cv2
import numpy as np
import matplotlib.pyplot as plt    # import all the necessary

#the main aim of this program is to find the black to white ratio of a picture

def show(img):    # this defines the "show" command - which shows the input image
    cv2.imshow('This is your image:', img)     # shows image
    cv2.waitKey(0)               # click any key to close image
    cv2.destroyAllWindows()       # close image window
    #plt.imshow(img, cmap="gray") # plots the image as an diagram
    #plt.show()

def counting_pixels(): # this defines the counting pixel process
    l1 = len(img)        # this is the length of the BIG array
    l2 = len(img[1])     # this is the length of the first array of the BIG array
    phil_pixels = 0       # this is the initial definition of the philic pixels

    # all the black or blackish pixels are superhyrophilic

    for i in range(l1):
        for j in range(l2):
            if img[i][j] < 127: # every object inside the array has a number from 0 (total black)
                                # to 255 (total white) . We want the black ones..
                phil_pixels += 1 # this is the blackish pixel counter

    print(f'Superhydrophilic pixels: ', phil_pixels)

    Tot_mm = 50.8 * 50.8 # this is the total area of interest. I want a square of 48.8 X 48.8 mm
                         # this is real dimensions
    scal = 1000 / 25.4;  # this is the scale factor for the picture
                         # this is the scale:  pixels/mm for 1000 ppi

    phil_mm = phil_pixels / (scal * scal)  # go from pixels to mm
    Phi_ratio = phil_mm / Tot_mm           # the phi ratio is the ultimate goal

    print(f'PHI ratio: ', round(Phi_ratio, 2)) # it's get rounded to 2 digits



img = cv2.imread('C:\\Users\\Dino\\PycharmProjects\\Phi_ratio\\wp08.tif',0) #this loads the image into grayscale

print('Program starts.')
print('Counting pixels...this will take a few seconds.')
print('The image will be open soon, to close image press any key.')

counting_pixels()
show(img)

print('Program ends.')





