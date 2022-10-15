
from kivymd.app import MDApp
from kivy.lang import Builder

from kivymd.uix.screen import MDScreen
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDFlatButton

kv="""
screen:

    BoxLayout:
        orientation:'vertical'
        canvas:
            Color:
                rgba:(87/255,84/255,212/255,100)
            Rectangle:
                size: self.size
        BoxLayout:
            orientation:'vertical'
            size_hint_y: 20
            height: self.minimum_height
            canvas:
                Color:
                    rgba:(217/255,217/255,217/255,100)
                Rectangle:
                    size: self.size
            BoxLayout:
                orientation:'horizontal'
                size_hint_y: 8
                height: self.minimum_height
                GridLayout:
                    cols:3
                    rows:3
                    MDLabel:
                        text:"Connexion"
                       
                        theme_text_color:"Custom"
                        text_color:(87/255,84/255,212/255,100)
                        font_style:'H6'
                        font_name:'Roboto'
                    MDLabel:
                        text:"Connexion"
                        halign:'center'
                        theme_text_color:"Custom"
                        text_color:(87/255,84/255,212/255,100)
                        font_style:'H3'
                        font_name:'Roboto'
                    MDLabel:
                        text:"S'identifier"
                       
                        theme_text_color:"Custom"
                        text_color:(87/255,84/255,212/255,100)
                        font_style:'H6'
                        font_name:'Roboto'
                    MDLabel:
                        text:"Pseudo :"
                        halign:'center'
                        theme_text_color:"Custom"
                        text_color:(87/255,84/255,212/255,100)
                        font_style:'H6'
                        font_name:'Roboto'
                    MDTextField:
                        padding_bottom:10
                        hint_text: "Round mode"
                        mode: "round"
                        max_text_length: 15
                        helper_text: "Massage"
                    MDLabel:
                        text:"S'identifier"
                       
                        theme_text_color:"Custom"
                        text_color:(87/255,84/255,212/255,100)
                        font_style:'H6'
                        font_name:'Roboto'
                    MDLabel:
                        text:"S'identifier"
                       
                        theme_text_color:"Custom"
                        text_color:(87/255,84/255,212/255,100)
                        font_style:'H6'
                        font_name:'Roboto'
                    MDLabel:
                        text:"S'identifier"
                       
                        theme_text_color:"Custom"
                        text_color:(87/255,84/255,212/255,100)
                        font_style:'H6'
                        font_name:'Roboto'
                    MDLabel:
                        text:"S'identifier"
                       
                        theme_text_color:"Custom"
                        text_color:(87/255,84/255,212/255,100)
                        font_style:'H6'
                        font_name:'Roboto'
                    
            BoxLayout:
                orientation:'vertical'
                height: self.minimum_height
                canvas:
                    Color:
                        rgba:(217/255,217/255,43/255,100)
                    Rectangle
                        size:self.size
                    
            
            
            
                
        
        
        BoxLayout:
            orientation:'vertical'
            canvas:
                Color:
                    rgba:(87/255,84/255,212/255,100)
                Rectangle:
                    size: self.size
"""


class relative(MDRelativeLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class screen(MDScreen):
      pass

class Test(MDApp):
       
        def build(self):
            
            return Builder.load_string(kv)


Test().run()