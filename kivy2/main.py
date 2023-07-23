from kivy.app import App
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Line, Rectangle, Ellipse
from kivy.metrics import dp
from kivy.properties import StringProperty, Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
class CanvasExample7(BoxLayout):
    pass

class CanvasExample4(Widget):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Line(points=(100,100,200,400),width=2)
            Color(0, 255, 255)
            Line(circle=(200,200,100),width=2)
            self.rect= Rectangle(pos=(0,0),size=(150,100))

    def on_button_click(self):

        x,y=self.rect.pos
        w,h=self.rect.size
        inc=dp(10)
        diff_w=self.width-(x+w)
        diff_h=self.height-(y+h)
        if diff_w>10:
            inc=dp(10)
        if diff_w<10 and diff_w>5:
            inc=dp(5)
        if diff_w<5 and diff_w>0:
            inc=dp(1)
        if diff_w==0:
            inc=dp(0)


        x+=inc
        y=(2/3)*x+10
        self.rect.pos=(x,y)

    def on_button_click_negative(self):
        x,y=self.rect.pos
        x-=dp(10)
        y=(2/3)*x+10
        self.rect.pos=(x,y)



class CanvasExample3(Widget):
    pass
class CanvasExample6(Widget):
    pass

class CanvasExample2(Widget):
    pass
class CanvasExample(Widget):
    pass

class WidgetLayoutE(GridLayout):
    count=0
    value=50

    my_text=StringProperty(str(count))
    input_text=StringProperty("fog")
    #slider_text=StringProperty(str(value))

    def on_toggle_click(self,widget):
        self.count+=1
        self.my_text=str(self.count)

    def on_slider_value(self,widget):
        #print(int(widget.value))
        self.value=str(int(widget.value))
       # self.slider_text=str(int(widget.value))

        #self.progress_value=str(self.k)
    def switch_on_active(self,widget):
        print(widget.active)

    def on_text_validate(self,widget):
        self.input_text=widget.text
class CanvasExample5(Widget):
    def __init__(self,**Kwargs):
        super().__init__(**Kwargs)
        with self.canvas:
           self.c_size=dp(10)
           self.vx=dp(3)
           self.vy=dp(3)

           self.elli= Ellipse(pos=(self.center_x,self.center_y),size=(self.c_size,self.c_size))

        Clock.schedule_interval(self.update,1/60)

    def on_size(self,*args):
        #print(self.width,self.height)
        self.elli.pos=(self.center_x-self.c_size/2,self.center_y-self.c_size/2)

    def update(self,dt):


        x,y=self.elli.pos
        x+=self.vx
        y+=self.vy
        if y+self.c_size>self.height:
            y=self.height-self.c_size
            self.vy=-self.vy
        if x+self.c_size>self.width:
            x=self.width-self.c_size
            self.vx=-self.vx
        #print(x,y)
        #print(self.vy)
        if x<0:
            x=0
            self.vx=-self.vx
        if y<0:
            y=0
            self.vy=-self.vy








        self.elli.pos=(x,y)








class TheLabApp(App):
    pass
TheLabApp().run()