from kivmob import KivMob, TestIds, RewardedListenerInterface
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.progressbar import ProgressBar
from kivy.uix.togglebutton import ToggleButton
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from pytube import YouTube
from kivy.utils import platform
import urllib3
import os

Builder.load_file("layout.kv")  # loading kivy file


class MainWidget(Screen):

    def on_press(self, vid):
        url = str(vid)
        self.Search(url)

    def Search(self, url):
        self.Url = YouTube(url)
        res = set()
        co = 0
        self.bo_layout = BoxLayout(orientation="horizontal", pos_hint={"x": 0.05, "y": 0.50}, size_hint=(0.9, 0.3),
                                   spacing=10)
        self.add_widget(self.bo_layout)
        self.progress_bar = ProgressBar(value=0, pos_hint={"center_x": 0.5, "center_y": 0.19}, size_hint=(0.4, 0.1),
                                        width="3dp")
        self.add_widget(self.progress_bar)
        self.label_pro = Label(pos_hint={"center_x": 0.5, "center_y": 0.08}, text=' ', color="black")
        self.add_widget(self.label_pro)
        self.ids.thumbnail.source = self.Url.thumbnail_url
        self.ids.vid_title.text = self.Url.title
        for i in self.Url.streams:
            if i.resolution == None:
                pass
            else:
                if i.resolution not in ("1080p", "2040p", "1440p", "2160p"):
                    res.add(i.resolution)
        for i in res:
            btn = ToggleButton(pos_hint={"x": 0.1 + co, "y": 0.6}, size_hint=(0.1, 0.08), text=str(i))
            self.bo_layout.add_widget(btn)
            btn.id = str(i)
            btn.bind(on_press=self.Downloader)

            co += 0.13

        print(res)

    def Downloader(self, btn):
        video_url = self.Url.streams.filter(res=btn.text, progressive=True).first()
        print(video_url)

        def on_progess(stream, chunk, bytes_remaining):
            print("downloading started")
            size = video_url.filesize
            progress = int(((size - bytes_remaining) / size) * 100)
            self.progress_bar.value = progress
            self.label_pro.text = f'{progress}%'

        def on_complete(stream, file_handle):
            print("download complete")

        self.Url.register_on_progress_callback(on_progess)
        self.Url.register_on_complete_callback(on_complete)

        try:
            if video_url != None:
                if platform == "android":
                    video_url.download("/storage/emulated/0/downtube/", filename=str(self.Url.title))
            else:
                if platform == "android"
                    video_url = self.Url.streams.first()
                    video_url.download("/storage/emulated/0/downtube/", filename=str(self.Url.title))
        except:
            print("some Error Occured")


class TheLabApp(MDApp):
    ads = KivMob(TestIds.APP)

    def build(self):
        self.ads.new_banner(TestIds.BANNER, False)
        self.ads.request_banner()
        self.ads.show_banner()
        return MainWidget()

    def on_start(self):
        if platform == "android":
            from android.permissions import request_permissions, Permission
            request_permissions([Permission.READ_EXTERNAL_STORAGE,Permission.WRITE_EXTERNAL_STORAGE])
            if os.path.exists("/storage/emulated/0/downtube") == 0:
                os.mkdir("/storage/emulated/0/downtube")


TheLabApp().run()