from kivy.app import App
from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget
from kivy.uix.scrollview import ScrollView
class WidgetLayoutE(GridLayout):
    count=1
    value=50
    my_text=StringProperty(str(count))
    slider_text=StringProperty(str(value))
    count_enabled=BooleanProperty(True)
   # progress_value=
    def on_Button_click(self):

           if self.count_enabled==False:
               self.count +=1
               print("button pressed")
               self.my_text=str(self.count)
           else:
               print("deactivated")



    def on_click_toggle(self, widget):
        print("toggle pressed: "+ widget.state)


        if widget.state=="normal":
            widget.text='OFF'
            self.count_enabled=True
        else:
            widget.text="ON"
            self.count_enabled=False

    def on_slider_value(self,widget):
        print("value :"+ str(int(widget.value)))
        self.value=str(int(widget.value))
        self.slider_text=self.value
        self.progress_value=int(widget.value)
        #print(self.progress_value)







class ScrollViewE(ScrollView):


    pass
class StackLayoutExample(StackLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.orientation="rl-tb"

        for i in range(1,100):

          b=Button(text=str(i),size_hint=(None,None),size=(dp(100),dp(100)))
          self.add_widget(b)




class GridLayoutExample(GridLayout):
    pass


class AnchorLayoutExample(AnchorLayout):
    pass




class MainWidget(Widget):
    pass

class TheLabApp(App):
    pass

TheLabApp().run()