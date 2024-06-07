from depthai_sdk import OakCamera

with OakCamera(rotation=90) as oak:
    cams = oak.create_all_cameras()
    oak.visualize(cams, fps=True)
    oak.start(blocking=True)