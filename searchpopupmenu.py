from kivymd.uix.dialog import MDInputDialog
from urllib.parse import quote
from kivy.network.urlrequest import UrlRequest
from kivy.app import App
import certifi
from kivy.clock import Clock

class SearchPopupMenu(MDInputDialog):
    title = 'Search by Address'
    text_button_ok = 'Search'

    def __init__(self):
        super().__init__()
        self.size_hint = [.9, .3]
        self.events_callback = self.callback

    def open(self):
        super().open()
        Clock.schedule_once(self.set_field_focus, 0.5)

    def callback(self, *args):
        address = self.text_field.text
        self.geocode_get_lat_lon(address)

    def geocode_get_lat_lon(self, address):
        address = quote(address)
        api_key = "jspHzeMeAxIm3GmSSyiVFV9ZD36sI61FWQjSrvRF134"
        url = f"https://geocoder.ls.hereapi.com/6.2/geocode.json?searchtext={address}&apiKey={api_key}"
        UrlRequest(url, on_success=self.success, on_failure=self.failure, on_error=self.failure)

    def success(self, urlrequest, result):
        print("Success")
        latitude = result['Response']['View'][0]['Result'][0]['Location']['NavigationPosition'][0]['Latitude']
        longitude = result['Response']['View'][0]['Result'][0]['Location']['NavigationPosition'][0]['Longitude']
        app = App.get_running_app()
        mapview = app.root.ids.mapview
        mapview.center_on(latitude, longitude)

    def error(self, urlrequest, result):
        print("error")
        print(result)

    def failure(self, urlrequest, result):
        print("failure")
        print(result)

