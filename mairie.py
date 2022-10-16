
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.properties import ListProperty, ObjectProperty , StringProperty
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivy.core.window import Window,Config
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.menu import MDDropdownMenu
from kivy.metrics import dp
from mairiekv import KV
Window.font_name='font\AkayaKanadaka-Regular.ttk'
Window.fullscreen='auto'


class ClickableTextFieldRound(MDRelativeLayout):
 
        
    text = StringProperty()
    hint_text = StringProperty()
    # Here specify the required parameters for MDTextFieldRound:
    # [...]
class ContentNavigationDrawerSP(MDBoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()

class ContentNavigationDrawerMaire(MDBoxLayout):
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

        # Les Tableaux
        # Maire     
       def create_datatable_acteNais_Maire(self):
           self.data_tablenaiss=MDDataTable(
               size_hint=(0.01,0.5),
               use_pagination=True,
               check=True,column_data=[
                   ("Num",dp(30),lambda *args:print("Numéro de l'acte")),
                   ("Nom",dp(30)),
                   ("Prénom",dp(30)),
                   ("Date_Naissance",dp(30)),
                   ("Lieu_Naissance",dp(30)),
                   ("Sexe",dp(30)),
                   ("Prénom_Père",dp(30)),
                   ("Profession",dp(30)),
                   ("Domicile",dp(30)),
                   ("Nom_Mère",dp(30)),
                   ("Prénom_Mère",dp(30)),
                   ("Profession",dp(30)),
                   ("Domicile",dp(30)),
                   ("Officier",dp(30)),
                   ("Date",dp(30)),
               ],
               background_color_header="grey",
               row_data=[]
            )
           self.screen.ids['boxtablenaissance'].add_widget(self.data_tablenaiss)

       def create_datatable_acteMari_Maire(self):
           self.data_tablemari=MDDataTable(
               size_hint=(0.01,0.5),
               use_pagination=True,
               check=True,column_data=[
                   ("Num",dp(30),lambda *args:print("Numéro de l'acte")),
                   ("Date_Mariage",dp(30)),
                   ("Nom_marié",dp(30)),
                   ("Prénom_marié",dp(30)),
                   ("Date_Naissance",dp(30)),
                   ("Lieu_Naissance",dp(30)),
                   ("Profession",dp(30)),
                   ("Domicile",dp(30)),
                   ("Parent",dp(40)),
                   ("Nom_mariée",dp(30)),
                   ("Prénom_mariée",dp(30)),
                   ("Date_Naissance",dp(30)),
                   ("Lieu_Naissance",dp(30)),
                   ("Profession",dp(30)),
                   ("Domicile",dp(30)),
                   ("Parent",dp(40)),
                   ("regime_matrimoniale",dp(40)),
                   ("option_matrimoniale",dp(40)),
                   ("Bancs",dp(40)),
               ],
               background_color_header="grey",
               row_data=[]
            )
           self.screen.ids['boxtablemariage'].add_widget(self.data_tablemari)

       def create_datatable_acteDeces_Maire(self):
           self.data_tabledeces=MDDataTable(
               size_hint=(0.01,0.5),
               use_pagination=True,
               check=True,column_data=[
                   ("Num",dp(40),lambda *args:print("Numéro de l'acte")),
                   ("Nom",dp(40)),
                   ("Prénom",dp(40)),
                   ("Date_décès",dp(40)),
                   ("Cause_décès",dp(40)),
                   ("Officier",dp(40)),
                   ("Date",dp(40)),
               ],
               background_color_header="grey",
               row_data=[]
            )
           self.screen.ids['boxtabledeces'].add_widget(self.data_tabledeces)

       def create_datatable_bancs_Maire(self):
           self.data_tablebancs=MDDataTable(
               size_hint=(0.01,0.5),
               use_pagination=True,
               check=True,column_data=[
                   ("identifiant",dp(40),lambda *args:print("Numéro de l'acte")),
                   ("Nom_marié",dp(40)),
                   ("Prénom_marié",dp(40)),
                   ("Nom_mariée",dp(40)),
                   ("Prénom_mariée",dp(40)),
                   ("Date_declaration",dp(40)),
                   ("Date_mariage",dp(40)),
                   ("Téléphone",dp(40)),
               ],
               background_color_header="grey",
               row_data=[]
            )
           self.screen.ids['boxtablebancs'].add_widget(self.data_tablebancs)

       def create_datatable_doc_Maire(self):
           self.data_tabledoc=MDDataTable(
               size_hint=(0.01,0.5),
               use_pagination=True,
               check=True,column_data=[
                   ("Num",dp(50),lambda *args:print("Numéro de l'acte")),
                   ("Type_document",dp(50)),
                   ("Prénom",dp(50)),
                   ("Nom",dp(50)),
                   ("Téléphone",dp(50)),
                   ("Date",dp(50)),
                   
               ],
               background_color_header="grey",
               row_data=[]
            )
           self.screen.ids['boxtabledocument'].add_widget(self.data_tabledoc)

       def create_datatable_emp_Maire(self):
           self.data_tableemp=MDDataTable(
               size_hint=(0.01,0.5),
               use_pagination=True,
               check=True,column_data=[
                   ("Nom",dp(60),lambda *args:print("Numéro de l'acte")),
                   ("Prénom",dp(60)),
                   ("Téléphone",dp(60)),
                   ("Salaire",dp(60)),
                   ("Date_embauche",dp(60)),
                   
                   
               ],
               background_color_header="grey",
               row_data=[]
            )
           self.screen.ids['boxtableemploye'].add_widget(self.data_tableemp)

       def create_datatable_projet_Maire(self):
           self.data_tableprojet=MDDataTable(
               size_hint=(0.01,0.5),
               use_pagination=True,
               check=True,column_data=[
                   ("Num",dp(50),lambda *args:print("Numéro de l'acte")),
                   ("Description",dp(50)),
                   ("Etat",dp(50)),
                   ("Nom",dp(50)),
                   ("Prénom",dp(50)),
                   ("Téléphone",dp(50)),
                   
                   
               ],
               background_color_header="grey",
               row_data=[]
            )
           self.screen.ids['boxtableprojet'].add_widget(self.data_tableprojet)

       def create_datatable_rdv_Maire(self):
           self.data_tablerdv=MDDataTable(
               size_hint=(0.01,0.5),
               use_pagination=True,
               check=True,column_data=[
                   ("Num",dp(40),lambda *args:print("Numéro de l'acte")),
                   ("Date",dp(40)),
                   ("Heure",dp(40)),
                   ("Motif",dp(40)),
                   ("Nom",dp(40)),
                   ("Prénom",dp(40)),
                   ("Téléphone",dp(40)),
                   
                   
               ],
               background_color_header="grey",
               row_data=[]
            )
           self.screen.ids['boxtablerdv'].add_widget(self.data_tablerdv)

       def create_datatable_personne_Maire(self):
           self.data_tablepersonne=MDDataTable(
               size_hint=(0.01,0.5),
               use_pagination=True,
               check=True,column_data=[
                   ("Nom",dp(70)),
                   ("Prénom",dp(70)),
                   ("Téléphone",dp(70)),
                     
               ],
               background_color_header="grey",
               row_data=[]
            )
           self.screen.ids['boxtabledpersonne'].add_widget(self.data_tablepersonne)


        #SECRETAIRE PRINCIPAL
       def create_datatable_acteNais_SP(self):
           self.data_tablenaissSP=MDDataTable(
               size_hint=(0.01,0.5),
               use_pagination=True,
               check=True,column_data=[
                   ("Num",dp(30),lambda *args:print("Numéro de l'acte")),
                   ("Nom",dp(30)),
                   ("Prénom",dp(30)),
                   ("Date_Naissance",dp(30)),
                   ("Lieu_Naissance",dp(30)),
                   ("Sexe",dp(30)),
                   ("Prénom_Père",dp(30)),
                   ("Profession",dp(30)),
                   ("Domicile",dp(30)),
                   ("Nom_Mère",dp(30)),
                   ("Prénom_Mère",dp(30)),
                   ("Profession",dp(30)),
                   ("Domicile",dp(30)),
                   ("Officier",dp(30)),
                   ("Date",dp(30)),
               ],
               background_color_header="grey",
               row_data=[]
            )
           self.screen.ids['boxtablenaissancesp'].add_widget(self.data_tablenaissSP)

       def create_datatable_acteMari_SP(self):
           self.data_tablemariSP=MDDataTable(
               size_hint=(0.01,0.5),
               use_pagination=True,
               check=True,column_data=[
                   ("Num",dp(30),lambda *args:print("Numéro de l'acte")),
                   ("Date_Mariage",dp(30)),
                   ("Nom_marié",dp(30)),
                   ("Prénom_marié",dp(30)),
                   ("Date_Naissance",dp(30)),
                   ("Lieu_Naissance",dp(30)),
                   ("Profession",dp(30)),
                   ("Domicile",dp(30)),
                   ("Parent",dp(40)),
                   ("Nom_mariée",dp(30)),
                   ("Prénom_mariée",dp(30)),
                   ("Date_Naissance",dp(30)),
                   ("Lieu_Naissance",dp(30)),
                   ("Profession",dp(30)),
                   ("Domicile",dp(30)),
                   ("Parent",dp(40)),
                   ("regime_matrimoniale",dp(40)),
                   ("option_matrimoniale",dp(40)),
                   ("Bancs",dp(40)),
               ],
               background_color_header="grey",
               row_data=[]
            )
           self.screen.ids['boxtablemariagesp'].add_widget(self.data_tablemariSP)

       def create_datatable_acteDeces_SP(self):
           self.data_tabledecesSP=MDDataTable(
               size_hint=(0.01,0.5),
               use_pagination=True,
               check=True,column_data=[
                   ("Num",dp(40),lambda *args:print("Numéro de l'acte")),
                   ("Nom",dp(40)),
                   ("Prénom",dp(40)),
                   ("Date_décès",dp(40)),
                   ("Cause_décès",dp(40)),
                   ("Officier",dp(40)),
                   ("Date",dp(40)),
               ],
               background_color_header="grey",
               row_data=[]
            )
           self.screen.ids['boxtabledecessp'].add_widget(self.data_tabledecesSP)

       def create_datatable_bancs_SP(self):
           self.data_tablebancsSP=MDDataTable(
               size_hint=(0.01,0.5),
               use_pagination=True,
               check=True,column_data=[
                   ("identifiant",dp(40),lambda *args:print("Numéro de l'acte")),
                   ("Nom_marié",dp(40)),
                   ("Prénom_marié",dp(40)),
                   ("Nom_mariée",dp(40)),
                   ("Prénom_mariée",dp(40)),
                   ("Date_declaration",dp(40)),
                   ("Date_mariage",dp(40)),
                   ("Téléphone",dp(40)),
               ],
               background_color_header="grey",
               row_data=[]
            )
           self.screen.ids['boxtablebancssp'].add_widget(self.data_tablebancsSP)

       def create_datatable_doc_SP(self):
           self.data_tabledocSP=MDDataTable(
               size_hint=(0.01,0.5),
               use_pagination=True,
               check=True,column_data=[
                   ("Num",dp(50),lambda *args:print("Numéro de l'acte")),
                   ("Type_document",dp(50)),
                   ("Prénom",dp(50)),
                   ("Nom",dp(50)),
                   ("Téléphone",dp(50)),
                   ("Date",dp(50)),
                   
               ],
               background_color_header="grey",
               row_data=[]
            )
           self.screen.ids['boxtabledocumentsp'].add_widget(self.data_tabledocSP)

       def create_datatable_emp_SP(self):
           self.data_tableempSP=MDDataTable(
               size_hint=(0.01,0.5),
               use_pagination=True,
               check=True,column_data=[
                   ("Nom",dp(60),lambda *args:print("Numéro de l'acte")),
                   ("Prénom",dp(60)),
                   ("Téléphone",dp(60)),
                   ("Salaire",dp(60)),
                   ("Date_embauche",dp(60)),
                   
                   
               ],
               background_color_header="grey",
               row_data=[]
            )
           self.screen.ids['boxtableemployesp'].add_widget(self.data_tableempSP)

       def create_datatable_projet_SP(self):
           self.data_tableprojetSP=MDDataTable(
               size_hint=(0.01,0.5),
               use_pagination=True,
               check=True,column_data=[
                   ("Num",dp(50),lambda *args:print("Numéro de l'acte")),
                   ("Description",dp(50)),
                   ("Etat",dp(50)),
                   ("Nom",dp(50)),
                   ("Prénom",dp(50)),
                   ("Téléphone",dp(50)),
                   
                   
               ],
               background_color_header="grey",
               row_data=[]
            )
           self.screen.ids['boxtableprojetsp'].add_widget(self.data_tableprojetSP)

       def create_datatable_rdv_SP(self):
           self.data_tablerdvSP=MDDataTable(
               size_hint=(0.01,0.5),
               use_pagination=True,
               check=True,column_data=[
                   ("Num",dp(40),lambda *args:print("Numéro de l'acte")),
                   ("Date",dp(40)),
                   ("Heure",dp(40)),
                   ("Motif",dp(40)),
                   ("Nom",dp(40)),
                   ("Prénom",dp(40)),
                   ("Téléphone",dp(40)),
                   
                   
               ],
               background_color_header="grey",
               row_data=[]
            )
           self.screen.ids['boxtablerdvsp'].add_widget(self.data_tablerdvSP)

       def create_datatable_personne_SP(self):
           self.data_tablepersonneSP=MDDataTable(
               size_hint=(0.01,0.5),
               use_pagination=True,
               check=True,column_data=[
                   ("Nom",dp(70)),
                   ("Prénom",dp(70)),
                   ("Téléphone",dp(70)),
                     
               ],
               background_color_header="grey",
               row_data=[]
            )
           self.screen.ids['boxtabledpersonnesp'].add_widget(self.data_tablepersonneSP)

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
            self.create_datatable_acteNais_Maire()
            self.create_datatable_acteMari_Maire()
            self.create_datatable_acteDeces_Maire()
            self.create_datatable_bancs_Maire()
            self.create_datatable_doc_Maire()
            self.create_datatable_emp_Maire()
            self.create_datatable_projet_Maire()
            self.create_datatable_rdv_Maire()
            self.create_datatable_personne_Maire()
            self.create_datatable_acteNais_SP()
            self.create_datatable_acteMari_SP()
            self.create_datatable_acteDeces_SP()
            self.create_datatable_bancs_SP()
            self.create_datatable_doc_SP()
            self.create_datatable_emp_SP()
            self.create_datatable_projet_SP()
            self.create_datatable_rdv_SP()
            self.create_datatable_personne_SP()
            return self.screen



       
'''Config.set('graphics','fullscreen','auto')
Config.set('graphics','window_state','maximized')
Config.write()'''            


Test().run()