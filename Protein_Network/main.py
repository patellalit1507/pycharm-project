
from kivy.lang import builder
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.filemanager import MDFileManager
import pyrebase
builder.Builder.load_file("MainLayout.kv")
from kivy.core.window import Window
Window.size=(350,660)
class MainScreen(Screen):

    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        config={
            "apiKey": "AIzaSyDWnfAQNgN_9_JEpeZdbKKrddrmgYP2yYY",
            "authDomain": "proteinnetwork-445cb.firebaseapp.com",
            "databaseURL": "https://proteinnetwork-445cb-default-rtdb.firebaseio.com",
            "projectId": "proteinnetwork-445cb",
            "storageBucket": "proteinnetwork-445cb.appspot.com",
            "serviceAccount":"ServiceAccountKey.json"
        }
        firebase_storage=pyrebase.initialize_app(config)
        self.storage=firebase_storage.storage()
        self.file_manager_obj=MDFileManager(
            select_path=self.select_path,
            exit_manager=self.exit_manager,
            preview=True
        )
    def select_path(self,path):
        self.path=path
        self.ids.image.source=path
        self.exit_manager()
    def open_file_manager(self):
        self.file_manager_obj.show('C:/Users/ASUS/Desktop')
    def exit_manager(self):
        self.file_manager_obj.close()
    def upload(self):
        pro_name=self.ids.product_name.text
        pro_price=self.ids.product_price.text
        pro_id=self.ids.product_id.text
        desc=self.ids.product_desc.text
        self.storage.child(f'products/{pro_id}.JPG').put(self.path)
    def clear(self):
        self.ids.product_name.text=""
        self.ids.product_price.text=""
        self.ids.product_id.text=""
        self.ids.product_desc.text=""
        self.ids.image.source =""


class MainApp(MDApp):
    def build(self):
        return MainScreen()

if __name__ == '__main__':
    root=MainApp()
    root.run()

