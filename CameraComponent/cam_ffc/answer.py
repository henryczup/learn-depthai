from depthai_sdk import OakCamera

with OakCamera() as oak:
    cama = oak.create_camera('cama,c', '1200p')
    camb = oak.create_camera('camb,c', '1200p')
    camc = oak.create_camera('camc,c', '1200p')

    cama.config_color_camera(isp_scale=(2,3))
    camb.config_color_camera(isp_scale=(2,3))
    camc.config_color_camera(isp_scale=(2,3))

    stereo = oak.create_stereo(left=camb, right=camc)

    stereo.config_undistortion(0)

    oak.visualize([stereo, cama, camc, stereo.out.rectified_left], fps=True )

    oak.start(blocking=True)


