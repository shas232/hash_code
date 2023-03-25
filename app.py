import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
import cv2
import requests
import base64


class CameraApp(App):

    def build(self):
        self.capture = cv2.VideoCapture(0)
        self.layout = BoxLayout()
        self.image = Image()
        self.layout.add_widget(self.image)
        # Update the camera preview 30 times per second
        Clock.schedule_interval(self.update, 1.0 / 30.0)
        return self.layout

    def update(self, dt):
        ret, frame = self.capture.read()
        if ret:
            texture = Texture.create(
                size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
            texture.blit_buffer(
                frame.tobytes(), colorfmt='bgr', bufferfmt='ubyte')
            self.image.texture = texture

            # Convert the image to a base64-encoded string
            _, buffer = cv2.imencode('.jpg', frame)
            jpg_as_text = base64.b64encode(buffer).decode('utf-8')

            # Send the image to the server
            url = 'http://your-laptop-ip-address:5000/api/image'
            headers = {'Content-Type': 'application/json'}
            data = {'image': jpg_as_text}
            response = requests.post(url, headers=headers, json=data)


if __name__ == '__main__':
    CameraApp().run()
