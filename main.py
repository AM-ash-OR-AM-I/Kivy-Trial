from kivymd.app import MDApp
from farmersmapview import FarmersMapView
from searchpopupmenu import SearchPopupMenu
import sqlite3
from gpshelper import GpsHelper
class MainApp(MDApp):
    connection = None
    cursor = None
    search_menu = None

    def on_start(self):
        self.theme_cls.primary_palette = "BlueGray"
        # Initialize GPS
        GpsHelper().run()
        # Connect to Database
        self.connection = sqlite3.connect('markets.db')
        self.cursor = self.connection.cursor()

        # Instantiate SearchPopupMenu
        self.search_menu = SearchPopupMenu()

MainApp().run()