from depthai_sdk import OakCamera

with OakCamera() as oak:
    color = oak.create_camera('color')

    nn = oak.create_nn('face-detection-retail-0004', color)

    color.control_with_nn(nn, auto_exposure=True, auto_focus=True, debug=False)

    oak.visualize([nn], fps=True)

    oak.start(blocking=True)