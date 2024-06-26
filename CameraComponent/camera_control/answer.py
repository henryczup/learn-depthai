from depthai_sdk import OakCamera

with OakCamera() as oak:
    color = oak.create_camera('color')

    oak.visualize([color], scale=.6, fps=True)

    oak.start()

    while True:
        key = oak.poll()

        if key == ord('i'):
            color.control.exposure_time_down()
        elif key == ord('o'):
            color.control.exposure_time_up()
        elif key == ord('k'):
            color.control.sensitivity_down()
        elif key == ord('l'):
            color.control.sensitivity_up()
        elif key == ord('e'):
            color.control.send_controls({'exposure_time': {'auto': True}})