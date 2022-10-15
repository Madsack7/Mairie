from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''
MDScreen:

    MDCard:
        size_hint: .7, .4
        focus_behavior: True
        pos_hint: {"center_x": .5, "center_y": .5}
        md_bg_color: "darkgrey"
        unfocus_color: "darkgrey"
        focus_color: "grey"
        elevation: 6
'''


class Example(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)


Example().run()