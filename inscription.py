from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.properties import ListProperty, ObjectProperty , StringProperty
from kivy.graphics import Color,Rectangle,RoundedRectangle
from kivymd.uix.screen import MDScreen
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.menu import MDDropdownMenu

KV = '''
MDScreen:
    canvas:
        Color:
            rgba:(87/255,84/255,212/255,100)
        Rectangle:
            pos: self.pos
            size: self.size

        Color:
            rgba:(255/255,255/255,255/255,100)
        Rectangle:
            pos: (self.x,self.y+30)
            size:(self.width,self.height-60)

    BoxLayout:
        orientation:'vertical'
        
        
        MDLabel:
            size_hint_y: 2
            text:"CREER VOTRE COMPTE"
            halign:'center'
            theme_text_color:"Custom"
            text_color:(87/255,84/255,212/255,100)
            font_style:'H3'
            

        BoxLayout:
            orientation:'horizontal'
            
            BoxLayout:
                orientation:'horizontal'
                
                MDLabel:
                    text:"Nom:"
                    size_hint_X: 1
                    halign:'center'
                    theme_text_color:"Custom"
                    text_color:(0/255,0/255,0/255,100)
                    font_style:'H4'
                   

                MDTextField:
                    id: nom
                    width: "100dp"
                    mode: "round"
                    size_hint_x: 1.5
                    md_bg_color:(217/255,217/255,217/255,100)
                    size_hint_y: None
                    pos_hint: {"center_x": 0, "center_y": .5}
                    
            
            BoxLayout:
                orientation:'horizontal'
               
                MDLabel:
                    text:"Pseudo:"
                    size_hint_y: 1
                    halign:'center'
                    theme_text_color:"Custom"
                    text_color:(0/255,0/255,0/255,100)
                    font_style:'H4'

                MDTextField:
                    id: pseudo
                    width: "100dp"
                    mode: "round"
                    size_hint_x: 1.5
                    md_bg_color:(217/255,217/255,217/255,100)
                    size_hint_y: None
                    pos_hint: {"center_x": 0, "center_y": .5}



        BoxLayout:
            orientation:'horizontal'
            
            BoxLayout:
                orientation:'horizontal'
                
                MDLabel:
                    text:"Prénom:"
                    size_hint_X: 1
                    halign:'center'
                    theme_text_color:"Custom"
                    text_color:(0/255,0/255,0/255,100)
                    font_style:'H4'
                   

                MDTextField:
                    id: prenom
                    width: "100dp"
                    mode: "round"
                    size_hint_x: 1.5
                    md_bg_color:(217/255,217/255,217/255,100)
                    size_hint_y: None
                    pos_hint: {"center_x": 0, "center_y": .5}
            
            BoxLayout:
                orientation:'horizontal'
               
                MDLabel:
                    text:"Mot de passe:"
                    size_hint_X: 1
                    halign:'center'
                    theme_text_color:"Custom"
                    text_color:(0/255,0/255,0/255,100)
                    font_style:'H4'
                   

                MDTextField:
                    id: mdp
                    width: "100dp"
                    mode: "round"
                    size_hint_x: 1.5
                    md_bg_color:(217/255,217/255,217/255,100)
                    size_hint_y: None
                    pos_hint: {"center_x": 0, "center_y": .5}



        BoxLayout:
            orientation:'horizontal'
            
            BoxLayout:
                orientation:'horizontal'
               
                MDLabel:
                    text:"Téléphone:"
                    size_hint_X: 1
                    halign:'center'
                    theme_text_color:"Custom"
                    text_color:(0/255,0/255,0/255,100)
                    font_style:'H4'
                   

                MDTextField:
                    id: telephone
                    width: "100dp"
                    mode: "round"
                    size_hint_x: 1.5
                    md_bg_color:(217/255,217/255,217/255,100)
                    size_hint_y: None
                    pos_hint: {"center_x": 0, "center_y": .5}
            
            BoxLayout:
                orientation:'horizontal'
                
                MDLabel:
                    text:"Confirmation:"
                    size_hint_X: 1
                    halign:'center'
                    theme_text_color:"Custom"
                    text_color:(0/255,0/255,0/255,100)
                    font_style:'H4'
                   

                MDTextField:
                    id: confirmation
                    width: "100dp"
                    mode: "round"
                    size_hint_x: 1.5
                    md_bg_color:(217/255,217/255,217/255,100)
                    size_hint_y: None
                    pos_hint: {"center_x": 0, "center_y": .5}



        BoxLayout:
            orientation:'horizontal'
            
            BoxLayout:
                orientation:'horizontal'
                
                MDLabel:
                    text:"Fonction:"
                    size_hint_X: 1
                    halign:'center'
                    theme_text_color:"Custom"
                    text_color:(0/255,0/255,0/255,100)
                    font_style:'H4'
                   

                MDDropDownItem:
                    id: fonction
                    size_hint_x: 1.
                    pos_hint: {'center_x': .5, 'center_y': .5}
                    text: 'Sélectionnez'
                    on_release:  app.menu.open()
            
            BoxLayout:
                orientation:'horizontal'
                
                
                   



        BoxLayout:
            orientation:'horizontal'
            
            BoxLayout:
                orientation:'horizontal'
                
                
            BoxLayout:
                orientation:'horizontal'
               
                



        BoxLayout:
            orientation:'horizontal'
            
            AnchorLayout:
                anchor_x:'right'
                anchor_y:'center'
                size_hint_y: 1.9 
                size_hint_x: 1.
                MDRectangleFlatButton:
                    id: annuler
                    text:'    Annuler    '
                    text_color: "black"
                    theme_text_color: "Custom"
                    md_bg_color:(217/255,217/255,217/255,100)
                    size_hint_y: None
                    pos_hint: {"center_x": 2.5, "center_y": .5}
            
            AnchorLayout:
                anchor_x:'center'
                anchor_y:'center'
                size_hint_y: 1.9 
                size_hint_x: 1.
                MDRectangleFlatButton:
                    id: valider
                    text:'    Valider    '
                    text_color: "black"
                    theme_text_color: "Custom"
                    md_bg_color:(87/255,84/255,212/255,100)
                    pos_hint: {"center_x": .5, "center_y": .5}
                    on_release:app.data()



        BoxLayout:
            orientation:'horizontal'
            

'''

class ecran(MDScreen,MDBoxLayout):
    def __init__(self, **kwargs):
        super(ecran,self).__init__( **kwargs)
        

        

class inscription(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(KV)
        fonction=['Maire','Sécretaire principale','Sécretaire']
        menu_items = [
            {
                "text": f"{i}",
                "viewclass": "OneLineListItem",
                "on_release": lambda x=f"{i}": self.menu_callback(x),
            } for i in fonction
        ]
        self.menu = MDDropdownMenu(
            caller=self.screen.ids.fonction,
            items=menu_items,
            width_mult=4,
        )
    def data(self):
        print(self.screen.ids.nom.text)
        print(self.screen.ids.prenom.text)
        print(self.screen.ids.telephone.text)
        print(self.screen.ids.fonction.text)
        print(self.screen.ids.pseudo.text)
        print(self.screen.ids.mdp.text)
        print(self.screen.ids.confirmation.text)

    def menu_callback(self, text_item):
        self.screen.ids.fonction.text=text_item
        print(text_item)
    

    def build(self):
        
        return self.screen
        #return ecran()

inscription().run()