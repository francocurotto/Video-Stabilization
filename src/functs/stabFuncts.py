import numpy as np
import cv2
from matplotlib import pyplot as plt
from drawMatches import drawMatches

def getVideoArray (videoPath):
    # video in info
    video = cv2.VideoCapture(videoPath)
    N_FRAMES = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    FPS = video.get(cv2.CAP_PROP_FPS)
    VID_WIDTH = video.get(cv2.CAP_PROP_FRAME_WIDTH)
    VID_HEIGHT = video.get(cv2.CAP_PROP_FRAME_HEIGHT)
    print "N_FRAMES: " + str(N_FRAMES)
    print "FPS: " + str(FPS)

    # numpy array
    videoArr = np.zeros((N_FRAMES, VID_HEIGHT, VID_WIDTH), dtype=np.uint8)
    # fill array
    for i in range(N_FRAMES):
        _, videoArr[i,:,:] = readVideoGray(video)
    video.release()
    return videoArr

def readVideoGray (video):
    ret, frame = video.read()
    if ret:
        frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        frameGray = None
    return ret, frameGray

def filterMatches (matches, MATCH_THRES):
    goodMatches = []
    for m in matches:
        if m.distance < MATCH_THRES:
            goodMatches.append(m)
    return goodMatches

def maskMatches (matches, mask):
    goodMatches = []
    for i in range(len(matches)):
        if mask[i] == 1:
            goodMatches.append(matches[i])
    return goodMatches

def plotMatches(frame1, kp1, frame2, kp2, matches, nFrame):
    imMatches = drawMatches(frame1, kp1, frame2, kp2, matches)
    imName = "Matches between frame " + str(nFrame) + " and frame " + str(nFrame+1)
    #cv2.namedWindow(imName, cv2.WINDOW_AUTOSIZE);
    cv2.namedWindow(imName, cv2.WINDOW_NORMAL);
    cv2.resizeWindow(imName, 1280, 480)
    cv2.imshow(imName, imMatches)
    cv2.waitKey(0)
    cv2.destroyWindow(imName)
    cv2.imwrite("frame matching.png", imMatches)

def plotTrans(Macc, Macc2, videoName, suffix, show):
    title = [["$m_{11}$", "$m_{12}$", "$t_x$"], ["$m_{21}$", "$m_{22}$", "$t_y$"], ["$m_{31}$", "$m_{32}$", "1"]]
    #plotPos = [321, 322, 325, 323, 324, 326]
    plt.figure(1)
    for i in range(3):
        for j in range(3):
            ax = plt.subplot(331+3*i+j)
            plt.plot(Macc[i,j,:], '-')
            if Macc2 is not None:
                plt.plot(Macc2[i,j,:], 'g-')
            plt.title(title[i][j])
            ax.autoscale_view(True, True, True)
            plt.grid(True)
            plt.xticks(np.arange(0, len(Macc[i,j,:]), 100))
            #plt.figure(num=1, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')
    plt.tight_layout()
    plt.savefig(videoName + suffix + ".pdf")#, figsize=(80, 60), dpi=80)#, bbox_inches='tight')
    if show:
        plt.show()
    plt.clf()

# Peak Signal to Noise Ratio
def getPSNR (frame1, frame2):
    MSE = ((frame2-frame1)**2).mean()
    I_MAX_SQR = 255.0**2
    return 10*np.log10(I_MAX_SQR/MSE)

# interframe video fidelity
def getITF (videoPath):
    video = cv2.VideoCapture(videoPath)
    N_FRAMES = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    ITF = 0

    _, currFrame = readVideoGray(video)
    for i in range(N_FRAMES-1):
        _, nextFrame = readVideoGray(video)
        ITF += getPSNR(currFrame, nextFrame)
        currFrame = nextFrame

    ITF = 1.0/(N_FRAMES-1) * ITF
    video.release()
    return ITF
