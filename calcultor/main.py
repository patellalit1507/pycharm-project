from sys import maxsize
from kivy.config import Config

# 0 being off 1 being on as in true / false
# you can use 0 or 1 && True or False
Config.set('graphics', 'resizable', True)
from kivy.app import App
from kivy.properties import NumericProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout


class MainWidgetE(BoxLayout):
    text_input=StringProperty()

    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.stack=self.CreateStack()
        self.stack2=self.CreateStack()
        self.count=0
        self.expr=''

    def on_Button_click(self,widget):
        char=widget.text


        if char=="C":
            self.text_input=""
            self.stack=[]
            self.count=0
        elif char=="=":
            k=len(self.text_input)

            self.push(self.stack, self.text_input[self.count:])
            self.text_input=str(self.Calculate())
            self.stack=[]
            self.count=0
            self.expr=''

        elif char=="(":
            self.push(self.stack,char)
            self.text_input=self.text_input+char
            self.count=self.count+1

        elif char==")":
            self.push(self.stack,self.text_input[self.count:])
            self.push(self.stack,char)
            self.text_input = self.text_input + char
            self.count = len(self.text_input)
        elif char=="+" or char=="-" or char=="/" or char=="*" or char=="%":
            if self.count==0:
               self.push(self.stack,self.text_input)
               self.text_input=self.text_input+str(char)
            else:
                self.push(self.stack, self.text_input[self.count:])
                self.text_input = self.text_input + str(char)
            self.push(self.stack,char)
            self.count=len(self.text_input)



        else:
            self.text_input=self.text_input+str(char)



    def CreateStack(self):
        self.Stack=[]
        return self.Stack

    def isEmpty(self,stack):
        return len(stack) == 0

    def push(self,stack, key):
        stack.append(key)
        print(key + " pushed to stack")

    def pop(self,stack):
        if (self.isEmpty(stack)):
            return str(-maxsize - 1)
        return stack.pop()
    def Calculate(self):
        for i in self.stack:
           self.expr+=str(i)
        print(self.expr)
        result=self.Evaluation(self.expr)
        return  result

    def Precedence(self,op):
        if op=="+" or op=="-":
            return 1
        if op=="*" or op=="/":
            return 2
        return 0

    def applyOp(self,a, b, op):

        if op == '+': return a + b
        if op == '-': return a - b
        if op == '*': return a * b
        if op == '/': return a // b
    def Evaluation(self,token):
        value=[]  #stock to store int value
        op=[]
        i=0
        while i<len(token):
            if token[i]==" ":
                i+=1
                continue
            elif token[i]=="(":
                op.append(token[i])
            elif token[i].isdigit():
                val=0
                while i<len(token) and token[i].isdigit():
                   val=(val*10)+int(token[i])
                   i+=1
                value.append(val)
                i-=1
            elif token[i]==")":
                while len(op)!=0 and op[-1]!="(":
                    val2=value.pop()
                    val1=value.pop()
                    ops=op.pop()
                    value.append(self.applyOp(val1,val2,ops))
                op.pop()
            else:
                while len(op)!=0 and self.Precedence(op[-1])>=self.Precedence(token[i]):
                    val2=value.pop()
                    val1=value.pop()
                    ops=op.pop()
                    value.append(self.applyOp(val1,val2,ops))
                op.append(token[i])

            i+=1
        while len(op)!=0:
            val2 = value.pop()
            val1 = value.pop()
            ops = op.pop()

            value.append(self.applyOp(val1, val2, ops))
        return value[-1]







class TheLab(App):
    pass

TheLab().run()