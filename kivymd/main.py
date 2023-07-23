from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField


class MainApp(MDApp):
    def build(self):
        screen=Screen()
        screen.add_widget(
            MDRectangleFlatButton(
                text="hii",
                pos_hint={"center_x":0.5,"center_y":0.5},

            )
        )
        screen.add_widget(
            MDTextField(
                id="Link_text",
                hint_text="enter something.."
            )
        )
        return screen



if __name__ == '__main__':
    MainApp().run()