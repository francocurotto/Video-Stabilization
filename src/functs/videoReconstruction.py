import cv2
import os

def reconVideo (videoInPath, videoOutPath, trans, BORDER_CUT):
    # video in info
    videoIn = cv2.VideoCapture(videoInPath)
    N_FRAMES = int(videoIn.get(cv2.CAP_PROP_FRAME_COUNT))
    FPS = videoIn.get(cv2.CAP_PROP_FPS)
    FOURCC = videoIn.get(cv2.CAP_PROP_FOURCC)
    VID_WIDTH = videoIn.get(cv2.CAP_PROP_FRAME_WIDTH)
    VID_HEIGHT = videoIn.get(cv2.CAP_PROP_FRAME_HEIGHT)

    # video out creation
    videoInSize = (int(VID_WIDTH), int(VID_HEIGHT))
    videoOutSize = (int(VID_WIDTH) - 2*BORDER_CUT, int(VID_HEIGHT) - 2*BORDER_CUT)
    videoOut = cv2.VideoWriter(videoOutPath, int(FOURCC), FPS, videoOutSize)

    # frame transformation
    for i in range(N_FRAMES):
        ret, frame = videoIn.read()
        frameOut = cv2.warpPerspective(frame, trans[i,:,:], videoInSize, flags=cv2.INTER_NEAREST)
        frameOut = frameOut[BORDER_CUT:-BORDER_CUT, BORDER_CUT:-BORDER_CUT]
        videoOut.write(frameOut)

    videoIn.release()
    videoOut.release()
