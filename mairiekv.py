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

#Maire
<ContentNavigationDrawerMaire>
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

    MDList:

        OneLineListItem:
            text: "Deconnectez-vous"
            item_color:'red'
            on_press:
                root.nav_drawer.set_state("close")
                app.decon()

#Sécretaire PRINCIPAL
<ContentNavigationDrawerSP>
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
                root.nav_drawersp.set_state("close")
                root.screen_managersp.current = "acceuil_sp"
            
        DrawerClickableItem:
            #icon: "send"
            text: "Acte de Naissance"
            text_color: "black"
            on_press:
                root.nav_drawersp.set_state("close")
                root.screen_managersp.current = "actenaissance_sp"
        
        DrawerClickableItem:
            #icon: "send"
            text: "Acte de Mariage"
            text_color: "black"
            on_press:
                root.nav_drawersp.set_state("close")
                root.screen_managersp.current = "actemariage_sp"
        
        DrawerClickableItem:
            #icon: "send"
            text: "Acte de Décès"
            text_color: "black"
            on_press:
                root.nav_drawersp.set_state("close")
                root.screen_managersp.current = "actedeces_sp"

        DrawerClickableItem:
            #icon: "send"
            text: "Bancs"
            text_color: "black"
            on_press:
                root.nav_drawersp.set_state("close")
                root.screen_managersp.current = "bancs_sp"

        DrawerClickableItem:
            #icon: "send"
            text: "Documents"
            text_color: "black"
            on_press:
                root.nav_drawersp.set_state("close")
                root.screen_managersp.current = "documents_sp"

        DrawerClickableItem:
            #icon: "gmail"
            #right_text: "+99"
            text: "Employés"
            text_color: "black"
            on_press:
                root.nav_drawersp.set_state("close")
                root.screen_managersp.current = "employés_sp"
            
        DrawerClickableItem:
            #icon: "send"
            text: "Projets"
            text_color: "black"
            on_press:
                root.nav_drawersp.set_state("close")
                root.screen_managersp.current = "projets_sp"

        DrawerClickableItem:
            #icon: "send"
            text: "Rendez-vous"
            text_color: "black"
            on_press:
                root.nav_drawersp.set_state("close")
                root.screen_managersp.current = "rdv_sp"
                
        DrawerClickableItem:
            #icon: "send"
            text: "Personne"
            text_color: "black"
            on_press:
                root.nav_drawersp.set_state("close")
                root.screen_managersp.current = "personnes_sp"

        DrawerClickableItem:
            #icon: "send"
            text: "Comptabilité"
            text_color: "black"
            on_press:
                root.nav_drawersp.set_state("close")
                root.screen_managersp.current = "comptabilité_sp"
            
            

        MDNavigationDrawerDivider:

    MDList:

        OneLineListItem:
            text: "Deconnectez-vous"
            item_color:'red'
            on_press:
                root.nav_drawersp.set_state("close")
                app.decon()



<MagicButton@MagicBehavior+MDRectangleFlatButton>
MDScreen:
    name:'mairie'
    #Le screnmanager qui controle Tout
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
                        manager1.current='sp'
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
                        size_hint_x: 0.3
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
                                focus_behavior: False
                                md_bg_color: "#FF6347"
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
                                focus_behavior: False
                                md_bg_color: "#1C89B8"
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
                                focus_behavior: False
                                md_bg_color: "#502E5C"
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
                                focus_behavior: False
                                md_bg_color: "#51C055"
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
                                focus_behavior: False
                                md_bg_color: "#FF5F04"
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
                                focus_behavior: False
                                md_bg_color: "#D13434"
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
                            pos:10,550
                            size_hint: .98, .15
                            focus_behavior: False
                            md_bg_color: "darkgrey"
                            unfocus_color: "darkgrey"
                            focus_color: "grey"
                            elevation: 6
                            MDLabel:
                                text: "Liste des actes de naissance"
                                halign: "center"
                                theme_text_color:"Custom"
                                text_color:'white'
                                font_style:'H3'
                                font_name:'font\AkayaKanadaka-Regular.ttf'
                                bold: True
                                

                        MDCard:
                            pos:10,450
                            size_hint: .98, .15
                            focus_behavior: False
                            md_bg_color: "darkgrey"
                            unfocus_color: "darkgrey"
                            focus_color: "grey"
                            elevation: 6
                            BoxLayout:
                                orientation:'horizontal'
                            
                                MDDropDownItem:
                                    id: fonction
                                    size_hint_x: 0.18
                                    pos_hint: {'center_x': .5, 'center_y': .5}
                                    text: 'Sélectionnez'
                                    on_release:  app.menu.open()
                                

                                MDTextField:
                                    id: researchnaissance
                                    width: "100dp"
                                    mode: "round"
                                    size_hint_x: 0.5
                                    md_bg_color:(217/255,217/255,217/255,100)
                                    size_hint_y: None
                                    pos_hint: {"center_x": 0, "center_y": .5}
                                    padding_x:20
                                BoxLayout:
                                    orientation:'horizontal'
                        MDBoxLayout:
                            orientation:'horizontal'
                            id:boxtablenaissance
                            pos:10,30


                    #SCREEN ACTE DE MARIAGE
                    MDScreen:
                        name: "actemariage_maire"

                        MDCard:
                            pos:10,550
                            size_hint: .98, .15
                            focus_behavior: False
                            md_bg_color: "darkgrey"
                            unfocus_color: "darkgrey"
                            focus_color: "grey"
                            elevation: 6
                            MDLabel:
                                text: "Liste des actes de mariage"
                                halign: "center"
                                theme_text_color:"Custom"
                                text_color:'white'
                                font_style:'H3'
                                font_name:'font\AkayaKanadaka-Regular.ttf'
                                bold: True
                                

                        MDCard:
                            pos:10,450
                            size_hint: .98, .15
                            focus_behavior: False
                            md_bg_color: "darkgrey"
                            unfocus_color: "darkgrey"
                            focus_color: "grey"
                            elevation: 6
                            BoxLayout:
                                orientation:'horizontal'
                            
                                MDDropDownItem:
                                    id: fonction
                                    size_hint_x: 0.18
                                    pos_hint: {'center_x': .5, 'center_y': .5}
                                    text: 'Sélectionnez'
                                    on_release:  app.menu.open()
                                

                                MDTextField:
                                    id: researchmariage
                                    width: "100dp"
                                    mode: "round"
                                    size_hint_x: 0.5
                                    md_bg_color:(217/255,217/255,217/255,100)
                                    size_hint_y: None
                                    pos_hint: {"center_x": 0, "center_y": .5}
                                    padding_x:20
                                BoxLayout:
                                    orientation:'horizontal'
                        MDBoxLayout:
                            orientation:'horizontal'
                            id:boxtablemariage
                            pos:10,30

                    #SCREEN ACTE DE DECES
                    MDScreen:
                        name: "actedeces_maire"

                        MDCard:
                            pos:10,550
                            size_hint: .98, .15
                            focus_behavior: False
                            md_bg_color: "darkgrey"
                            unfocus_color: "darkgrey"
                            focus_color: "grey"
                            elevation: 6
                            MDLabel:
                                text: "Liste des actes de décès"
                                halign: "center"
                                theme_text_color:"Custom"
                                text_color:'white'
                                font_style:'H3'
                                font_name:'font\AkayaKanadaka-Regular.ttf'
                                bold: True
                                

                        MDCard:
                            pos:10,450
                            size_hint: .98, .15
                            focus_behavior: False
                            md_bg_color: "darkgrey"
                            unfocus_color: "darkgrey"
                            focus_color: "grey"
                            elevation: 6
                            BoxLayout:
                                orientation:'horizontal'
                            
                                MDDropDownItem:
                                    id: fonction
                                    size_hint_x: 0.18
                                    pos_hint: {'center_x': .5, 'center_y': .5}
                                    text: 'Sélectionnez'
                                    on_release:  app.menu.open()
                                

                                MDTextField:
                                    id: researchdeces
                                    width: "100dp"
                                    mode: "round"
                                    size_hint_x: 0.5
                                    md_bg_color:(217/255,217/255,217/255,100)
                                    size_hint_y: None
                                    pos_hint: {"center_x": 0, "center_y": .5}
                                    padding_x:20
                                BoxLayout:
                                    orientation:'horizontal'
                        MDBoxLayout:
                            orientation:'horizontal'
                            id:boxtabledeces
                            pos:10,30

                    #SCREEN DE BANCS
                    MDScreen:
                        name: "bancs_maire"

                        MDCard:
                            pos:10,550
                            size_hint: .98, .15
                            focus_behavior: False
                            md_bg_color: "darkgrey"
                            unfocus_color: "darkgrey"
                            focus_color: "grey"
                            elevation: 6
                            MDLabel:
                                text: "Liste des bancs"
                                halign: "center"
                                theme_text_color:"Custom"
                                text_color:'white'
                                font_style:'H3'
                                font_name:'font\AkayaKanadaka-Regular.ttf'
                                bold: True
                                

                        MDCard:
                            pos:10,450
                            size_hint: .98, .15
                            focus_behavior: False
                            md_bg_color: "darkgrey"
                            unfocus_color: "darkgrey"
                            focus_color: "grey"
                            elevation: 6
                            BoxLayout:
                                orientation:'horizontal'
                            
                                MDDropDownItem:
                                    id: fonction
                                    size_hint_x: 0.18
                                    pos_hint: {'center_x': .5, 'center_y': .5}
                                    text: 'Sélectionnez'
                                    on_release:  app.menu.open()
                                

                                MDTextField:
                                    id: researchbancs
                                    width: "100dp"
                                    mode: "round"
                                    size_hint_x: 0.5
                                    md_bg_color:(217/255,217/255,217/255,100)
                                    size_hint_y: None
                                    pos_hint: {"center_x": 0, "center_y": .5}
                                    padding_x:20
                                BoxLayout:
                                    orientation:'horizontal'
                        MDBoxLayout:
                            orientation:'horizontal'
                            id:boxtablebancs
                            pos:10,30
                        

                    #SCREEN DE DOCUMENTS
                    MDScreen:
                        name: "documents_maire"

                        MDCard:
                            pos:10,550
                            size_hint: .98, .15
                            focus_behavior: False
                            md_bg_color: "darkgrey"
                            unfocus_color: "darkgrey"
                            focus_color: "grey"
                            elevation: 6
                            MDLabel:
                                text: "Liste des documents"
                                halign: "center"
                                theme_text_color:"Custom"
                                text_color:'white'
                                font_style:'H3'
                                font_name:'font\AkayaKanadaka-Regular.ttf'
                                bold: True
                                

                        MDCard:
                            pos:10,450
                            size_hint: .98, .15
                            focus_behavior: False
                            md_bg_color: "darkgrey"
                            unfocus_color: "darkgrey"
                            focus_color: "grey"
                            elevation: 6
                            BoxLayout:
                                orientation:'horizontal'
                            
                                MDDropDownItem:
                                    id: fonction
                                    size_hint_x: 0.18
                                    pos_hint: {'center_x': .5, 'center_y': .5}
                                    text: 'Sélectionnez'
                                    on_release:  app.menu.open()
                                

                                MDTextField:
                                    id: researchdocument
                                    width: "100dp"
                                    mode: "round"
                                    size_hint_x: 0.5
                                    md_bg_color:(217/255,217/255,217/255,100)
                                    size_hint_y: None
                                    pos_hint: {"center_x": 0, "center_y": .5}
                                    padding_x:20
                                BoxLayout:
                                    orientation:'horizontal'
                        MDBoxLayout:
                            orientation:'horizontal'
                            id:boxtabledocument
                            pos:10,30
                    
                    #SCREEN DE EMPLOYES
                    MDScreen:
                        name: "employés_maire"

                        MDCard:
                            pos:10,550
                            size_hint: .98, .15
                            focus_behavior: False
                            md_bg_color: "darkgrey"
                            unfocus_color: "darkgrey"
                            focus_color: "grey"
                            elevation: 6
                            MDLabel:
                                text: "Liste des employés"
                                halign: "center"
                                theme_text_color:"Custom"
                                text_color:'white'
                                font_style:'H3'
                                font_name:'font\AkayaKanadaka-Regular.ttf'
                                bold: True
                                

                        MDCard:
                            pos:10,450
                            size_hint: .98, .15
                            focus_behavior: False
                            md_bg_color: "darkgrey"
                            unfocus_color: "darkgrey"
                            focus_color: "grey"
                            elevation: 6
                            BoxLayout:
                                orientation:'horizontal'
                            
                                MDDropDownItem:
                                    id: fonction
                                    size_hint_x: 0.18
                                    pos_hint: {'center_x': .5, 'center_y': .5}
                                    text: 'Sélectionnez'
                                    on_release:  app.menu.open()
                                

                                MDTextField:
                                    id: researchemploye
                                    width: "100dp"
                                    mode: "round"
                                    size_hint_x: 0.5
                                    md_bg_color:(217/255,217/255,217/255,100)
                                    size_hint_y: None
                                    pos_hint: {"center_x": 0, "center_y": .5}
                                    padding_x:20
                                BoxLayout:
                                    orientation:'horizontal'
                        MDBoxLayout:
                            orientation:'horizontal'
                            id:boxtableemploye
                            pos:10,30

                    #SCREEN DE PROJETS
                    MDScreen:
                        name: "projets_maire"

                        MDCard:
                            pos:10,550
                            size_hint: .98, .15
                            focus_behavior: False
                            md_bg_color: "darkgrey"
                            unfocus_color: "darkgrey"
                            focus_color: "grey"
                            elevation: 6
                            MDLabel:
                                text: "Liste des projets"
                                halign: "center"
                                theme_text_color:"Custom"
                                text_color:'white'
                                font_style:'H3'
                                font_name:'font\AkayaKanadaka-Regular.ttf'
                                bold: True
                                

                        MDCard:
                            pos:10,450
                            size_hint: .98, .15
                            focus_behavior: False
                            md_bg_color: "darkgrey"
                            unfocus_color: "darkgrey"
                            focus_color: "grey"
                            elevation: 6
                            BoxLayout:
                                orientation:'horizontal'
                            
                                MDDropDownItem:
                                    id: fonction
                                    size_hint_x: 0.18
                                    pos_hint: {'center_x': .5, 'center_y': .5}
                                    text: 'Sélectionnez'
                                    on_release:  app.menu.open()
                                

                                MDTextField:
                                    id: researchprojet
                                    width: "100dp"
                                    mode: "round"
                                    size_hint_x: 0.5
                                    md_bg_color:(217/255,217/255,217/255,100)
                                    size_hint_y: None
                                    pos_hint: {"center_x": 0, "center_y": .5}
                                    padding_x:20
                                BoxLayout:
                                    orientation:'horizontal'
                        MDBoxLayout:
                            orientation:'horizontal'
                            id:boxtableprojet
                            pos:10,30

                    #SCREEN DE RDV
                    MDScreen:
                        name: "rdv_maire"

                        MDCard:
                            pos:10,550
                            size_hint: .98, .15
                            focus_behavior: False
                            md_bg_color: "darkgrey"
                            unfocus_color: "darkgrey"
                            focus_color: "grey"
                            elevation: 6
                            MDLabel:
                                text: "Liste des rendez-vous"
                                halign: "center"
                                theme_text_color:"Custom"
                                text_color:'white'
                                font_style:'H3'
                                font_name:'font\AkayaKanadaka-Regular.ttf'
                                bold: True
                                

                        MDCard:
                            pos:10,450
                            size_hint: .98, .15
                            focus_behavior: False
                            md_bg_color: "darkgrey"
                            unfocus_color: "darkgrey"
                            focus_color: "grey"
                            elevation: 6
                            BoxLayout:
                                orientation:'horizontal'
                            
                                MDDropDownItem:
                                    id: fonction
                                    size_hint_x: 0.18
                                    pos_hint: {'center_x': .5, 'center_y': .5}
                                    text: 'Sélectionnez'
                                    on_release:  app.menu.open()
                                

                                MDTextField:
                                    id: researchrdv
                                    width: "100dp"
                                    mode: "round"
                                    size_hint_x: 0.5
                                    md_bg_color:(217/255,217/255,217/255,100)
                                    size_hint_y: None
                                    pos_hint: {"center_x": 0, "center_y": .5}
                                    padding_x:20
                                BoxLayout:
                                    orientation:'horizontal'
                        MDBoxLayout:
                            orientation:'horizontal'
                            id:boxtablerdv
                            pos:10,30

                    #SCREEN DE PERSONNES
                    MDScreen:
                        name: "personnes_maire"

                        MDCard:
                            pos:10,550
                            size_hint: .98, .15
                            focus_behavior: False
                            md_bg_color: "darkgrey"
                            unfocus_color: "darkgrey"
                            focus_color: "grey"
                            elevation: 6
                            MDLabel:
                                text: "Liste des personnes"
                                halign: "center"
                                theme_text_color:"Custom"
                                text_color:'white'
                                font_style:'H3'
                                font_name:'font\AkayaKanadaka-Regular.ttf'
                                bold: True
                                

                        MDCard:
                            pos:10,450
                            size_hint: .98, .15
                            focus_behavior: False
                            md_bg_color: "darkgrey"
                            unfocus_color: "darkgrey"
                            focus_color: "grey"
                            elevation: 6
                            BoxLayout:
                                orientation:'horizontal'
                            
                                MDDropDownItem:
                                    id: fonction
                                    size_hint_x: 0.18
                                    pos_hint: {'center_x': .5, 'center_y': .5}
                                    text: 'Sélectionnez'
                                    on_release:  app.menu.open()
                                

                                MDTextField:
                                    id: researchpersonne
                                    width: "100dp"
                                    mode: "round"
                                    size_hint_x: 0.5
                                    md_bg_color:(217/255,217/255,217/255,100)
                                    size_hint_y: None
                                    pos_hint: {"center_x": 0, "center_y": .5}
                                    padding_x:20
                                BoxLayout:
                                    orientation:'horizontal'
                        MDBoxLayout:
                            orientation:'horizontal'
                            id:boxtabledpersonne
                            pos:10,30
                    
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
                    ContentNavigationDrawerMaire:
                        orientation:'vertical'
                        screen_manager: screen_manager
                        nav_drawer: nav_drawer
        #LA FIN DU SCREEN MAIRE


        #LE SCREEN SECRETAIRE PRINCIPAL COMMENCE ICI
        MDScreen:
            name:'sp'
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
                        size_hint_x: 0.2
                        size_hint_y: 0
                        theme_text_color: "Custom"
                        text_color:'white'
                        on_release:nav_drawersp.set_state("open")

                    MDLabel:
                        id:titress
                        text:"BIENVENUE SUR LA PAGE DU SECRETAIRE PRINCIPAL  "
                        size_hint_x: 2.2
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
                    id: screen_managersp
                    #SCREEN ACCEUIL
                    MDScreen:
                        name: "acceuil_sp"
                        RelativeLayout:
                            MDCard:
                                pos:15,550
                                size_hint: .45, .2
                                focus_behavior: False
                                md_bg_color: "#FF6347"
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
                                focus_behavior: False
                                md_bg_color: "#1C89B8"
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
                                focus_behavior: False
                                md_bg_color: "#502E5C"
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
                                focus_behavior: False
                                md_bg_color: "#51C055"
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
                                focus_behavior: False
                                md_bg_color: "#FF5F04"
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
                                focus_behavior: False
                                md_bg_color: "#D13434"
                                unfocus_color: "darkgrey"
                                focus_color: "grey"
                                elevation: 6
                                MDLabel:
                                    text: "bancs"
                                    halign: "center"
                                    text_color:"white"

                    #SCREEN ACTE DE NAISSANCE
                    MDScreen:
                        name: "actenaissance_sp"

                        MDCard:
                            pos:10,550
                            size_hint: .98, .15
                            focus_behavior: False
                            md_bg_color: "darkgrey"
                            unfocus_color: "darkgrey"
                            focus_color: "grey"
                            elevation: 6
                            MDLabel:
                                text: "Liste des actes de naissance"
                                halign: "center"
                                theme_text_color:"Custom"
                                text_color:'white'
                                font_style:'H3'
                                font_name:'font\AkayaKanadaka-Regular.ttf'
                                bold: True
                                

                        MDCard:
                            pos:10,450
                            size_hint: .98, .15
                            focus_behavior: False
                            md_bg_color: "darkgrey"
                            unfocus_color: "darkgrey"
                            focus_color: "grey"
                            elevation: 6
                            BoxLayout:
                                orientation:'horizontal'
                            
                                MDDropDownItem:
                                    id: fonction
                                    size_hint_x: 0.18
                                    pos_hint: {'center_x': .5, 'center_y': .5}
                                    text: 'Sélectionnez'
                                    on_release:  app.menu.open()
                                

                                MDTextField:
                                    id: researchnaissancesp
                                    width: "100dp"
                                    mode: "round"
                                    size_hint_x: 0.5
                                    md_bg_color:(217/255,217/255,217/255,100)
                                    size_hint_y: None
                                    pos_hint: {"center_x": 0, "center_y": .5}
                                    padding_x:20
                                BoxLayout:
                                    orientation:'horizontal'
                        MDBoxLayout:
                            orientation:'horizontal'
                            id:boxtablenaissancesp
                            pos:10,30


                    #SCREEN ACTE DE MARIAGE
                    MDScreen:
                        name: "actemariage_sp"

                        MDCard:
                            pos:10,550
                            size_hint: .98, .15
                            focus_behavior: False
                            md_bg_color: "darkgrey"
                            unfocus_color: "darkgrey"
                            focus_color: "grey"
                            elevation: 6
                            MDLabel:
                                text: "Liste des actes de mariage"
                                halign: "center"
                                theme_text_color:"Custom"
                                text_color:'white'
                                font_style:'H3'
                                font_name:'font\AkayaKanadaka-Regular.ttf'
                                bold: True
                                

                        MDCard:
                            pos:10,450
                            size_hint: .98, .15
                            focus_behavior: False
                            md_bg_color: "darkgrey"
                            unfocus_color: "darkgrey"
                            focus_color: "grey"
                            elevation: 6
                            BoxLayout:
                                orientation:'horizontal'
                            
                                MDDropDownItem:
                                    id: fonction
                                    size_hint_x: 0.18
                                    pos_hint: {'center_x': .5, 'center_y': .5}
                                    text: 'Sélectionnez'
                                    on_release:  app.menu.open()
                                

                                MDTextField:
                                    id: researchmariagesp
                                    width: "100dp"
                                    mode: "round"
                                    size_hint_x: 0.5
                                    md_bg_color:(217/255,217/255,217/255,100)
                                    size_hint_y: None
                                    pos_hint: {"center_x": 0, "center_y": .5}
                                    padding_x:20
                                BoxLayout:
                                    orientation:'horizontal'
                        MDBoxLayout:
                            orientation:'horizontal'
                            id:boxtablemariagesp
                            pos:10,30

                    #SCREEN ACTE DE DECES
                    MDScreen:
                        name: "actedeces_sp"

                        MDCard:
                            pos:10,550
                            size_hint: .98, .15
                            focus_behavior: False
                            md_bg_color: "darkgrey"
                            unfocus_color: "darkgrey"
                            focus_color: "grey"
                            elevation: 6
                            MDLabel:
                                text: "Liste des actes de décès"
                                halign: "center"
                                theme_text_color:"Custom"
                                text_color:'white'
                                font_style:'H3'
                                font_name:'font\AkayaKanadaka-Regular.ttf'
                                bold: True
                                

                        MDCard:
                            pos:10,450
                            size_hint: .98, .15
                            focus_behavior: False
                            md_bg_color: "darkgrey"
                            unfocus_color: "darkgrey"
                            focus_color: "grey"
                            elevation: 6
                            BoxLayout:
                                orientation:'horizontal'
                            
                                MDDropDownItem:
                                    id: fonction
                                    size_hint_x: 0.18
                                    pos_hint: {'center_x': .5, 'center_y': .5}
                                    text: 'Sélectionnez'
                                    on_release:  app.menu.open()
                                

                                MDTextField:
                                    id: researchdecessp
                                    width: "100dp"
                                    mode: "round"
                                    size_hint_x: 0.5
                                    md_bg_color:(217/255,217/255,217/255,100)
                                    size_hint_y: None
                                    pos_hint: {"center_x": 0, "center_y": .5}
                                    padding_x:20
                                BoxLayout:
                                    orientation:'horizontal'
                        MDBoxLayout:
                            orientation:'horizontal'
                            id:boxtabledecessp
                            pos:10,30

                    #SCREEN DE BANCS
                    MDScreen:
                        name: "bancs_sp"

                        MDCard:
                            pos:10,570
                            size_hint: .98, .15
                            focus_behavior: False
                            md_bg_color: "#E2E7F6FF"
                            unfocus_color: "darkgrey"
                            focus_color: "grey"
                            border: 10,10,10,10
                            elevation: 200
                            elevation_color:"#25A4F9FF"
                            MDBoxLayout:
                                orientation:'horizontal'
                                BoxLayout:
                                    orientation:'vertical'
                                    padding:10
                                    MDTextField:
                                        id:nom_marie
                                        pos_hint: {"center_x": 0.5, "center_y": .5}
                                        hint_text:"Nom du marie"
                                        theme_text_color:"Custom"
                                        size_hint: .7, 1
                                        text_color:'black'
                                        mode: "round"
                                        bold: True
                                        md_bg_color:"white"
                                        padding_x:20
                                        padding_y:10

                                    BoxLayout:
                                        orientation:'vertical'
                                
                                    MDTextField:
                                        id:prenom_marie
                                        pos_hint: {"center_x": 0.5, "center_y": .5}
                                        hint_text:"Prénom du marie"
                                        theme_text_color:"Custom"
                                        size_hint: .7, 1
                                        text_color:'black'
                                        mode: "round"
                                        bold: True
                                        md_bg_color:"white"
                                        padding_x:20
                                        padding_y:10
                                       
                                        
                                BoxLayout:
                                    orientation:'vertical'
                                    padding:10
                                    MDTextField:
                                        id:nom_mariee
                                        pos_hint: {"center_x": 0.5, "center_y": .5}
                                        hint_text:"Nom de la mariée"
                                        theme_text_color:"Custom"
                                        size_hint: .7, 1
                                        text_color:'black'
                                        mode: "round"
                                        bold: True
                                        md_bg_color:"white"
                                        padding_x:20
                                        padding_y:10

                                    BoxLayout:
                                        orientation:'vertical'
                                
                                    MDTextField:
                                        id:prenom_mariee
                                        pos_hint: {"center_x": 0.5, "center_y": .5}
                                        hint_text:"Prénom de la mariée"
                                        size_hint: .7, 1
                                        theme_text_color:"Custom"
                                        text_color:'black'
                                        mode: "round"
                                        bold: True
                                        md_bg_color:"white"
                                        padding_x:20
                                        padding_y:10


                                BoxLayout:
                                    orientation:'vertical'
                                    padding:10
                                    MDTextField:
                                        id:identifiant_banc
                                        pos_hint: {"center_x": 0.5, "center_y": .5}
                                        hint_text:"Identifiant du banc "
                                        size_hint: .7, 1
                                        theme_text_color:"Custom"
                                        text_color:'black'
                                        mode: "round"
                                        bold: True
                                        md_bg_color:"white"
                                        padding_x:20
                                        padding_y:10

                                    BoxLayout:
                                        orientation:'vertical'
                                
                                    MDTextField:
                                        id:telephone_declarateur
                                        pos_hint: {"center_x": 0.5, "center_y": .5}
                                        hint_text:"Téléphone du déclarateur"
                                        size_hint: .7, 1
                                        theme_text_color:"Custom"
                                        text_color:'black'
                                        mode: "round"
                                        bold: True
                                        md_bg_color:"white"
                                        padding_x:20
                                        padding_y:10

                        MDCard:
                            pos:10,430
                            size_hint: .98, .15
                            focus_behavior: False
                            md_bg_color: "white"
                            unfocus_color: "darkgrey"
                            focus_color: "grey"
                            elevation: 6
                            MDBoxLayout:
                                orientation:'horizontal'
                                BoxLayout:
                                    orientation:'vertical'
                                    padding:10
                                    MagicButton:
                                        id: enregistrer_banc
                                        text: "    Enregistrer    "
                                        mode: "round"
                                        size_hint: .7, .15
                                        text_color: "black"
                                        on_release: self.grow()
                                        md_bg_color:(76/255,175/255,80/255,100)
                                        pos_hint: {"center_x": .5, "center_y": .5}

                                    BoxLayout:
                                        orientation:'vertical'
                                
                                    MDTextField:
                                        id:prenom_marie
                                        halign: "center"
                                        hint_text:"Prénom du marie"
                                        theme_text_color:"Custom"
                                        text_color:'black'
                                        mode: "round"
                                        bold: True
                                        md_bg_color:(217/255,217/255,217/255,100)
                                        padding_x:20
                                        padding_y:10
                                       
                                        
                                BoxLayout:
                                    orientation:'vertical'
                                    padding:10
                                    MagicButton:
                                        id: modifier_banc
                                        text: "    Modifier    "
                                        mode: "round"
                                        size_hint: .7, .15
                                        text_color: "black"
                                        on_release: self.grow()
                                        md_bg_color:(87/255,84/255,212/255,100)
                                        pos_hint: {"center_x": .5, "center_y": .5}

                                    BoxLayout:
                                        orientation:'vertical'
                                
                                    MDTextField:
                                        id:prenom_mariee
                                        halign: "center"
                                        hint_text:"Prénom de la mariée"
                                        theme_text_color:"Custom"
                                        text_color:'black'
                                        mode: "round"
                                        bold: True
                                        md_bg_color:(217/255,217/255,217/255,100)
                                        padding_x:20
                                        padding_y:10


                                BoxLayout:
                                    orientation:'vertical'
                                    padding:10
                                    MagicButton:
                                        id: supprimer_banc
                                        text: "    Supprimer    "
                                        mode: "round"
                                        size_hint: .7, .15
                                        text_color: "black"
                                        on_release: self.grow()
                                        md_bg_color:(76/255,175/255,212/255,100)
                                        pos_hint: {"center_x": .5, "center_y": .5}

                                    BoxLayout:
                                        orientation:'vertical'
                                
                                    MDTextField:
                                        id:telephone_declarateur
                                        halign: "center"
                                        hint_text:"Téléphone du déclarateur"
                                        theme_text_color:"Custom"
                                        text_color:'black'
                                        mode: "round"
                                        bold: True
                                        md_bg_color:(217/255,217/255,217/255,100)
                                        padding_x:20
                                        padding_y:10
                        MDBoxLayout:
                            orientation:'horizontal'
                            id:boxtablebancssp
                            pos:10,30
                        

                    #SCREEN DE DOCUMENTS
                    MDScreen:
                        name: "documents_sp"

                        MDCard:
                            pos:10,550
                            size_hint: .98, .15
                            focus_behavior: False
                            md_bg_color: "darkgrey"
                            unfocus_color: "darkgrey"
                            focus_color: "grey"
                            elevation: 6
                            MDLabel:
                                text: "Liste des documents"
                                halign: "center"
                                theme_text_color:"Custom"
                                text_color:'white'
                                font_style:'H3'
                                font_name:'font\AkayaKanadaka-Regular.ttf'
                                bold: True
                                

                        MDCard:
                            pos:10,450
                            size_hint: .98, .15
                            focus_behavior: False
                            md_bg_color: "darkgrey"
                            unfocus_color: "darkgrey"
                            focus_color: "grey"
                            elevation: 6
                            BoxLayout:
                                orientation:'horizontal'
                            
                                MDDropDownItem:
                                    id: fonction
                                    size_hint_x: 0.18
                                    pos_hint: {'center_x': .5, 'center_y': .5}
                                    text: 'Sélectionnez'
                                    on_release:  app.menu.open()
                                

                                MDTextField:
                                    id: researchdocumentsp
                                    width: "100dp"
                                    mode: "round"
                                    size_hint_x: 0.5
                                    md_bg_color:(217/255,217/255,217/255,100)
                                    size_hint_y: None
                                    pos_hint: {"center_x": 0, "center_y": .5}
                                    padding_x:20
                                BoxLayout:
                                    orientation:'horizontal'
                        MDBoxLayout:
                            orientation:'horizontal'
                            id:boxtabledocumentsp
                            pos:10,30
                    
                    #SCREEN DE EMPLOYES
                    MDScreen:
                        name: "employés_sp"

                        MDCard:
                            pos:10,550
                            size_hint: .98, .15
                            focus_behavior: False
                            md_bg_color: "darkgrey"
                            unfocus_color: "darkgrey"
                            focus_color: "grey"
                            elevation: 6
                            MDLabel:
                                text: "Liste des employés"
                                halign: "center"
                                theme_text_color:"Custom"
                                text_color:'white'
                                font_style:'H3'
                                font_name:'font\AkayaKanadaka-Regular.ttf'
                                bold: True
                                

                        MDCard:
                            pos:10,450
                            size_hint: .98, .15
                            focus_behavior: False
                            md_bg_color: "darkgrey"
                            unfocus_color: "darkgrey"
                            focus_color: "grey"
                            elevation: 6
                            BoxLayout:
                                orientation:'horizontal'
                            
                                MDDropDownItem:
                                    id: fonction
                                    size_hint_x: 0.18
                                    pos_hint: {'center_x': .5, 'center_y': .5}
                                    text: 'Sélectionnez'
                                    on_release:  app.menu.open()
                                

                                MDTextField:
                                    id: researchemployesp
                                    width: "100dp"
                                    mode: "round"
                                    size_hint_x: 0.5
                                    md_bg_color:(217/255,217/255,217/255,100)
                                    size_hint_y: None
                                    pos_hint: {"center_x": 0, "center_y": .5}
                                    padding_x:20
                                BoxLayout:
                                    orientation:'horizontal'
                        MDBoxLayout:
                            orientation:'horizontal'
                            id:boxtableemployesp
                            pos:10,30

                    #SCREEN DE PROJETS
                    MDScreen:
                        name: "projets_sp"

                        MDCard:
                            pos:10,550
                            size_hint: .98, .15
                            focus_behavior: False
                            md_bg_color: "darkgrey"
                            unfocus_color: "darkgrey"
                            focus_color: "grey"
                            elevation: 6
                            MDLabel:
                                text: "Liste des projets"
                                halign: "center"
                                theme_text_color:"Custom"
                                text_color:'white'
                                font_style:'H3'
                                font_name:'font\AkayaKanadaka-Regular.ttf'
                                bold: True
                                

                        MDCard:
                            pos:10,450
                            size_hint: .98, .15
                            focus_behavior: False
                            md_bg_color: "darkgrey"
                            unfocus_color: "darkgrey"
                            focus_color: "grey"
                            elevation: 6
                            BoxLayout:
                                orientation:'horizontal'
                            
                                MDDropDownItem:
                                    id: fonction
                                    size_hint_x: 0.18
                                    pos_hint: {'center_x': .5, 'center_y': .5}
                                    text: 'Sélectionnez'
                                    on_release:  app.menu.open()
                                

                                MDTextField:
                                    id: researchprojetsp
                                    width: "100dp"
                                    mode: "round"
                                    size_hint_x: 0.5
                                    md_bg_color:(217/255,217/255,217/255,100)
                                    size_hint_y: None
                                    pos_hint: {"center_x": 0, "center_y": .5}
                                    padding_x:20
                                BoxLayout:
                                    orientation:'horizontal'
                        MDBoxLayout:
                            orientation:'horizontal'
                            id:boxtableprojetsp
                            pos:10,30

                    #SCREEN DE RDV
                    MDScreen:
                        name: "rdv_sp"

                        MDCard:
                            pos:10,550
                            size_hint: .98, .15
                            focus_behavior: False
                            md_bg_color: "darkgrey"
                            unfocus_color: "darkgrey"
                            focus_color: "grey"
                            elevation: 6
                            MDLabel:
                                text: "Liste des rendez-vous"
                                halign: "center"
                                theme_text_color:"Custom"
                                text_color:'white'
                                font_style:'H3'
                                font_name:'font\AkayaKanadaka-Regular.ttf'
                                bold: True
                                

                        MDCard:
                            pos:10,450
                            size_hint: .98, .15
                            focus_behavior: False
                            md_bg_color: "darkgrey"
                            unfocus_color: "darkgrey"
                            focus_color: "grey"
                            elevation: 6
                            BoxLayout:
                                orientation:'horizontal'
                            
                                MDDropDownItem:
                                    id: fonction
                                    size_hint_x: 0.18
                                    pos_hint: {'center_x': .5, 'center_y': .5}
                                    text: 'Sélectionnez'
                                    on_release:  app.menu.open()
                                

                                MDTextField:
                                    id: researchrdvsp
                                    width: "100dp"
                                    mode: "round"
                                    size_hint_x: 0.5
                                    md_bg_color:(217/255,217/255,217/255,100)
                                    size_hint_y: None
                                    pos_hint: {"center_x": 0, "center_y": .5}
                                    padding_x:20
                                BoxLayout:
                                    orientation:'horizontal'
                        MDBoxLayout:
                            orientation:'horizontal'
                            id:boxtablerdvsp
                            pos:10,30

                    #SCREEN DE PERSONNES
                    MDScreen:
                        name: "personnes_sp"

                        MDCard:
                            pos:10,570
                            size_hint: .98, .12
                            focus_behavior: False
                            md_bg_color: "#E2E7F6FF"
                            unfocus_color: "darkgrey"
                            focus_color: "grey"
                            border: 10,10,10,10
                            elevation: 200
                            elevation_color:"#25A4F9FF"
                            MDBoxLayout:
                                orientation:'horizontal'
                                BoxLayout:
                                    orientation:'vertical'
                                    padding:10
                                    MDTextField:
                                        id:nom_personne
                                        pos_hint: {"center_x": 0.5, "center_y": .5}
                                        hint_text:"Nom de la personne"
                                        theme_text_color:"Custom"
                                        size_hint: .7, 0.8
                                        text_color:'black'
                                        mode: "round"
                                        bold: True
                                        md_bg_color:"white"
                                        padding_x:20
                                        padding_y:10

                                    MDBoxLayout:
                                        orientation:'horizontal'    
                                       
                                        
                                BoxLayout:
                                    orientation:'vertical'
                                    padding:10
                                    MDTextField:
                                        id:prenom_personne
                                        pos_hint: {"center_x": 0.5, "center_y": .5}
                                        hint_text:"Prénom de la personne"
                                        theme_text_color:"Custom"
                                        size_hint: .7, 0.8
                                        text_color:'black'
                                        mode: "round"
                                        bold: True
                                        md_bg_color:"white"
                                        padding_x:20
                                        padding_y:10

                                    MDBoxLayout:
                                        orientation:'horizontal'


                                BoxLayout:
                                    orientation:'vertical'
                                    padding:10
                                    MDTextField:
                                        id:telephone_personne
                                        pos_hint: {"center_x": 0.5, "center_y": .5}
                                        hint_text:"Numéro de téléphone"
                                        required: True
                                        max_text_length: 8
                                        theme_text_color:"Custom"
                                        size_hint: .7, 0.8
                                        text_color:'black'
                                        mode: "round"
                                        bold: True
                                        background_color:"white"
                                        padding_x:20
                                        padding_y:10

                                    MDBoxLayout:
                                        orientation:'horizontal'


                        MDCard:
                            pos:10,430
                            size_hint: .98, .15
                            focus_behavior: False
                            md_bg_color: "white"
                            unfocus_color: "darkgrey"
                            focus_color: "grey"
                            elevation: 6
                            MDBoxLayout:
                                orientation:'horizontal'
                                BoxLayout:
                                    orientation:'vertical'
                                    padding:10
                                    MagicButton:
                                        id: enregistrer_personne
                                        text: "    Enregistrer    "
                                        mode: "round"
                                        size_hint: .7, .15
                                        text_color: "black"
                                        on_release: 
                                            self.grow()
                                            app.enregistrer_personne()
                                        md_bg_color:(76/255,175/255,80/255,100)
                                        pos_hint: {"center_x": .5, "center_y": .5}

                                    BoxLayout:
                                        orientation:'vertical'

                                    MDTextField:
                                        id:recherche_personnesp
                                        pos_hint: {"center_x": 0.5, "center_y": .5}
                                        hint_text:"Rechercher ici"
                                        icon_left:"magnify"
                                        theme_text_color:"Custom"
                                        size_hint: .7, 1.1
                                        text_color:'black'
                                        mode: "round"
                                        bold: True
                                        background_color:"white"
                                        padding_x:20
                                        padding_y:10
                                        on_text:
                                            app.rechercher_personne()
                                    
                                
                                   
                                        
                                BoxLayout:
                                    orientation:'vertical'
                                    padding:10
                                    MagicButton:
                                        id: modifier_personne
                                        text: "    Modifier    "
                                        mode: "round"
                                        size_hint: .7, .15
                                        text_color: "black"
                                        on_release: 
                                            self.grow()
                                            app.modifier_personne()
                                        md_bg_color:(87/255,84/255,212/255,100)
                                        pos_hint: {"center_x": .5, "center_y": .5}

                                    BoxLayout:
                                        orientation:'vertical'
                                
                                    

                                BoxLayout:
                                    orientation:'vertical'
                                    padding:10
                                    MagicButton:
                                        id: supprimer_personne
                                        text: "    Supprimer    "
                                        mode: "round"
                                        size_hint: .7, .15
                                        text_color: "black"
                                        on_release: 
                                            self.grow()
                                            app.supprimer_personne()
                                        md_bg_color:(213/255,0/255,0/255,50)
                                        pos_hint: {"center_x": .5, "center_y": .5}

                                    BoxLayout:
                                        orientation:'vertical'
                                
                                    
                        MDBoxLayout:
                            orientation:'horizontal'
                            id:boxtabledpersonnesp
                            pos:10,30
                    
                    #SCREEN DE COMPTABILITE
                    MDScreen:
                        name: "comptabilité_sp"

                        MDLabel:
                            text: "comptabilité"
                            halign: "center"
            

                MDNavigationDrawer:
                    id: nav_drawersp
                    radius: (0, 16, 16, 0)
                    md_bg_color:(87/255,84/255,212/255,100)
                    ContentNavigationDrawerSP:
                        orientation:'vertical'
                        screen_managersp: screen_managersp
                        nav_drawersp: nav_drawersp
        #LA FIN DU SCREEN SECRETAIRE PRINCIPAL

    #LA FIN DU SCREENMANAGER manager1                   
'''