
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.properties import ListProperty, ObjectProperty , StringProperty
from kivy.uix.screenmanager import Screen
from kivymd.uix import MDAdaptiveWidget
from kivymd.uix.behaviors import DeclarativeBehavior
from kivymd.uix.hero import MDHeroTo
from kivymd.uix.screen import MDScreen
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivy.core.window import Window,Config
from kivymd.uix.button import MDFlatButton
from kivymd.uix.menu import MDDropdownMenu
from mairiekv import KV
Window.font_name='font\AkayaKanadaka-Regular.ttk'
Window.fullscreen='auto'


class ClickableTextFieldRound(MDRelativeLayout):
 
        
    text = StringProperty()
    hint_text = StringProperty()
    # Here specify the required parameters for MDTextFieldRound:
    # [...]

class ContentNavigationDrawer(MDBoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()
    pass

class Test(MDApp):
       def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.screen=Builder.load_string(KV)

            #Connexion et inscription
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

            

       #Connexion et inscription fonction debut
       def decon(self):
           print(self.screen.ids.manager1)
           self.screen.ids.manager1.current='connexion'

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

       def show_data(self):
           print(self.screen.ids.pseudocon.text)
           print(self.screen.ids.mdpcon.text)
       #Connexion et inscription fin

       def build(self):
            return self.screen



       
'''Config.set('graphics','fullscreen','auto')
Config.set('graphics','window_state','maximized')
Config.write()'''            


Test().run()