import cv2

class Camera:
    def __init__(self):
        self.camera = cv2.VideoCapture(1)
        if not self.camera.isOpened():
            raise ValueError("Camera not found")

        self.width = self.camera.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.camera.get(cv2.CAP_PROP_FRAME_HEIGHT)
        
    def get_frame(self):
        if self.camera.isOpened():
            ret, frame = self.camera.read()

            if ret:
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                return ret, None
        else:
            return None

    def __del__(self):
        if self.camera.isOpened():
            self.camera.release()