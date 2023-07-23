from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import  Window
Window.size=360,640
from kivy.lang import Builder
from kivy.utils import platform
from jnius import autoclass
Environment=autoclass('android.os.Environment')
path=Environment.getExternalStorageDirectory().getAbsolutePath()
import qrcode
import plyer

class Function(ScreenManager):
    def generate_qr_code(self,root):
        if self.ids.link_text!="" and self.ids.image_name!='':
            code=qrcode.QRCode(version=1.0,box_size=15,border=4)
            code.add_data(self.ids.link_text.text)
            code.make(fit=True)
            img=code.make_image(fill='Black',back_color="White")
            #img.save(f'{self.ids.image_name.text}.png')
            img.save(f'{path}/{self.ids.image_name.text}.png')
            plyer.notification.notify(
                title="QR code Generator", message="Qr code generated"
            )
        else:
            plyer.notification.notify(
                title="QR code Generator",message="type something in text fields"
            )
    def view_image(self,root):
        self.ids.img_.source=f'{path}/{self.ids.image_name.text}.png'
        root.current="image"
    def make_another(self,root):
        self.ids.image_name.text=''
        self.ids.link_text.text=''
        root.current="first"

class Main(MDApp):
    Builder.load_file("layout.kv")
    def build(self):
        return Function()
    def on_start(self):
        if platform=="android":
            from android.permission import request_permission, Permission
            request_permission([Permission.READ_EXTERNAL_STORAGE,Permission.WRITE_EXTERNAL_STORAGE])
if __name__ == '__main__':
    Main().run()