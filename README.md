## Introducción

This is an implementation of a video stabilization system using ORB descriptor. The input of the program is a video, and it outputs the stabilized video in the same folder. 

## Requirements

The program was written in Python. The libraries used are:

* OpenCV 3.1 (Use these instructions: http://docs.opencv.org/2.4/doc/tutorials/introduction/linux_install/linux_install.html#linux-installation)
* Numpy 1.8.2


## To run

to run the program simply use:

python videoStab.py [video]

Parameters must be changed manually in videoStap.py

* videoInPath:  path of the unstabilized video (optional)
* MATCH_THRES:  Matches distance threshold
* RANSAC_THRES: RANSAC threshold
* BORDER_CUT:   Number of pixel to crop in output video 
* FILT:         filter type (square or Gauss)
* FILT_WIDTH:   filter width
* FILT_SIGMA:   filter variance (only in Gaussian filter)
* FAST:         If true use the fast version of the algorithm
