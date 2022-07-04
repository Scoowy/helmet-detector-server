import cv2
from cv2 import VideoCapture


def getFpsFromVideo(video: VideoCapture):
    fps = video.get(cv2.CAP_PROP_FPS)
    return fps


def getOutputVideoWriter(filename, fps: float, dimensions: tuple[int, int]):
    fourcc = cv2.VideoWriter_fourcc(*'AVC1')
    output = cv2.VideoWriter(filename, fourcc, fps, dimensions)
    return output
