from depthai_sdk import OakCamera

with OakCamera() as oak:
    cams = oak.create_all_cameras(resolution='max')
    oak.visualize(cams, scale=.6, fps=True)
    oak.start(blocking=True)