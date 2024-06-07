from depthai_sdk import OakCamera

with OakCamera(usb_speed='usb2') as oak:
    color = oak.create_camera('color', encode='h265')

    oak.visualize(color.out.encoded, scale=.6, fps=True)

    oak.visualize(color, scale=.6, fps=True)

    oak.start(blocking=True)
