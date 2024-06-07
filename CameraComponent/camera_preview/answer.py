from depthai_sdk import OakCamera

with OakCamera() as oak:
    color = oak.create_camera('color')

    left = oak.create_camera('left')
    right = oak.create_camera('right')

    stereo = oak.create_stereo(left, right)

    oak.visualize([color, left, right, stereo.out.depth], scale=.6, fps=True)

    oak.start(blocking=True)
