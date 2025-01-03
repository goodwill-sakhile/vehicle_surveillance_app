import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang import Builder
root = Builder.load_string("""
<MainVehicleSurveillanceScreenBox>:
    md_bg_color:47/float(255), 79/float(255), 79/float(255), 1
    MDScreen:
        name:"main_screen"
        MDBoxLayout:
            orientation:"vertical"
            MDBoxLayout:
                padding:10
                spacing:10
                MDBoxLayout:
                    radius:10, 10, 10, 10
                    md_bg_color:220/float(255), 220/float(255), 220/float(255), 0.5
                MDBoxLayout:
                    size_hint_x:None
                    width:"200dp"
                    radius:10, 10, 10, 10
                    md_bg_color:220/float(255), 220/float(255), 220/float(255), 0.5
            MDBoxLayout:
                radius:10, 10, 10, 10
                size_hint_y:None
                height:"50dp"
                padding:5
                spacing:5
                MDBoxLayout:
                    radius:20, 20, 20, 20
                    md_bg_color:0, 0, 0, 1
                MDBoxLayout:
                    radius:20, 20, 20, 20
                    md_bg_color:0, 154/float(255), 220/float(255), 1
""")
class MainVehicleSurveillanceScreenBox(MDBoxLayout):
    pass
class VehicleSurveillanceApp(MDApp):
    def build(self):
        root = MainVehicleSurveillanceScreenBox()
        return root
if __name__ == "__main__":
    VehicleSurveillanceApp().run()
