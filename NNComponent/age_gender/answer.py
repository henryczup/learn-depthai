from depthai_sdk import OakCamera
from depthai_sdk.classes import TwoStagePacket
from depthai_sdk.visualize.configs import TextPosition
import cv2
import numpy as np

def Callback(packet: TwoStagePacket):
    visualizer = packet.visualizer
    for det, rec in zip(packet.detections, packet.nnData):
        age = int(float(np.squeeze(np.array(rec.getFirstLayerFp16('age_conv3')))) * 100)
        gen_prob = np.squeeze(np.array(rec.getFirstLayerFp16('prob')))
        gender_str = "Woman" if gen_prob[0] else "Man"
        visualizer.add_text(gender_str)
