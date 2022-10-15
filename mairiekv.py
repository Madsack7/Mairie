KV = '''
<DrawerClickableItem@MDNavigationDrawerItem>
    focus_color: "white"
    text_color: "black"
    icon_color: "#4a4939"
    ripple_color: "#c5bdd2"
    selected_color: "#4a4939"


<DrawerLabelItem@MDNavigationDrawerItem>
    text_color: "#4a4939"
    icon_color: "#4a4939"
    focus_behavior: False
    selected_color: "#4a4939"
    _no_ripple_effect: True

<ContentNavigationDrawer>
    MDNavigationDrawerMenu:
        MDNavigationDrawerHeader:
            title: "Menu"
            title_color: "white"
            #text: "Header text"
            font_name:'font\AkayaKanadaka-Regular.ttf'
            spacing: "4dp"
            padding: "12dp", 0, 0, "30dp"

        #MDNavigationDrawerLabel:
            #text: "Mail"

        DrawerClickableItem:
            #icon: "gmail"
            #right_text: "+99"
            text: "Accueil"
            text_color: "black"
            on_press:
                root.nav_drawer.set_state("close")
                root.screen_manager.current = "acceuil_maire"
            
        DrawerClickableItem:
            #icon: "send"
            text: "Acte de Naissance"
            text_color: "black"
            on_press:
                root.nav_drawer.set_state("close")
                root.screen_manager.current = "actenaissance_maire"
        
        DrawerClickableItem:
            #icon: "send"
            text: "Acte de Mariage"
            text_color: "black"
            on_press:
                root.nav_drawer.set_state("close")
                root.screen_manager.current = "actemariage_maire"
        
        DrawerClickableItem:
            #icon: "send"
            text: "Acte de Décès"
            text_color: "black"
            on_press:
                root.nav_drawer.set_state("close")
                root.screen_manager.current = "actedeces_maire"

        DrawerClickableItem:
            #icon: "send"
            text: "Bancs"
            text_color: "black"
            on_press:
                root.nav_drawer.set_state("close")
                root.screen_manager.current = "bancs_maire"

        DrawerClickableItem:
            #icon: "send"
            text: "Documents"
            text_color: "black"
            on_press:
                root.nav_drawer.set_state("close")
                root.screen_manager.current = "documents_maire"

        DrawerClickableItem:
            #icon: "gmail"
            #right_text: "+99"
            text: "Employés"
            text_color: "black"
            on_press:
                root.nav_drawer.set_state("close")
                root.screen_manager.current = "employés_maire"
            
        DrawerClickableItem:
            #icon: "send"
            text: "Projets"
            text_color: "black"
            on_press:
                root.nav_drawer.set_state("close")
                root.screen_manager.current = "projets_maire"

        DrawerClickableItem:
            #icon: "send"
            text: "Rendez-vous"
            text_color: "black"
            on_press:
                root.nav_drawer.set_state("close")
                root.screen_manager.current = "rdv_maire"
                
        DrawerClickableItem:
            #icon: "send"
            text: "Personne"
            text_color: "black"
            on_press:
                root.nav_drawer.set_state("close")
                root.screen_manager.current = "personnes_maire"

        DrawerClickableItem:
            #icon: "send"
            text: "Comptabilité"
            text_color: "black"
            on_press:
                root.nav_drawer.set_state("close")
                root.screen_manager.current = "comptabilité_maire"
            
            

        MDNavigationDrawerDivider:

        MDNavigationDrawerLabel:
            text: "Labels"
            

        DrawerLabelItem:
            icon: "information-outline"
            text: "Label"

        DrawerLabelItem:
            icon: "information-outline"
            text: "Label"

    MDList:

        OneLineListItem:
            text: "Deconnectez-vous"
            item_color:'red'
            on_press:
                root.nav_drawer.set_state("close")
                app.decon()



<MagicButton@MagicBehavior+MDRectangleFlatButton>
MDScreen:
    name:'mairie'
    #Le screnmanager qui controle la page de connexion et d'inscription
    ScreenManager:
        id:manager1

        #LE SCREEN DE CONNEXION COMMENCE ICI
        MDScreen:
            name:'connexion'

            RelativeLayout:
                canvas:
                    Color:
                        rgba:(87/255,84/255,212/255,100)
                    Rectangle:
                        pos: (0,0)
                        size: self.size
                    Color:
                        rgba:(255/255,255/255,212/255,100)
                    Rectangle:
                        pos: (0,20)
                        size: 1280, 700
                    Color:
                        rgba:(217/255,217/255,217/255,100)
                    RoundedRectangle:
                        pos: (600,70)
                        size:600,600
            MDLabel:
                text:"S'identifier"
                pos:(810,200)
                theme_text_color:"Custom"
                text_color:(87/255,84/255,212/255,100)
                font_style:'H2'
                font_name:'font\AkayaKanadaka-Regular.ttf'
                bold: True


                BoxLayout:
                    pos:(650,150)
                    orientation:'vertical'
                    size: 300,400
                    BoxLayout:
                        orientation:'horizontal'
                        size_hint_y: 2
                        height: self.minimum_height
                        AnchorLayout:
                            anchor_x:'left'
                            anchor_y:'center'
                            size_hint_y: 1 
                            MDLabel:
                                text:"Pseudo"
                                halign:'left'
                                theme_text_color:"Custom"
                                text_color:(0/255,0/255,0/255,100)
                                font_style:'H5'
                                font_name:'font\AkayaKanadaka-Regular.ttf'
                                bold: True
                        AnchorLayout:
                            anchor_x:'left'
                            anchor_y:'center'
                            size_hint_y: 1 
                            MDTextField:
                                id:pseudocon
                                padding_bottom:10
                                hint_text: "Nom d'utilisateur"
                                icon_left: "account-circle"
                                mode: "round"
                                size_hint_x: 2

                            
                    BoxLayout:
                        orientation:'horizontal'
                        size_hint_y: 2
                        height: self.minimum_height
                        
                        AnchorLayout:
                            anchor_x:'left'
                            anchor_y:'center'
                            size_hint_y: 1.9    
                            MDLabel:
                                text:"Mot de passe"
                                theme_text_color:"Custom"
                                text_color:(0/255,0/255,0/255,100)
                                font_style:'H5'
                                font_name:'font\AkayaKanadaka-Regular.ttf'
                                bold: True
                        AnchorLayout:
                            anchor_x:'left'
                            anchor_y:'center'
                            size_hint_y: 1.9
                            size_hint_x:1
                        

                            MDTextField:
                                id: mdpcon
                                width: "300dp"
                                hint_text: "Mot de passe"
                                mode: "round"
                                password: True
                                icon_left: "key-variant"
                                size_hint_x: None
                                size_hint_y: None
                                pos_hint: {"center_x": .5, "center_y": .5}
                                
                            
                MDIconButton:
                    icon: "eye-off"
                    pos_hint: {"center_x": 2.5,"center_y": .5}
                    pos:1060,320
                    theme_text_color: "Hint"
                    on_release:
                        self.icon = "eye" if self.icon == "eye-off" else "eye-off"
                        mdpcon.password = False if mdpcon.password is True else True
                
                
                MDRectangleFlatButton:
                    pos:(880,250)
                    text: "Se connecter"
                    theme_text_color: "Custom"
                    text_color: "black"
                    line_color: "black"
                    font_name:'font\AkayaKanadaka-Regular.ttf'
                    md_bg_color:(87/255,84/255,212/255,100)
                    on_release:
                        manager1.current='maire'
                        app.show_data()

                MDLabel:
                    text:"Vous n'avez pas de compte ?"
                    theme_text_color:"Secondary"
                    width: "250dp"
                    text_color:(0/255,0/255,0/255,100)
                    font_name:'font\AkayaKanadaka-Regular.ttf'
                    pos:(760,100)

                MDTextButton:
                    text: "Cliquez ici"
                    font_name:'font\AkayaKanadaka-Regular.ttf'
                    theme_text_color: "Custom"
                    custom_color:(131/255,24/255,24/255,100)
                    pos:(980,140)
                    on_press:manager1.current='inscription'
                    bold: True
        #LA FIN DU SCREEN DE CONNEXION

        #LE SCREEN D'INSCRIPTION COMMENCE ICI
        MDScreen:
            name:'inscription'
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
                    font_name:'font\AkayaKanadaka-Regular.ttf'
                    bold: True
                    

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
                            font_name:'font\AkayaKanadaka-Regular.ttf'
                        

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
                            font_name:'font\AkayaKanadaka-Regular.ttf'

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
                            font_name:'font\AkayaKanadaka-Regular.ttf'
                        

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
                            font_name:'font\AkayaKanadaka-Regular.ttf'
                        

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
                            font_name:'font\AkayaKanadaka-Regular.ttf'
                        

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
                            font_name:'font\AkayaKanadaka-Regular.ttf'
                        

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
                            font_name:'font\AkayaKanadaka-Regular.ttf'
                        

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
                            on_press:manager1.current='connexion'
                    
                    AnchorLayout:
                        anchor_x:'center'
                        anchor_y:'center'
                        size_hint_y: 1.9 
                        size_hint_x: 1.
                        MagicButton:
                            id: valider
                            text: "    Valider    "
                            text_color: "black"
                            on_release: self.grow(),app.data()
                            md_bg_color:(87/255,84/255,212/255,100)
                            pos_hint: {"center_x": .5, "center_y": .5}
                    



                BoxLayout:
                    orientation:'horizontal'

        #LA FIN DU SCREEN DE D'INSCRIPTION

        #LE SCREEN MAIRE COMMENCE ICI
        MDScreen:
            name:'maire'
            BoxLayout:
                orientation:'vertical'
                
                BoxLayout:
                    orientation:'horizontal'
                    size_hint_y: 0.5
                    height: self.minimum_height
                    canvas:
                        Color:
                            rgba:(87/255,84/255,212/255,100)
                        Rectangle:
                            pos: self.pos
                            size: self.size

                    MDIconButton:
                        icon: "menu"
                        pos_hint: {"center_x": .0,"center_y": .5}
                        halign:'left'
                        size_hint_x: 0.5
                        size_hint_y: 0
                        theme_text_color: "Custom"
                        text_color:'white'
                        on_release:nav_drawer.set_state("open")

                    MDLabel:
                        id:titre
                        text:"BIENVENUE SUR LA PAGE DU MAIRE"
                        size_hint_x: 2
                        halign:'center'
                        pos_hint: {"center": 1}
                        theme_text_color:"Custom"
                        text_color:'white'
                        font_style:'H3'
                        font_name:'font\AkayaKanadaka-Regular.ttf'
                        bold: True
                            
                
                BoxLayout:
                    orientation:'horizontal'
                    size_hint_y: 5
                    height: self.minimum_height
                                

            MDNavigationLayout:

                MDScreenManager:
                    id: screen_manager
                    #SCREEN ACCEUIL
                    MDScreen:
                        name: "acceuil_maire"
                        RelativeLayout:
                            MDCard:
                                pos:15,550
                                size_hint: .45, .2
                                focus_behavior: True
                                md_bg_color: "darkgrey"
                                unfocus_color: "darkgrey"
                                focus_color: "grey"
                                elevation: 6
                                MDLabel:
                                    text: "bancs"
                                    halign: "center"
                                    text_color:"white"
                            MDCard:
                                pos:15,300
                                size_hint: .45, .2
                                focus_behavior: True
                                md_bg_color: "darkgrey"
                                unfocus_color: "darkgrey"
                                focus_color: "grey"
                                elevation: 6
                                MDLabel:
                                    text: "bancs"
                                    halign: "center"
                                    text_color:"white"
                            MDCard:
                                pos:685,550
                                size_hint: .45, .2
                                focus_behavior: True
                                md_bg_color: "darkgrey"
                                unfocus_color: "darkgrey"
                                focus_color: "grey"
                                elevation: 6
                                MDLabel:
                                    text: "actes"
                                    halign: "center"
                                    text_color:"white"
                            MDCard:
                                pos:685,300
                                size_hint: .45, .2
                                focus_behavior: True
                                md_bg_color: "darkgrey"
                                unfocus_color: "darkgrey"
                                focus_color: "grey"
                                elevation: 6
                                MDLabel:
                                    text: "bancs"
                                    halign: "center"
                                    text_color:"white"
                            MDCard:
                                pos:15,50
                                size_hint: .45, .2
                                focus_behavior: True
                                md_bg_color: "darkgrey"
                                unfocus_color: "darkgrey"
                                focus_color: "grey"
                                elevation: 6
                                MDLabel:
                                    text: "actes"
                                    halign: "center"
                                    text_color:"white"
                            MDCard:
                                pos:685,50
                                size_hint: .45, .2
                                focus_behavior: True
                                md_bg_color: "darkgrey"
                                unfocus_color: "darkgrey"
                                focus_color: "grey"
                                elevation: 6
                                MDLabel:
                                    text: "bancs"
                                    halign: "center"
                                    text_color:"white"

                    #SCREEN ACTE DE NAISSANCE
                    MDScreen:
                        name: "actenaissance_maire"

                        MDCard:
                            pos:10,400
                            size_hint: .98, .3
                            focus_behavior: True
                            md_bg_color: "darkgrey"
                            unfocus_color: "darkgrey"
                            focus_color: "grey"
                            elevation: 6
                            BoxLayout:
                                orientation:'horizontal'
                            
                                MDDropDownItem:
                                    id: fonction
                                    size_hint_x: 1.
                                    pos_hint: {'center_x': .5, 'center_y': .5}
                                    text: 'Sélectionnez'
                                    on_release:  app.menu.open()'
                                

                                MDTextField:
                                    id: telephone
                                    width: "100dp"
                                    mode: "round"
                                    size_hint_x: 1.5
                                    md_bg_color:(217/255,217/255,217/255,100)
                                    size_hint_y: None
                                    pos_hint: {"center_x": 0, "center_y": .5}

                    #SCREEN ACTE DE MARIAGE
                    MDScreen:
                        name: "actemariage_maire"

                        MDLabel:
                            text: "MARIAGE"
                            halign: "center"

                    #SCREEN ACTE DE DECES
                    MDScreen:
                        name: "actedeces_maire"

                        MDLabel:
                            text: "DECES"
                            halign: "center"

                    #SCREEN DE BANCS
                    MDScreen:
                        name: "bancs_maire"
                        
                    #SCREEN DE DOCUMENTS
                    MDScreen:
                        name: "documents_maire"

                        MDLabel:
                            text: "documents"
                            halign: "center"
                    
                    #SCREEN DE EMPLOYES
                    MDScreen:
                        name: "employés_maire"

                        MDLabel:
                            text: "employés"
                            halign: "center"

                    #SCREEN DE PROJETS
                    MDScreen:
                        name: "projets_maire"

                        MDLabel:
                            text: "projets"
                            halign: "center"

                    #SCREEN DE RDV
                    MDScreen:
                        name: "rdv_maire"

                        MDLabel:
                            text: "rdv"
                            halign: "center"

                    #SCREEN DE PERSONNES
                    MDScreen:
                        name: "personnes_maire"

                        MDLabel:
                            text: "personnes"
                            halign: "center"
                    
                    #SCREEN DE COMPTABILITE
                    MDScreen:
                        name: "comptabilité_maire"

                        MDLabel:
                            text: "comptabilité"
                            halign: "center"
            

                MDNavigationDrawer:
                    id: nav_drawer
                    radius: (0, 16, 16, 0)
                    md_bg_color:(87/255,84/255,212/255,100)
                    ContentNavigationDrawer:
                        orientation:'vertical'
                        screen_manager: screen_manager
                        nav_drawer: nav_drawer
        #LA FIN DU SCREEN MAIRE

    #LA FIN DU SCREENMANAGER manager1                   
'''