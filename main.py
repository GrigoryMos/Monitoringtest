#pip install kivy
#pip install kivymd
#pip install https://github.com/kivymd/KivyMD/archive/3274d62.zip

from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ListProperty

from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import OneLineIconListItem, MDList

from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout

from kivymd.font_definitions import fonts
from kivymd.icon_definitions import md_icons

from kivymd.uix.menu import MDDropdownMenu
from kivy.clock import Clock

from kivymd.uix.picker import MDDatePicker
import datetime
import calendar

from kivy.graphics import Color, Rectangle, Line, Ellipse
from random import random as r

KV = '''
#https://stackoverflow.com/questions/65698145/kivymd-tab-name-containing-icons-and-text
# this import will prevent disappear tabs through some clicks on them)))
#:import md_icons kivymd.icon_definitions.md_icons
#:import fonts kivymd.font_definitions.fonts

# Menu item in the DrawerList list.
<ItemDrawer>:
    theme_text_color: "Custom"
    on_release: self.parent.set_color_item(self)

    IconLeftWidget:
        id: icon
        icon: root.icon
        theme_text_color: "Custom"
        text_color: root.text_color


<ContentNavigationDrawer>:
    orientation: "vertical"
    padding: "8dp"
    spacing: "8dp"

    AnchorLayout:
        anchor_x: "left"
        size_hint_y: None
        height: avatar.height

        Image:
            id: avatar
            size_hint: None, None
            size: "56dp", "56dp"
            source: "data/logo/kivy-icon-256.png"

    MDLabel:
        text: app.title
        font_style: "Button"
        size_hint_y: None
        height: self.texture_size[1]

    MDLabel:
        text: app.by_who
        font_style: "Caption"
        size_hint_y: None
        height: self.texture_size[1]



    ScrollView:

        DrawerList:
            id: md_list



Screen:

    MDNavigationLayout:

        ScreenManager:

            Screen:

                BoxLayout:
                    orientation: 'vertical'

                    MDToolbar:
                        title: app.title
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.set_state("open")]]
                        right_action_items: [["star-outline", lambda x: app.on_star_click()]]
                        md_bg_color: 0, 0, 0, 1
                        
                    MDTabs:
                        id: tabs
                        on_tab_switch: app.on_tab_switch(*args)                        
                        height: "48dp"
                        tab_indicator_anim: False
                        background_color: 0.1, 0.1, 0.1, 1
                    
                        Tab:
                            id: tab1
                            name: 'tab1'
                            text: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['calculator-variant']}[/size][/font] ????????????"
                            
                            BoxLayout:
                                orientation: 'vertical'
                                padding: "10dp"   
                                
                                BoxLayout:
                                    orientation: 'horizontal'                               
                                    
                                    MDIconButton:
                                        icon: "calendar-month"
                                        
                                    MDTextField:
                                        id: start_date
                                        hint_text: "????????????"
                                        on_focus: if self.focus: app.date_dialog.open()
                                
                                BoxLayout:
                                    orientation: 'horizontal'                         
                                    
                                    MDIconButton:
                                        icon: "numeric-5-circle-outline"
                                        
                                    MDTextField:
                                        id: needs
                                        hint_text: "?????????????????????? ????????????/??????????"
                                    
                                BoxLayout:
                                    orientation: 'horizontal'                                
                                    
                                    MDIconButton:
                                        icon: "clock-time-five-outline"
                                            
                                    MDTextField:
                                        id: months
                                        hint_text: "?????????????? ?????????????? (?? ??????????????)"
                                    
                                BoxLayout:
                                    orientation: 'horizontal'                                 
                                    
                                    MDIconButton:
                                        icon: "pencil-plus"
                                            
                                    MDTextField:
                                        id: pars
                                        hint_text: "???????????????????? ??????"
                                    
                                    MDTextField:
                                        id: rereceive_type
                                        hint_text: "????????????"
                                        on_focus: if self.focus: app.menu.open()
                                
                                MDSeparator:
                                    height: "1dp"
                                    
                                
                                BoxLayout:
                                    orientation: 'horizontal'
                                    
                                    AnchorLayout:
                                        anchor_x: 'center'
                                
                                        MDRectangleFlatIconButton:
                                            icon: "android"
                                            text: "BUTTON1"
                                            theme_text_color: "Custom"
                                            text_color: 1, 1, 1, 1
                                            line_color: 0, 0, 0, 1
                                            icon_color: 1, 0, 0, 1
                                            md_bg_color: 0.1, 0.1, 0.1, 1
                                            adaptive_width: True
                                            on_release: app.monit_table(*args)
                                    
                                    AnchorLayout:
                                        anchor_x: 'center'
                                    
                                        MDRectangleFlatIconButton:
                                            icon: "android"
                                            text: "BUTTON2"
                                            theme_text_color: "Custom"
                                            text_color: 1, 1, 1, 1
                                            line_color: 0, 0, 0, 1
                                            icon_color: 1, 0, 0, 1
                                            md_bg_color: 0.1, 0.1, 0.1, 1
                                    
                                    AnchorLayout:
                                        anchor_x: 'center'
                                        
                                        Button:
                                            text: "Test Ok"
                                            size_hint_y: .5
                                            background_color: (0.1, 0.1, 0.1, 1.0)
                                 
                        
                        Tab:
                            id: tab2
                            name: 'tab2'
                            text: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['table-large']}[/size][/font] ??????????????"
                            
                            BoxLayout:
                                orientation: 'vertical'
                                padding: "10dp" 
                                
                                ScrollView:
                                
                                    MDList:
                                        id: table_list
                        
                        Tab:
                            id: tab3
                            name: 'tab3'
                            text: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['chart-areaspline']}[/size][/font] ????????????"
                              
                            BoxLayout:
                                orientation: 'vertical'
                                padding: "10dp"
                                
                                
                                BoxLayout:
                                    orientation: 'vertical'
                                    padding: "10dp"
                                    size_hint_x: 1
                                    size_hint_y: None
                                    height: 50
                                       
                                    canvas:
                                        Color:
                                            rgba: 0.2, 0.2, 0.2, 0.1
                                        Rectangle:
                                            size: self.size
                                            pos: self.pos
                                                                         
                                    MDLabel:
                                        text: "?????????? ????????????????"
                                        halign: "center"
                                        font_style: "H5"
                                        height: "48dp"
                                    
                                BoxLayout:
                                    orientation: 'vertical'
                                    padding: "10dp"
                                    id: graph
                                    
                                    canvas:
                                        Color:
                                            rgba: 1, 1, 1, 1
                                        Rectangle:
                                            size: self.size
                                            pos: self.pos   
                                
                                BoxLayout:
                                    orientation: 'horizontal'
                                    padding: "10dp"
                                    size_hint_x: 1
                                    size_hint_y: None
                                    height: 50  
                                    
                                    MDIcon:
                                        icon: "checkbox-blank"
                                        halign: "right"
                                        color: 0, 0, 1, 1
                                        
                                    MDLabel:
                                        text: "????????"
                                        halign: "left"
                                        font_style: "H6"
                                        height: "48dp"
                                        
                                    MDIcon:
                                        icon: "checkbox-blank"
                                        halign: "right"
                                        color: 1, 0, 0, 1
                                        
                                    MDLabel:
                                        text: "?? ????????????"
                                        halign: "left"
                                        font_style: "H6"
                                        height: "48dp"   
                        
                        Tab:
                            id: tab4
                            name: 'tab4'
                            text: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['chart-pie']}[/size][/font] ??????????????????"
                            
                            BoxLayout:
                                orientation: 'vertical'
                                padding: "10dp"
                                
                                
                                BoxLayout:
                                    orientation: 'vertical'
                                    padding: "10dp"
                                    size_hint_x: 1
                                    size_hint_y: None
                                    height: 50
                                       
                                    canvas:
                                        Color:
                                            rgba: 0.2, 0.2, 0.2, 0.1
                                        Rectangle:
                                            size: self.size
                                            pos: self.pos
                                                                         
                                    MDLabel:
                                        text: "?????????? ????????????????"
                                        halign: "center"
                                        font_style: "H5"
                                        height: "48dp"
                                    
                                BoxLayout:
                                    orientation: 'vertical'
                                    padding: "10dp"
                                    id: chart
                                    
                                    canvas:
                                        Color:
                                            rgba: 1, 1, 1, .6
                                        Rectangle:
                                            size: self.size
                                            pos: self.pos
                                
                                BoxLayout:
                                    orientation: 'horizontal'
                                    padding: "10dp"
                                    size_hint_x: 1
                                    size_hint_y: None
                                    height: 50  
                                    
                                    MDIcon:
                                        icon: "checkbox-blank"
                                        halign: "right"
                                        color: 0, 0, 1, 1
                                        
                                    MDLabel:
                                        text: "????????"
                                        halign: "left"
                                        font_style: "H6"
                                        height: "48dp"
                                        
                                    MDIcon:
                                        icon: "checkbox-blank"
                                        halign: "right"
                                        color: 1, 0, 0, 1
                                        
                                    MDLabel:
                                        text: "?? ????????????"
                                        halign: "left"
                                        font_style: "H6"
                                        height: "48dp"
                        
                        Tab:
                            id: tab5
                            name: 'tab5'
                            text: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['book-open-variant']}[/size][/font] ??????????????"
         
                    
        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                id: content_drawer

<ItemTable>:
    size_hint_y: None
    height: "42dp"

    canvas:
        Color:
            rgba: root.color
        Rectangle:
            size: self.size
            pos: self.pos

    MDLabel:
        text: root.num
        halign: "center"
    MDLabel:
        text: root.date
        halign: "center"
    MDLabel:
        text: root.rereceive
        halign: "center"
    MDLabel:
        text: root.pars
        halign: "center"
    MDLabel:
        text: root.principal
        halign: "center"
    MDLabel:
        text: root.debt
        halign: "center"
                        
'''


class ContentNavigationDrawer(BoxLayout):
    pass


class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()
    text_color = ListProperty((0, 0, 0, 1))


class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):
        """Called when tap on a menu item."""

        # Set the color of the icon and text for the menu item.
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color


class Tab(MDFloatLayout, MDTabsBase):
    pass


class ItemTable(BoxLayout):
    num = StringProperty()
    date = StringProperty()
    rereceive = StringProperty()
    pars = StringProperty()
    principal = StringProperty()
    debt = StringProperty()
    color = ListProperty()


# https://stackoverflow.com/questions/2249956/how-to-get-the-same-day-of-next-month-of-a-given-day-in-python-using-datetime
def next_month_date(d):
    _year = d.year + (d.month // 12)
    _month = 1 if (d.month // 12) else d.month + 1
    next_month_len = calendar.monthrange(_year, _month)[1]
    next_month = d
    if d.day > next_month_len:
        next_month = next_month.replace(day=next_month_len)
    next_month = next_month.replace(year=_year, month=_month)
    return next_month


#https://kivy.org/doc/stable/examples/gen__canvas__canvas_stress__py.html
def show_canvas_stress(wid):
    with wid.canvas:
        for x in range(10):
            Color(r(), 1, 1, mode='hsv')
            Rectangle(pos=(r() * wid.width + wid.x, r() * wid.height + wid.y), size=(20, 20))



def draw_graph(wid, start_date, needs, months, pars, rereceive_type):
    #print(wid.x, wid.y)
    with wid.canvas:
        Color(.2, .2, .2, 1)
        Line(rectangle=(wid.x, wid.y, wid.width, wid.height), width=1)
    graph_height = wid.height
    delta_width = wid.width / months

    percent = pars / 100 / 12
    monthly_score = needs * (percent + percent / ((1 + percent) ** months - 1))

    debt_end_month = needs
    for i in range(0, months):
        rereceive_of_pars = debt_end_month * percent
        rereceive_of_needs_body = monthly_score - rereceive_of_pars
        debt_end_month = debt_end_month - rereceive_of_needs_body
        delta_height_pars = int(rereceive_of_pars * graph_height / monthly_score)
        delta_height_needs = int(rereceive_of_needs_body * graph_height / monthly_score)
        print("####: ", delta_height_needs, delta_height_needs)
        print(monthly_score, rereceive_of_pars, rereceive_of_needs_body, debt_end_month)
        with wid.canvas:
            Color(1, 0, 0, 1)
            Rectangle(pos=(wid.x + int(i * delta_width), wid.y), size=(int(delta_width), delta_height_needs))
            Color(0, 0, 1, 1)
            Rectangle(pos=(wid.x + int(i * delta_width), wid.y+delta_height_needs), size=(int(delta_width), delta_height_pars))

def draw_chart(wid, total_amount_of_rereceives, needs):
    pars_chart = ((total_amount_of_rereceives - needs) * 360) / total_amount_of_rereceives
    circle_width = wid.width
    center_x = 0
    center_y = wid.height // 2 - circle_width // 2
    if (wid.width > wid.height):
        circle_width = wid.height
        center_x = wid.width // 2 - circle_width // 2
        center_y = 0
    #print(wid.x, wid.y)
    with wid.canvas:
        Color(0, 0, 1, 1)
        Ellipse(pos=(wid.x+center_x, wid.y+center_y), size=(circle_width, circle_width), angle_start=360-int(pars_chart), angle_end=360)
        Color(1, 0, 0, 1)
        Ellipse(pos=(wid.x+center_x, wid.y+center_y), size=(circle_width, circle_width), angle_start=0, angle_end=360-int(pars_chart))

class MonitoringApp(MDApp):
    title = "Monitoring for academic achievements"
    by_who = "Moscow Polytech"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(KV)
        #https://kivymd.readthedocs.io/en/latest/components/menu/?highlight=MDDropDownItem#center-position
        #menu_items = [{"icon": "git", "text": f"Item {i}"} for i in range(5)]
        menu_items = [{"icon": "format-text-rotation-angle-up", "text": "???? ??????????????????????"}, {"icon": "format-text-rotation-angle-down", "text": "???? ????????????????"}]
        self.menu = MDDropdownMenu(
            caller=self.screen.ids.rereceive_type,
            items=menu_items,
            position="auto",
            width_mult=4,
        )
        self.menu.bind(on_release=self.set_item)

        #https://kivymd.readthedocs.io/en/latest/components/pickers/?highlight=date%20picker#
        self.date_dialog = MDDatePicker(
            callback=self.get_date,
            background_color=(0.1, 0.1, 0.1, 1.0),
        )

    def set_item(self, instance_menu, instance_menu_item):
        def set_item(interval):
            self.screen.ids.rereceive_type.text = instance_menu_item.text
            instance_menu.dismiss()

        Clock.schedule_once(set_item, 0.5)

    def get_date(self, date):
        '''
        :type date: <class 'datetime.date'>
        '''
        print(date)
        self.screen.ids.start_date.text = date.strftime("%d-%m-%Y") # str(date)

    def build(self):
        # self.theme_cls.theme_style = "Light"  # "Dark"  # "Light"
        # return Builder.load_string(KV)
        return self.screen

    def on_start(self):
        self.screen.ids.start_date.text = datetime.date.today().strftime("%d-%m-%Y")
        self.screen.ids.needs.text = "50"
        self.screen.ids.months.text = "3"
        self.screen.ids.pars.text = "10"
        self.screen.ids.rereceive_type.text = "???? ??????????????????????"

        icons_item_menu_lines = {
            "order-numeric-ascending": "????????????",
            "human-queue": "????????????",
            "head-plus-outline": "??????????????????????????",
            "format-list-text": "????????????????????",
            "share-variant": "????????????????????",  #air-horn
            "shield-sun": "Dark/Light",
        }
        icons_item_menu_tabs = {
            "calculator-variant": "????????????",  #ab-testing
            "table-large": "??????????????",
            "chart-areaspline": "????????????",
            "chart-pie": "??????????????????",  # chart-arc
            "book-open-variant": "??????????????",
        }
        for icon_name in icons_item_menu_lines.keys():
            self.root.ids.content_drawer.ids.md_list.add_widget(
                ItemDrawer(icon=icon_name, text=icons_item_menu_lines[icon_name])
            )

        # To auto generate tabs
        # for icon_name, name_tab in icons_item_menu_tabs.items():
        #     self.root.ids.tabs.add_widget(
        #         Tab(
        #             text=f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons[icon_name]}[/size][/font] {name_tab}"
        #         )
        #     )

    def on_tab_switch(self, instance_tabs, instance_tab, instance_tab_label, tab_text):
        '''Called when switching tabs.

        :type instance_tabs: <kivymd.uix.tab.MDTabs object>;
        :param instance_tab: <__main__.Tab object>;
        :param instance_tab_label: <kivymd.uix.tab.MDTabsLabel object>;
        :param tab_text: text or name icon of tab;
        '''

        print("tab clicked! " + tab_text)

    def on_star_click(self):
        print("star clicked!")

    def monit_table(self, *args):
        print("button1 pressed")
        start_date = self.screen.ids.start_date.text
        needs = self.screen.ids.needs.text
        months = self.screen.ids.months.text
        pars = self.screen.ids.pars.text
        rereceive_type = self.screen.ids.rereceive_type.text
        print(start_date + " " + needs + " " + months + " " + pars + " " + rereceive_type)
        # convert to date object, float, and so on
        start_date = datetime.datetime.strptime(self.screen.ids.start_date.text, "%d-%m-%Y").date()
        needs = float(needs)
        months = int(months)
        pars = float(pars)


        # try to count
        percent = pars / 10 / 12
        monthly_score = needs * (percent + percent / ((1 + percent) ** months - 1))
        # print(monthly_score)

        debt_end_month = needs
        for i in range(0, months):
            rereceive_of_pars = debt_end_month * percent
            rereceive_of_needs_body = monthly_score - rereceive_of_pars
            debt_end_month = debt_end_month - rereceive_of_needs_body
            # print(monthly_score, rereceive_of_pars, rereceive_of_needs_body, debt_end_month)

        total_amount_of_rereceives = monthly_score * months
        overrereceive_needs = total_amount_of_rereceives - needs
        effective_pars_rate = ((total_amount_of_rereceives / needs - 1) / (months / 12)) * 100
        # print(total_amount_of_rereceives, overrereceive_needs, effective_pars_rate)

        # https://kivymd.readthedocs.io/en/latest/themes/color-definitions/
        self.screen.ids.table_list.clear_widgets()
        self.screen.ids.table_list.add_widget(
            ItemTable(
                color=(0.2, 0.2, 0.2, 0.5),
                num="???",
                date="???????? ????????????",
                rereceive="????????????????",
                pars="????????",
                principal="?? ????????????",
                debt="??????????????",
            )
        )

        debt_end_month = needs
        for i in range(0, months):
            row_color = (1, 1, 1, 1)
            if (i % 2 != 0):
                row_color = (0.2, 0.2, 0.2, 0.1)
            rereceive_of_pars = debt_end_month * percent
            rereceive_of_needs_body = monthly_score - rereceive_of_pars
            debt_end_month = debt_end_month - rereceive_of_needs_body

            self.screen.ids.table_list.add_widget(
                ItemTable(
                    color=row_color,  # (0, 0, 0, 1),
                    num=str(i + 1),
                    date=start_date.strftime("%d-%m-%Y"),
                    rereceive=str(round(monthly_score, 2)),
                    pars=str(round(rereceive_of_pars, 2)),
                    principal=str(round(rereceive_of_needs_body, 2)),
                    debt=str(round(debt_end_month, 2)),
                )
            )

            # d = datetime.datetime.today()
            # print(next_month_date(d))
            # start_date = start_date + datetime.timedelta(days=30)
            start_date = next_month_date(start_date)

        # wid = self.screen.ids.graph
        # with wid.canvas:
        #     for x in range(10):
        #         Color(r(), 1, 1, mode='hsv')
        #         Rectangle(pos=(r() * wid.width + wid.x,
        #                        r() * wid.height + wid.y), size=(20, 20))
        #
        # wid = self.screen.ids.chart
        # with wid.canvas:
        #     for x in range(10):
        #         Color(r(), 1, 1, mode='hsv')
        #         Rectangle(pos=(r() * wid.width + wid.x,
        #                        r() * wid.height + wid.y), size=(20, 20))

        # show_canvas_stress(self.screen.ids.graph)
        show_canvas_stress(self.screen.ids.chart)

        self.screen.ids.graph.canvas.clear()
        draw_graph(self.screen.ids.graph, start_date, needs, months, pars, rereceive_type)

        self.screen.ids.chart.canvas.clear()
        draw_chart(self.screen.ids.chart, total_amount_of_rereceives, needs)

        pass


MonitoringApp().run()